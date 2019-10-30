#!/usr/bin/env python3

def calculate(arg):
    stack = list()
    for token in arg.split():
        print(token)

def main():
    while True:
        calculate(input('rpn calc> '))


if __name__ == '__main__':
    main()
