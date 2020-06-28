import re

ref = {
    'I': 1,
    'V': 5,
    'X': 10,
    'L': 50,
    'C': 100,
    'D': 500,
    'M': 1000,
}

while True:
    roman = input('Enter a Roman Numeral: ')
    test = re.findall('[^' + ''.join(ref.keys()) + ']+', roman)                                                 
    lengthtracker = 0                                                                       
    for item in test:
        length = len(item)
        lengthtracker = lengthtracker + length                                              
        if length != 0:
            print('Roman Numerals may contain only the characters ' + ', '.join(ref.keys()))
            break
    if lengthtracker == 0:
        break                                                                            

print('Roman Numeral verified!')                                                            

n = len(roman)
m = 0
total = 0
negtotal = 0
tenttotal = 0
while m < n-1:
    if ref[roman[m]] == ref[roman[m+1]]:
        tenttotal += ref[roman[m]]
    elif ref[roman[m]] > ref[roman[m+1]]:
        total += tenttotal + ref[roman[m]]
        tenttotal = 0
    else:
        negtotal += tenttotal + ref[roman[m]]
        tenttotal = 0
    m += 1

total += tenttotal + ref[roman[m]] - negtotal
    

print('It equals:', total)
