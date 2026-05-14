"""
Zeroth: AI — Episode 2 Exercises
How Computers Actually Work

The big idea: Every computer runs on binary (0s and 1s) and logic gates.
AI isn't running on magic hardware — it's the same transistors, same gates,
same fetch-decode-execute cycle. Just a LOT of them.

These exercises let you see binary, logic gates, and ASCII in action.
"""

# ─── Exercise 1: Binary Converter ────────────────────────────────────────
#
# Decimal (base 10) uses digits 0-9. Binary (base 2) uses only 0 and 1.
# Every number you know has a binary equivalent.

print("=== Exercise 1: Binary Converter ===")
print()


def to_binary(n):
    """Convert a decimal number to its binary representation."""
    if n == 0:
        return "0"
    bits = []
    while n > 0:
        bits.append(str(n % 2))
        n = n // 2
    return "".join(reversed(bits))


numbers = [0, 1, 2, 5, 10, 42, 255]
for n in numbers:
    binary = to_binary(n)
    print(f"  {n:>3} decimal = {binary:>8} binary  ({len(binary)} bits)")

print()
print("Notice: 255 = 11111111 (eight 1s). That's the max value for 1 byte.")
print("A byte = 8 bits = 256 possible values (0 to 255).")
print()


# ─── Exercise 2: Bits and Bytes ──────────────────────────────────────────
#
# 1 bit = 2 states (0 or 1)
# 2 bits = 4 states (00, 01, 10, 11)
# 8 bits = 256 states
# Every time you add a bit, you DOUBLE the possibilities.

print("=== Exercise 2: How Bits Scale ===")
print()
print(f"{'Bits':<6} {'Combinations':<15} {'Example use'}")
print("-" * 50)

uses = {
    1: "On/off switch",
    2: "Direction (N/S/E/W)",
    4: "Single hex digit (0-F)",
    8: "One ASCII character",
    16: "Unicode character",
    24: "One pixel color (RGB)",
    32: "IPv4 address",
    64: "Modern integer",
}

for bits in [1, 2, 4, 8, 16, 24, 32, 64]:
    combos = 2**bits
    use = uses.get(bits, "")
    print(f"  {bits:<4} {combos:<15,} {use}")

print()
print("Every time you add 1 bit, you double the number of possibilities.")
print("That's exponential growth. 64 bits = 18 quintillion combinations.")
print()


# ─── Exercise 3: Logic Gates ────────────────────────────────────────────
#
# A logic gate takes binary inputs and produces one binary output.
# NOT: flips the input (1 becomes 0, 0 becomes 1)
# AND: output is 1 only if BOTH inputs are 1
# OR: output is 1 if EITHER input is 1


def NOT(a):
    return 1 if a == 0 else 0


def AND(a, b):
    return 1 if (a == 1 and b == 1) else 0


def OR(a, b):
    return 1 if (a == 1 or b == 1) else 0


print("=== Exercise 3: Logic Gates ===")
print()

print("NOT gate (flips the input):")
for a in [0, 1]:
    print(f"  NOT({a}) = {NOT(a)}")

print()
print("AND gate (both must be 1):")
for a in [0, 1]:
    for b in [0, 1]:
        print(f"  AND({a}, {b}) = {AND(a, b)}")

print()
print("OR gate (either one is enough):")
for a in [0, 1]:
    for b in [0, 1]:
        print(f"  OR({a}, {b}) = {OR(a, b)}")

print()
print("That's it. These three operations, chained together billions of")
print("times per second, produce everything a computer does.")
print()


# ─── Exercise 4: Building an Adder from Gates ───────────────────────────
#
# You can ADD numbers using only AND, OR, and NOT.
# A half-adder adds two single bits and produces a sum and a carry.


def XOR(a, b):
    """XOR = OR but not AND. Equivalent to: OR(AND(NOT(a),b), AND(a,NOT(b)))"""
    return OR(AND(NOT(a), b), AND(a, NOT(b)))


def half_adder(a, b):
    """Add two bits. Returns (sum, carry)."""
    s = XOR(a, b)
    carry = AND(a, b)
    return s, carry


print("=== Exercise 4: Half-Adder (Addition from Logic Gates) ===")
print()
print("Adding two single-bit numbers using only AND, OR, NOT:")
print()
print(f"{'A':<4} {'B':<4} {'Sum':<6} {'Carry':<6} {'Meaning'}")
print("-" * 40)
for a in [0, 1]:
    for b in [0, 1]:
        s, c = half_adder(a, b)
        decimal = f"{a} + {b} = {c}{s} (binary) = {a + b} (decimal)"
        print(f"{a:<4} {b:<4} {s:<6} {c:<6} {decimal}")

print()
print("0 + 0 = 0. 0 + 1 = 1. 1 + 0 = 1. 1 + 1 = 10 (that's 2 in binary).")
print("Chain these together and you can add any numbers. That's how CPUs do math.")
print()


# ─── Exercise 5: ASCII — Letters as Numbers ─────────────────────────────
#
# ASCII maps numbers to characters. A = 65 = 01000001 in binary.
# Every character on your keyboard has a number.

print("=== Exercise 5: ASCII — Letters Are Numbers ===")
print()

message = "AI"
print(f'The word "{message}" in binary:')
print()
for char in message:
    code = ord(char)
    binary = to_binary(code).zfill(8)
    print(f"  '{char}' = {code:>3} decimal = {binary} binary")

print()
print("Your turn — try any word:")
print()
for word in ["Hello", "Zeroth", "01"]:
    codes = " ".join(f"{ord(c):>3}" for c in word)
    print(f'  "{word}" = [{codes}]')

print()
print("Everything is numbers. Text, images, audio, video — all binary.")
print("The computer doesn't know what any of it means. It just moves bits around.")
