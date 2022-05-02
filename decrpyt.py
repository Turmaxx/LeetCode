def decrpytionSwapPairwise(s):
    s = list(s)
    for i in range(0, len(s)-1, 2):
        if s[i].isupper() and s[i+1].islower():
            s[i], s[i+1] = s[i+1], s[i]

    return ''.join(s)

def decrpytionDigits(s):
    i = 0
    digit_string = ""

    while i < len(s):
        if s[i].isdigit() and s[i] != '0':
            digit_string += s[i]
        i += 1

    s = list(s)
    for i in range(len(s)):
        if s[i] == '0':
            s[i] = digit_string[-1]
            digit_string = digit_string.replace(digit_string[-1],"")
        
    for i in range(len(s)):
        if s[i].isdigit() and s[i+1].isalpha():
            s = s[i+1:]
            break

    return "".join(s)


def decryptPassword(s):
    new_string = s.replace('*','')
    new_string = decrpytionSwapPairwise(new_string)
    new_string = decrpytionDigits(new_string)
    

    return new_string

print(decryptPassword("43Ah*ck0rr0nk"))