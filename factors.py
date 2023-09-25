import sys

def factorize(n):
    for p in range(2, n // 2 + 1):
        if n % p == 0:
            q = n // p
            return f"{n}={p}*{q}"
    return f"{n}=1*{n}"

if len(sys.argv) != 2:
    print("Usage: python factors.py <file>")
    sys.exit(1)

input_file = sys.argv[1]

try:
    with open(input_file, 'r') as file:
        for line in file:
            n = int(line.strip())
            result = factorize(n)
            print(result)

except FileNotFoundError:
    print(f"File '{input_file}' not found.")
    sys.exit(1)
except ValueError:
    print("Invalid input. Please provide a file with valid natural numbers greater than 1.")
    sys.exit(1)
