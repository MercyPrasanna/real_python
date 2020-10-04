print("demonstrate main function")
# Main function has __name__ = main when called as a script
# When imported as a module __name__ is the script name
# The best practice is to use an entry main script


def concat_string(str1, str2):
    """Concatenates two input strings."""
    return str1+str2


def main():
    str1 = input("Enter string 1")
    str2 = input("Enter string 2")
    print(concat_string(str1, str2))


if __name__ == "__main__":
    main()
