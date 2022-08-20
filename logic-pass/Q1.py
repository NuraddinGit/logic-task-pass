# Q1/Write a method that will remove any given character from a String?

def RemoverFromStr(str, letter):
    s = str.lower()
    l = letter.lower()
    return s.lower().replace(l, '') if l in s else print('Charecter not in the string')


# Test
print(RemoverFromStr("hERElo thREr", "H"))
