#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    from calculator_1 import add, sub, mul, div
    length = len(sys.argv)
    if length != 4:
        print("Usage: {:s} <a> <operator> <b>".format(sys.argv[0]))
        exit(1)

    a = int(sys.argv[1])
    b = int(sys.argv[3])
    if sys.argv[2] == "+":
        print("{:d} + {:d} = {}".format(a, b, add(a, b)))
    elif sys.argv[2] == "-":
        print("{:d} - {:d} = {}".format(a, b, sub(a, b)))
    elif sys.argv[2] == "*":
        print("{:d} * {:d} = {}".format(a, b, mul(a, b)))
    elif sys.argv[2] == "/":
        print("{:d} / {:d} = {}".format(a, b, div(a, b)))
    else:
        print("Unknown operator. Available operators: +, -, * and /")
        exit(1)
