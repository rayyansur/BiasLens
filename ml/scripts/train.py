"""Fine-tuning script. Usage: python scripts/train.py --config configs/bias_classifier.yaml"""
import argparse


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--config", required=True)
    args = parser.parse_args()
    print(f"Training with config: {args.config}")
    # TODO: load config, dataset, trainer


if __name__ == "__main__":
    main()
