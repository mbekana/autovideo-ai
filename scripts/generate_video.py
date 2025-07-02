import argparse
from autovideo.workflow.auto_pipeline import run_pipeline

parser = argparse.ArgumentParser()
parser.add_argument("--script", type=str, required=True)
parser.add_argument("--assets", type=str, required=True)
parser.add_argument("--output", type=str, required=True)
parser.add_argument("--davinci", action='store_true')
args = parser.parse_args()

with open(args.script, "r") as f:
    script_text = f.read()

run_pipeline(script_text, args.assets, args.output, args.davinci)
