#!/usr/bin/python3

if __name__ == "__main__":

    import sys
    from decimal import Decimal

    args = sys.argv[1:]
    addition = sum(Decimal(arg) for arg in args)
    print("{}".format(addition))
