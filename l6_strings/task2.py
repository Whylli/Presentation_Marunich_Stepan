# Write a function that returns a substring of `s`
# which contains `max(len(s), n)` first characters.
#
# If n <= 0, return an empty string.
#
# For example,
# take("abcd", 3) -> "abc"
def take(s: str, n: int) -> str:
    t = ""
    if n <= 0:
        return ""
    if n >= len(s):
        return s
    else:
        for i in range(n):
            t = t + s[i]
        return t


# Do not change the below's code
if __name__ == "__main__":
    assert take("abcde", 2) == "ab"
    assert take("bbhj", 3) == "bbh"
    assert take("bjk", 0) == ""
    assert take("bjk", -1) == ""
    assert take("bjk", 100) == "bjk"
