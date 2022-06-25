def disemvowel():
    s = input()
    #s = string_
    str_new=""
    alpha = 'aoeuiAOEUI'
    for i in range(len(s)):
        check = 0
        for g in range(len(alpha)):
            if s[i] == alpha[g]:
                check = 1
                break
        if check == 0:
            str_new += s[i]
    print(str_new, '')

disemvowel()