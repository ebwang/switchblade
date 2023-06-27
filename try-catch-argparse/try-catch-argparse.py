import argparse
parser = argparse.ArgumentParser(description='Read a file')
parser.add_argument('filename', help='the file to read')
parser.add_argument('--limit', '-l', type=int, help='the number of lines to read')
parser.add_argument('--version', '-v', action='version', version='%(prog)s verison 1.0')
args = parser.parse_args()
#Try will try yo open file
try:
    f = open(args.filename)
    limit = args.limit
#Exception with open file
except FileNotFoundError as err:
    print(f"Error: {err}")
#Execute below with no errors
else:
    with f:
        lines = f.readlines()
        #Will reverse the lines 
        lines.reverse()
        if limit:
            lines = lines[:limit]
        for line in lines:
            print(line.strip())