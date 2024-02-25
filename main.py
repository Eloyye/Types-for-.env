import argparse

from env_type import EnvType, EmptyPathException


def main():
    parser = argparse.ArgumentParser(description="create environment.d.ts file to add types for process.env "
                                                 "environment variables")
    parser.add_argument("input", help="input path to .env file")
    parser.add_argument("-o", "--output", help="input path to .env file")
    args = parser.parse_args()

    inp = args.input

    if inp:
        if args.output:
            EnvType(inp).create_env_ts(args.output)
        else:
            EnvType(inp).create_env_ts()
    else:
        raise EmptyPathException("expected path to be valid instead got empty string")


if __name__ == '__main__':
    main()
