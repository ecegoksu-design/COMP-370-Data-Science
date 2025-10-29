import argparse 

from comedic import is_comedic_actor

#python analyze_comedics.py ../data/daily_show_acting.csv 
def main():

    parser = argparse.ArgumentParser()
    parser.add_argument("acting_csv")
    args = parser.parse_args()

    acting_names = []
    with open(args.acting_csv) as f:
        f_iter = iter(f)
        header = next(f_iter)
        for line in f_iter:
            name = line.split(",")[-1].strip()
            acting_names.append(name)

if __name__ == "__main__":
    main()