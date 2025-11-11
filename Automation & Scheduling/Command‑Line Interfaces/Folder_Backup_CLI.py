# Memory Trick: ARG = Ask, Receive, Go! (define → parse → use)

import argparse , shutil 
p=argparse.ArgumentParser(description="simple folder backup")
p.add_argument("--src",required=True)
p.add_argument("--dst",required=True)
args = p.parse_args()

shutil.copytree(args.src , args.dst , dirs_exist_ok=True)
print(f"Backup {args.src} -> {args.dst}")