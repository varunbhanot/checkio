def checkio(data):
    len_flag = len(data)>=10
    len_digt = len(''.join(x for x in data if x.isdigit())) > 0
    len_lower = len(''.join(x for x in data if x.isalpha() and x.islower())) > 0
    len_upper = len(''.join(x for x in data if x.isalpha() and x.isupper())) > 0

    return len_flag and len_digt and len_lower and len_upper

#Some hints
#Just check all conditions


if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert checkio('ULFFunH8ni') == True, "1st example"
    assert checkio('bAse730onE4') == True, "2nd example"
    assert checkio('asasasasasasasaas') == False, "3rd example"
    assert checkio('QWERTYqwerty') == False, "4th example"
    assert checkio('123456123456') == False, "5th example"
    assert checkio('QwErTy911poqqqq') == True, "6th example"
    print("Coding complete? Click 'Check' to review your tests and earn cool rewards!")
