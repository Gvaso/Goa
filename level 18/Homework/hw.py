# Nathan loves cycling.

# Because Nathan knows it is important to stay hydrated, he drinks 0.5 litres of water per hour of cycling.

# You get given the time in hours and you need to return the number of litres Nathan will drink, rounded down.
def litres(time):
    return int(time * 0.5)

# Given a random non-negative number, you have to return the digits of this number within an array in reverse order.
def digitize(n):
    result = []
    for x in str(n)[::-1]:
        result.append(int(x))
    return result

# Welcome. In this kata, you are asked to square every digit of a number and concatenate them.

# For example, if we run 9119 through the function, 811181 will come out, because 92 is 81 and 12 is 1. (81-1-1-81)

# Example #2: An input of 765 will/should return 493625 because 72 is 49, 62 is 36, and 52 is 25. (49-36-25)

# Note: The function accepts a non-negative integer and returns an integer.

def square_digits(num):
    result = ""
    for x in str(num):
        result += str(int(x) ** 2)
    return int(result)

# Trolls are attacking your comment section!

# A common way to deal with this situation is to remove all of the vowels from the trolls' comments, neutralizing the threat.

# Your task is to write a function that takes a string and return a new string with all vowels removed.

# For example, the string "This website is for losers LOL!" would become "Ths wbst s fr lsrs LL!".

# Note: for this kata y isn't considered a vowel.
def disemvowel(string_):
    result = ""
    for x in string_:
        if x not in "aeiouAEIOU":
            result += x
    return result
