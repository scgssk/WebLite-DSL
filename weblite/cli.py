import argparse
from weblite.builder import build

def main():
    parser = argparse.ArgumentParser(description="WebLite - Build static websites from YAML.")
    parser.add_argument("command", help="The command to execute", choices=["build"])
    parser.add_argument("input", help="The .wl file to build from")
    args = parser.parse_args()

    if args.command == "build":
        build(args.input)
        print(f"✅ Site built successfully from {args.input}. Check the output/ folder!")

if __name__ == "__main__":
    main()
