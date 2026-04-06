"""Article ingestion. Usage: python scripts/ingest.py --source newsapi --limit 500"""
import argparse


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--source", default="newsapi")
    parser.add_argument("--limit", type=int, default=100)
    args = parser.parse_args()
    print(f"Ingesting {args.limit} articles from {args.source}")
    # TODO: call NewsAPI, persist to DB


if __name__ == "__main__":
    main()
