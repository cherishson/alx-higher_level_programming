def remove_char_at(str, n):
    str3 = ''
    if n > len(str) or n < 0:
        return str
    for x in str:
        if x != str[n]:
            str3 += x
    return str3
