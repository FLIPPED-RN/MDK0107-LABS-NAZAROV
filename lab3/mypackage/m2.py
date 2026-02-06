from random import uniform


def write_numbers(filename: str, n: int):
    numbers = [uniform(-100, 100) for _ in range(n)]
    with open(filename, "w") as file:
        file.write(" ".join(map(str, numbers)))


def min_max_sum(filename: str) -> float:
    with open(filename, "r") as file:
        numbers = list(map(float, file.read().split()))

    return min(numbers) + max(numbers)