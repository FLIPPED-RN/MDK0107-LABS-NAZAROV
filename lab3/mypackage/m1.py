def run(randomNumbers):
    with open("wassap.txt", "w") as file:
        file.write(" ".join(map(str, randomNumbers)))
    print("успешно записано :)")

def count_pars_words():
    with open("wassap.txt", "r") as file:
        numbers = list(map(int, file.read().split()))

    s = set(numbers)
    count = 0

    for x in s:
        if x > 0 and -x in s:
            count += 1

    print("количество пар противоположных чисел:", count)