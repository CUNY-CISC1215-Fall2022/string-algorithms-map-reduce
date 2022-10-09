# An iterative function for determining if a substring is contained
# within a larger string. It replicates the functionality
# of the "in" operator, which you should use instead - this is to
# demonstrate string algorithms and interacting with strings.
def is_in(string, substr):
    # This function works by using the range operator to take
    # substr-sized slices from the input string. For example,
    # with the input string "Hello, world" and substr "ello,",
    # i will equal each of the following in turn:
    #
    #   "Hello"
    #   "ello,"     <- substr matches here
    #   "llo, "
    #   "lo, w"
    #   "o, wo"
    #   ", wor"
    #   " worl"
    #   "world"
    #   "orld"
    #   "rld"
    #   "ld"
    #   "d"
    #
    # We can then compare each slice with substr. If
    # they match, we return True. If none of them match,
    # we eventually reach the end of the function and
    # return False.
    for i in range(len(string)):
        if string[i:i+len(substr)] == substr:
            return True
    return False


print(is_in("Hello, world", "ello,"))