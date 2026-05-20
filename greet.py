import argparse
print('Hello from command line!')
parser = argparse.ArgumentParser(description='A friendly greeting script.')
parser.add_argument('--name', help='The name of the person to greet.')
args = parser.parse_args()

if args.name:
 print(f"My name is {args.name}!")