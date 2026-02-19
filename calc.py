#!/usr/bin/env python3
import sys

def usage():
    print("Usage: python3 calc.py <add|sub|mul|div> <a> <b>")
    print("Example: python3 calc.py add 2 3")
    sys.exit(1)

def main():
    if len(sys.argv) == 2 and sys.argv[1] in ("-h", "--help"):
        usage()
    if len(sys.argv) != 4:
        usage()


    op = sys.argv[1]
    try:
        a = float(sys.argv[2])
        b = float(sys.argv[3])
    except ValueError:
        print("Error: a and b must be numbers.")
        usage()

    if op == "add":
        result = a + b
    elif op == "sub":
        result = a - b
    elif op == "mul":
        result = a * b
    elif op == "div":
        if b == 0:
            print("Error: division by zero.")
            sys.exit(1)
        result = a / b
    else:
        print(f"Error: unknown operation '{op}'")
        usage()

    # Print without trailing .0 if it's an integer-like float
    if result.is_integer():
        print(int(result))
    else:
        print(result)

if __name__ == "__main__":
    main()

