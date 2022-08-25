#!/usr/bin/python3
if __name__ == "__main__":
    import sys
def main():
    arg = len(sys.arg) - 1
    if arg == 0:
        print("0 arguments.")
    elif arg == 1:
        print("1 arguments.")
        print("1: {}".format(sys.argv[1]))
    else:
        print("{:d} arguments:".format(argc))
        for i in range(1, argc + 1):
            print("{}:{}".format(i, sys.argv[i]))
    main()
