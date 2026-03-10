from series_validator import ArithmeticProgressionValidator


def run_case(series: list[int]) -> None:
    validator = ArithmeticProgressionValidator(series)

    print(f"Serie: {series}")
    if validator.is_arithmetic_progression():
        print("Es una progresión aritmética")
        print(f"Diferencia común: {validator.get_difference()}")
    else:
        print("No es una progresión aritmética")
    print()


if __name__ == "__main__":
    valid_series = [2, 4, 6, 8, 10]
    invalid_series = [3, 7, 10, 15]

    run_case(valid_series)
    run_case(invalid_series)
