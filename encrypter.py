import random
import os
import getpass
import pyminizip
plataforma = input("Enter which platform your password is for: ")
lenghtpass = int(input("Enter the length of your password: "))
passw = getpass.getpass("Enter encryption key for your password file: ")
endpassword = []
characters = ['Q', 'W', 'E', 'R', 'T', 'Y', 'U', 'I', 'O', 'P', 'A', 'S', 'D', 'F', 'G', 'H', 'J', 'K', 'L', 'Z', 'X', 'C', 'V', 'B', 'N', 'M', 'W', 'E', 'R', 'T', 'Y', 'U', 'I', 'p',
       'a', 's', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'z', 'x', 'c', 'v', 'b', 'n', 'm']
numbers = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
especialcharacters = ['@', '#', '$', '%', '^', '&', '*', '(', ')', '-']
i = 0
while i < lenghtpass:
   endpassword.append(random.choice(characters))
   endpassword.append(random.choice(numbers))
   endpassword.append(random.choice(especialcharacters))
   i += 1
plat = plataforma + '.txt'
file = open(plat, "w")
file.write("".join(endpassword) + os.linesep)
file.close()
inpt = "./" + plat
pre = None
plats = plataforma  + '.zip'
oupt = "./" + plats
password = passw
com_lvl = 5
pyminizip.compress(inpt, None, oupt, 
                   password, com_lvl) 
os.remove(plat)












