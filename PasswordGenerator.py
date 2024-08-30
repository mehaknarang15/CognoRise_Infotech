import random
print('Password Generator')
length = int(input('Enter length of password needed'))
Alpha = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
L_Alpha = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'i', 'j', 'k', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
Numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
Symbols = ['!', '@', '#', '$', '%', '&', '*', '/']
upper = random.choice(Alpha)
lower = random.choice(L_Alpha)
num = random.choice(Numbers)
sym = random.choice(Symbols)
Combined = Alpha + L_Alpha + Numbers + Symbols
Temp = upper + lower + num + sym
for i in range(length-4):
    Temp = Temp + random.choice(Combined)
password = Temp
print('password', '=', password)





