#!/usr/bin/env python3
import sys

def factorize(n):
    factors = []
    divisor = 2

    while n > 1:
        while n % divisor == 0:
            factors.append(divisor)
            n //= divisor
        divisor += 1

    return factors

def main():
    if len(sys.argv) != 2:
        print("Usage: factors <file>")
        sys.exit(1)

    input_file = sys.argv[1]

    try:
        with open(input_file, 'r') as file:
            lines = file.readlines()

        for line in lines:
            n = int(line.strip())
            factors = factorize(n)
            factorization = f"{n}={'*'.join(map(str, factors))}"
            print(factorization)

    except FileNotFoundError:
        print(f"File '{input_file}' not found.")
        sys.exit(1)

if __name__ == "__main__":
    main()
