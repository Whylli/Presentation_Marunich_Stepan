# Use `for` loop to check if character `c` is present in
# string `s`.
#
# Return `True` is character is present. Return `False` otherwise
def has_char(s: str, c: str) -> bool:
    n = s.count(c)
    if n == 1:
        i = True
    else:
        i = False
    return i



# Do not change the below's code
if __name__ == "__main__":
    assert has_char("lfhyt", "f") == True
    assert has_char("abbaabba", "c") == False
