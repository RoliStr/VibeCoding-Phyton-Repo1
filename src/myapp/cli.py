import argparse
from myapp.core import hello

def main():
    p = argparse.ArgumentParser(description="MyApp CLI")
    p.add_argument("--name", default="world")
    args = p.parse_args()
    print(hello(args.name))

if __name__ == "__main__":
    main()
