# This file defines a function for detecting palindromes
# recursively, then uses the map/filter/reduce pattern to
# determine how many nontrivial words (3+ characters) in
# words.txt are palindromes.



# Part 1: Palindrome detection
#-------------------------------------------------------------
# This function determines if a word is a palindrome
# using a recursive approach. Here is how it works:
#
# A word is a palindrome if both of the following things
# are true:
#
#   1. word[0] equals word[-1]
#      (i.e., the first and last characters are equal)
#   2. word[1:-1] is a palindrome.
#      (i.e., the word minus its first and last character
#      is a palindrome)
#
# We also declare that a one-character string and an empty
# string is a palindrome by default. This is sufficient to
# arrange a base case and recursive case.
def is_palindrome(word):
    # Base case 1: Empty words and one-character words are
    # always palindromes
    if len(word) == 0 or len(word) == 1:
        return True
    # Base case 2: If the first and last character in word are
    # not equal, it cannot be a palindrome
    if word[0] != word[-1]:
        return False

    # Recursive case: Is word[1:-1] a palindrome?
    return is_palindrome(word[1:-1])

# Part 1: Map/filter/reduce for palindrome counting
#-------------------------------------------------------------
# Open the words.txt file for reading.
# Per request, this demonstrates accessing files in different
# directories relative to the map_reduce_string_algorithms.py
# script. You can also pass in an absolute path to any file in
# your system, though the details of this depend on whether you
# use Mac, Windows, or Linux.
infile = open('data/words.txt')

# Mapping operation 1: Remove newline character from words in
# the file
words = []
for word in infile:
    words.append(word.strip())

# Filter step: remove words with fewer than 2 characters
words_long = []
for word in words:
    if len(word) > 2:
        words_long.append(word)

# Mapping operation 3: Find palindromes
palindrome = []
for w in words_long:
    palindrome.append(is_palindrome(w))

# Reduce operation: Count how many of the words were palindromes,
# and sum it into a total.
total = 0
for p in palindrome:
    if p:
        total = total + 1


print("Total palindromes in words.txt: " + str(total))







# infile = open('words.txt')

# for line in infile:
#     print(line.strip())
