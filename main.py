


def to_digits(num):
    """ example: to_digits(235) => [2, 3, 5] """
    digits = [int(x) for x in str(num)]
    return digits


def to_num(digit_array):
    """ example: to_num([3, 2, 1]) => 321 """
    num = 0
    for v in digit_array:
        num = (num * 10) + v
    return num


def to_base_10(num, num_base):
    """ example: to_base_10(1101, 2) = 13 """
    digits = to_digits(num)
    base10_num = 0
    for position, v in enumerate(reversed(digits)):
        power = position
        base10_num = base10_num + (num_base ** power) * v
    return base10_num


def to_base_n(num, new_base):
    """example: to_base_n(16, 8) = 20 """
    digits = []
    while num > 0:
        remainder = num % new_base
        num = int(num / new_base)
        digits.insert(0, remainder)
    return to_num(digits)


def split_num_sum(num):
    sum1 = 0
    while num > 0:
        sum1 = sum1 + (num % 10)
        num = int(num / 10)
    return sum1


def findDigitSum(num, base, start):

    # 1. Convert starting number into base b
    # 2. Make sequence of consecutive numbers starting with s and ending with s+n-1
    # 3. Convert the sequence above into base b and print it
    # 4. Split all the numbers in the sequence into digits
    # 5. Add up all the digits in the sequence and print it

    final_sum = 0
    s10 = to_base_10(start, base)
    print("Generated Numbers")
    for i in range(num):
        final_sequence = to_base_n(s10 + i, base)
        print(final_sequence)
        final_sum = final_sum + split_num_sum(final_sequence)
    print("_______")
    print("Sum of the generated numbers in base 10")
    print(final_sum)
    return final_sum


if __name__ == '__main__':
    is_s_valid = True
    b = int(input("Type in a base from 2-9 inclusive."))
    if 2 <= b <= 9:
        s = int(input("Type a number in this base that is less that 16 digits."))
    else:
        exit(f"Sorry, {b} is not from 2-9 inclusive.")
    for i in to_digits(s):
        if i >= b or len(str(s)) >= 16:
            is_s_valid = False
            break
    if is_s_valid:
        n = int(input("How many numbers do you want to be generated?"))
        findDigitSum(n, b, s)
    elif len(str(s)) >= 16:
        exit(f"{s} is more than 16 digits.")
    else:
        exit(f"{s} doesn't exist in this base.")


# person enters 123 for number
# person enters 4 for base
# robot says it works


# person enters 123 for number
# person enters 3 for base
# robot says it doesn't work
