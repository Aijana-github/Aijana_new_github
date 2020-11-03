def double_char(txt):
    empty = ''
    for letter in txt:
        empty = empty + (letter*2)
    return empty
print(double_char('String'))