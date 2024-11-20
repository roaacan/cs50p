import argparse


parser = argparse.ArgumentParser(description="Say hello")
parser.add_argument("-n", default=1 ,help="number of times to hello", type=int)
args = parser.parse_args() # Values of the arguments

for _ in range(args.n):
    print("hello")