#Task
# You get an array of numbers, return the sum of all of the positives ones.
def positive_sum(arr):
    total=0
      
    for num in arr:
        if num > 0 :
            total +=  num 
    return total

#Complete the square sum function so that it squares each number passed into it and then sums the results together.
def square_sum(numbers):
    total = 0
    for num in numbers:
        total += num ** 2
    return total


# Return the number (count) of vowels in the given string.

# We will consider a, e, i, o, u as vowels for this Kata (but not y).

# The input string will only consist of lower case letters and/or spaces.
def get_count(sentence):
    count = 0
    for letter in sentence:
        if letter in "aeiou":
            count += 1 
    return  count 

#Check to see if a string has the same amount of 'x's and 'o's. The method must return a boolean and be case insensitive. The string can contain any char.
def xo(s):
    x_count = 0 
    o_count = 0 

    for letter in s:
        if letter == "x" or letter == "X":
            x_count += 1
        elif letter == "o" or letter == "O":
            o_count += 1

    return x_count == o_count