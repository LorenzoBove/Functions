def permutation_control(string1,string2):
    while string1 :
        if string2[0] in string1:
            string1 = string1[:string1.index(string2[0])]+string1[string1.index(string2[0])+1:]
            string2=string2[1:]
            print('string1:',string1,'string2:',string2)
        else:
            return False

    return True


string1='mario'
string2='omrai'
print('CASE 1, small string permutation:')
print('1:',string1,' 2:',string2)
print(permutation_control(string1,string2))
print('-------------------------------\n')
string1='eert873287'
string2='et828r37e7'
print('CASE 2, long string permutation together with \'e\',\'7\' and \'8\' repetitions:')
print('1:',string1,' 2:',string2)
print(permutation_control(string1,string2))
print('-------------------------------\n')
string1='efderyueffcrinu32489'
string2='ffdufin4e89eceu32ryr'
print('CASE 3, very long string permutation with several bytes repetition:')
print('1:',string1,' 2:',string2)
print(permutation_control(string1,string2))
print('-------------------------------\n')
string1='aaqa'
string2='daaa'
print('CASE 4, short string non permutations:')
print('1:',string1,' 2:',string2)
print(permutation_control(string1,string2))
print('-------------------------------\n')
string1='aa2aff4wff4w'
string2='2a1aff4wff4w'
print('CASE 5, long string non permutation:')
print('1:',string1,' 2:',string2)
print(permutation_control(string1,string2))

