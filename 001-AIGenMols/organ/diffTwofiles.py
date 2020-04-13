import argparse

parser = argparse.ArgumentParser()
parser.add_argument('-f1','--file1', type=str, default=False, help='The first file.')
parser.add_argument('-f2','--file2', type=str, default=False, help='The second file.')
args = parser.parse_args()

class DifferentTwoFiles(object):

    def __init__(self, f1, f2):
        def proc(fp,tset):
            for line in fp:
                for i in line.split():
                    tset.add(i)
            return tset


        if __name__ == "__main__":
            # file 1
            num1 = set()
            fp = open(f1, "r")
            num1 = proc(fp, num1)
            fp.close()

            # file 2
            num2 = set()
            fp = open(f2, "r")
            num2 = proc(fp, num2)
            fp.close()

            num2 = num2.difference(num1)

            """output file."""
            #print("^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ output",)
            fp = open(f2, "w")
            for i in num2:
                fp.write(i+'\n')
            fp.close()

if args.file1 and args.file2:
    DifferentTwoFiles(args.file1, args.file2)