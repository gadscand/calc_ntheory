"""Operations over the finite field GF(2^8)."""

from __future__ import annotations

FIELD_SIZE = 256
IRREDUCIBLE_POLYNOMIAL = 0x11D

def _validate_element(value: int) -> None:
    """Raise ValueError if value is not an element of GF(256)."""
    if not 0 <= value < FIELD_SIZE:
        raise ValueError(
            f"Invalid field element: {value}. "
            f"Expected a value between 0 and {FIELD_SIZE - 1}."
        )

def add(a: int, b: int) -> int:
    """Add two elements of GF(256)."""
    _validate_element(a)
    _validate_element(b)

    # Addition in GF(2^8) is XOR.
    return a ^ b

def subtract(a: int, b: int) -> int:
    """Subtract two elements of GF(256)."""
    # In characteristic 2, subtraction is the same as addition.
    return add(a, b)

def multiply(a: int, b: int) -> int:
    """Multiply two elements of GF(256)."""
    _validate_element(a)
    _validate_element(b)

    result = 0

    while b:
        if b & 1:
            result ^= a

        b >>= 1
        a <<= 1

        if a & FIELD_SIZE:
            a ^= IRREDUCIBLE_POLYNOMIAL

    return result & 0xFF

def inverse(a: int) -> int:
    """Return the multiplicative inverse of an element of GF(256)."""
    _validate_element(a)

    if a == 0:
        raise ValueError("Zero has no inverse in GF(256)")

    result = 1
    base = a
    exponent = 254
    
    while exponent:
        if exponent & 1:
            result = multiply(result, base)
        base = multiply(base, base)
        exponent >>= 1

    return result

def divide(a: int, b: int) -> int:
    """Divide two element on GF(256)"""
    _validate_element(a)
    _validate_element(b)

    if b == 0:
        raise ValueError("Division by zero is not defined")

    return multiply(a, inverse(b))

def calculate(a: int, operator: str, b: int) -> int:
    """Calculate an operation between two GF(256) elements."""
    operations = {
        "+": add,
        "-": subtract,
        "*": multiply,
        "/": divide,
    }

    try:
        operation = operations[operator]
    except KeyError:
        raise ValueError(f"Invalid operator: {operator!r}") from None

    return operation(a, b)
