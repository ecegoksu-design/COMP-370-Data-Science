
""" 
Generate numbers from 0 to n.
"""
import sys
import argparse

def main(): 
    parser = argparse.ArgumentParser()
    parser.add_argument("max_num", type=int, help="The max number that gets generated")
   
    args = parser.parse_args()

    max_num = int(sys.argv[1])

    for i in range(args.max_num):
        print(i)

print("I'm num_generator.py, my name is", __name__)

if __name__ == "__main__":
    main()