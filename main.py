import argparse
from pathlib import Path

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("-i", "--input", required=True)
    args = parser.parse_args()


if __name__ == "__main__":
    main()
