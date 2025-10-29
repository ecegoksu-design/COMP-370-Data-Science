import requests
import json
import os
import argparse

script_dir = os.path.dirname(__file__)
raw_path = os.path.join(script_dir, '..', 'data', 'raw')

def main():
    
    parse = argparse.ArgumentParser()
    parse.add_argument("author")

    args = parse.parse_args()

    author_name = r"octavia%20butler"

    # get author key
    query_url = "https://openlibrary.org/search/authors.json?q=" + author_name
    r = requests.get(query_url)

    author_data = r.json()
    author_key = author_data['docs'][0]['key']
    print("Author Key:", author_key)

    books_url = f"https://openlibrary.org/authors/{author_key}/works.json"
    r = requests.get(books_url)

    books_data = r.json()

    # write out the raw data
    fname = f"author_{author_key}_works.json"
    with open(os.path.join(raw_path, fname), 'w') as f:
        json.dump(books_data, f, indent=4)

if __name__ == "__main__":
    main()
