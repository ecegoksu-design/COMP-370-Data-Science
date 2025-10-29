"""
Count the number of unique author IDs in the dataset.
"""

import argparse
import json
import os

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("data_file", help="Path to the data file containing author IDs")
    parser.add_argument("--blacklist", help="Path to the JSON file containing blacklisted author IDs", default="data/author_id_blacklist.json")

    args = parser.parse_args()
    author_ids = set()
    author_id_blacklist = set()

    # Load blacklist if file exists and is not empty
    if args.blacklist and os.path.exists(args.blacklist):
        try:
            with open(args.blacklist, "r") as bl_fh:
                blacklist_data = json.load(bl_fh)
                if isinstance(blacklist_data, list):
                    author_id_blacklist = set(blacklist_data)
                else:
                    print(f"Warning: Blacklist file {args.blacklist} does not contain a valid list")
        except json.JSONDecodeError as e:
            print(f"Warning: Could not parse blacklist file {args.blacklist}: {e}")
            print("Continuing without blacklist...")
        except Exception as e:
            print(f"Warning: Error reading blacklist file {args.blacklist}: {e}")
            print("Continuing without blacklist...")
    else:
        print(f"Warning: Blacklist file {args.blacklist} not found. Continuing without blacklist...")

    # Process main data file
    try:
        with open(args.data_file, "r") as fh:
            next(fh)  # Skip header line
            for line in fh:
                parts = line.strip().split(",")
                if len(parts) > 1:
                    author_id = parts[0]  # Fixed the syntax error here
                    if author_id and author_id not in author_id_blacklist:
                        author_ids.add(author_id)
        
        print(f"Number of unique author IDs: {len(author_ids)}")
    
    except FileNotFoundError:
        print(f"Error: Data file {args.data_file} not found")
    except Exception as e:
        print(f"Error processing data file: {e}")

if __name__ == "__main__":
    main()

# python num_author_ids.py --blacklist ../data/author_id_blacklist.json ../data/IRAhandle_tweets_1.csv 