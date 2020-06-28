import re

bad = 1                                                                                     

while bad == 1:
    roman = input('Enter a Roman Numeral: ')
    test = re.findall('[^IVXLCDM]+', roman)                                                 
    lengthtracker = 0                                                                       
    for item in test:
        length = len(item)
        lengthtracker = lengthtracker + length                                              
        if length != 0:
            print('Roman Numerals may contain only the characters I, V, X, L, C, D, M')
            break
        else:
            continue
    if lengthtracker == 0:
        bad = 0                                                                             

print('Roman Numeral verified!')                                                            

ref = dict()                                                                                
ref['I'] = 1
ref['V'] = 5
ref['X'] = 10
ref['L'] = 50
ref['C'] = 100
ref['D'] = 500
ref['M'] = 1000

n = len(roman)
m = 0
total = 0
negtotal = 0
tenttotal = 0
while m < n-1:
    if ref[roman[m]] == ref[roman[m+1]]:
        tenttotal = tenttotal + ref[roman[m]]
    elif ref[roman[m]] > ref[roman[m+1]]:
        total = total + tenttotal + ref[roman[m]]
        tenttotal = 0
    else:
        negtotal = negtotal + tenttotal + ref[roman[m]]
        tenttotal = 0
    m = m + 1

total = total + tenttotal + ref[roman[m]] - negtotal
    

print('It equals:', total)
