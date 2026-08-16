from typing import Callable

def convert_dec(number: str, base: int) -> int:
    """Convert binary or hexadecimal number to decimal."""

    if base == 0:
        return int(number, 2)

    if base == 1:
        return int(number, 16)

    raise ValueError("Invalid base.")

def calculate(expression: str, base: int) -> int:
    """Calculate a simple addition or subtraction."""

    parts = expression.upper().split()

    if len(parts) == 1:
        return convert_dec(parts[0], base)

    if len(parts) != 3:
        raise ValueError("Invalid expression.")

    a, operator, b = parts

    a = convert_dec(a, base)
    b = convert_dec(b, base)

    operations: dict[str, Callable[[int, int], int]] = {
        "+": lambda x, y: x + y,
        "-": lambda x, y: x - y,
    }

    if operator not in operations:
        raise ValueError("Invalid operator.")

    return operations[operator](a, b)

def main() -> None:
    while True:
        option = input(
            "[-1 To exit]\n"
            "Type: 0 - Binary, 1 - Hexadecimal, 2 - Finite Field\n"
            "? "
        )

        if option == "-1":
            break

        if option not in {"0", "1", "2"}:
            print("Invalid option")
            continue

        try:
            expression = input("Operation: ")

            if option == "2":
                print("Finite Field not implemented yet.")
                continue

            result = calculate(expression, int(option))
            print(result)

        except ValueError as error:
            print(f"Error: {error}")

if __name__ == "__main__":
    main()
