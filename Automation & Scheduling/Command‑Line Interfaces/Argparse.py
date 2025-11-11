# argparse lets users pass options to scripts via the command line, Built‑in module to parse command‑line arguments for scripts (makes automation configurable).
    # add_argument()	= Define an input option
    # parse_args()	= Read user inputs
    # --flag or -f	= Optional argument
    # Positional args	= Mandatory values 
import argparse

parser = argparse.ArgumentParser(description="Simple Calculator CLI")
parser.add_argument("a", type=int, help="First number")
parser.add_argument("b", type=int, help="Second number")
parser.add_argument("--op", choices=["add","sub"], default="add", help="Operation type")
args = parser.parse_args()

if args.op == "add":
    print(f"Sum = {args.a + args.b}")
else:
    print(f"Difference = {args.a - args.b}")

# to run -->python '<file name>' 5 2 --op sub