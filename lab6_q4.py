
user_input = input("Enter a comma-separated string: ")


elements = user_input.split(", ")


letters_only = list(filter(lambda x: x.isalpha(), elements))
uppercase_letters = list(map(lambda x: x.upper(), letters_only))
print("Uppercase Letters:", uppercase_letters)

digits_only = list(filter(lambda x: x.isdigit(), elements))
squared_digits = list(map(lambda x: int(x) ** 2, digits_only))
print("Squared Digits:", squared_digits)


alphanumeric_strings = list(filter(lambda x: x.isalnum(), elements))
print("Alphanumeric Strings:", alphanumeric_strings)
