import argparse

parser = argparse.ArgumentParser()

parser.add_argument('-f', '--file')
parser.add_argument('-se', '--sepia')
parser.add_argument('-g', '--gray')
parser.add_argument('-sc', '--scale')
parser.add_argument('-i', '--implement')
parser.add_argument('-o', '--out')

args = parser.parse_args()
print(args)
