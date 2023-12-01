import re

str_to_num = {"zero": 0, "one": 1, "two": 2, "three": 3, "four": 4, "five": 5, "six": 6, "seven": 7, "eight": 8, "nine": 9}


def main():
    count = 0
    with open("./coordinates.txt", "r") as file:
        lines = file.readlines()
    for line in lines:
        numbers = re.findall(r'(?=({"0|1|2|3|4|5|6|7|8|9|one|two|three|four|five|six|seven|eight|nine|zero"}))', line)
        print(line)
        print(numbers)
        number = change_number(numbers[0])
        if len(numbers) > 1:
            number = number * 10 + change_number(numbers[-1])
        else:
            number = number + number * 10
        print(number)
        count += number

    print(count)


def change_number(number):
    if number in str_to_num.keys():
        return str_to_num.get(number)
    return int(number)


if __name__ == "__main__":
    main()
