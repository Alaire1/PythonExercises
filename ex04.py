import sys #tested with flake8


def check_arguments():
    num_args = len(sys.argv) - 1
    assert num_args >= 1, "No arguments provided"
    assert num_args <= 1, "More than one argument provided"
    try:
        number = int(sys.argv[1])
    except ValueError:
        raise AssertionError("argument is not a number")
    if number % 2 == 0:
        print("Even")
    else:
        print("Odd")


def main():
    try:
        check_arguments()
    except Exception as error:
        print(f"AssertionError: {error}")
        return 1
    return 0


if __name__ == "__main__":
    exit(main())
