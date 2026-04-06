"""Evaluation script. Usage: python scripts/evaluate.py --checkpoint checkpoints/latest.pt"""
import argparse


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--checkpoint", required=True)
    args = parser.parse_args()
    print(f"Evaluating checkpoint: {args.checkpoint}")
    # TODO: load model, run eval loop


if __name__ == "__main__":
    main()
