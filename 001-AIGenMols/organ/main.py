import argparse
from mol_genSample import genFDAFragSamples
from mol_genSample import genFDAMolSamples
from mol_genSample import genZINCMolSamples

parser = argparse.ArgumentParser()
parser.add_argument('-f','--file', type=str, default=False, help='Generated file name.')
parser.add_argument('-n','--num', type=int, default=100, help='The number for generating samples.')
parser.add_argument('-s','--select', type=str, default="", help='The value is: FDAFrag, zinc')
#parser.add_argument('-d', type=int, default=20, help='Delete data number,default 20;')
#parser.add_argument('-m', type=int, default=20, help='Modify the number of data,default 20;')
args = parser.parse_args()
#print("%%%%%%%%%%%%", args.select)
if args.select.lower() == 'FDAFrag'.lower():
    if args.file and args.num:
        genFDAFragSamples(args.file, args.num)

elif args.select.lower() == 'FDAMol'.lower():
    if args.file and args.num:
        genFDAMolSamples(args.file, args.num)

elif args.select.lower() == 'ZINCMol'.lower():
    if args.file and args.num:
        genZINCMolSamples(args.file, args.num)