# Maile Arellano

def encode(numbers):
    result = ''
    for i in numbers:
        encode_digit = int(i) + 3
        result += str(encode_digit)
    return result

'''
jill's code
'''
def decode(password):
    result = ''
    for i in password:
        decoded_digit = int(i) - 3
        result += str(decoded_digit)
    return result

    pass


def menu():
    print("Menu")
    print("-------------")
    print("1. Encode")
    print("2. Decode")
    print("3. Quit")
    pass


def main():
    while True:
        menu()

        option = int(input("Please enter an option: "))
        if option == 1:
            numbers = input("Please enter your password to decode: ")
            print("Your password has been encoded and stored!")
            result = encode(numbers)
            pass
        elif option == 2:
            decoded_password = decode(result)
            print(f"The encoded password is {result}, and the original password is {decoded_password}.")
            pass
        elif option == 3:
            break


if __name__ == "__main__":
    main()
