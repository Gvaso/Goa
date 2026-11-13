# Your task is to create a function that does four basic mathematical operations.

# The function should take three arguments - operation(string/char), value1(number), value2(number).
# The function should return result of numbers after applying the chosen operation.
def basic_op(operator, value1, value2):
    if operator == '+':
        return value1 + value2
    elif operator == '-':
        return value1 - value2
    elif operator == '*':
        return value1 * value2
    elif operator == '/':
        return value1 / value2

#Write a function to convert a name into initials. This kata strictly takes two words with one space in between them.

# The output should be two capital letters with a dot separating them.
def abbrev_name(name):
    first, last = name.split()
    return f"{first[0].upper()}.{last[0].upper()}"

# Timmy & Sarah think they are in love, but around where they live, they will only know once they pick a flower each. If one of the flowers has an even number of petals and the other has an odd number of petals it means they are in love.

# Write a function that will take the number of petals of each flower and return true if they are in love and false if they aren't.

def lovefunc(flower1, flower2):
    return (flower1 % 2) != (flower2 % 2)