from ntpath import join
import random
import os
import pyminizip
import getpass
print("Introduce para que plataforma es tu contraseña")
plataforma = input()
print("Introduce clave de encriptacion para tu archivo de contraseñas ")
passw = getpass.getpass("Contraseña: ")
nis = ['Q','W','E','R','T','Y','U','I','O','P','A','S','D','F','G','H','J','K','L','Z','X','C','V','B','N','M','W','E','R','T','Y','U','I','p','a','s','d','f','g','h','j','k','l','z','x','c','v','b','n','m','1','2','3','4','5','6','7','8','9''@','#','$','%','^','&','*','(',')','-']
num = 1
ctep1 = random.choice(nis)
ctep2 = random.choice(nis)
ctep3 = random.choice(nis)
ctep4 = random.choice(nis)
ctep5 = random.choice(nis)
ctep6 = random.choice(nis)
ctep7 = random.choice(nis)
ctep8 = random.choice(nis)
ctep9 = random.choice(nis)
ctep10 = random.choice(nis)
ctep11 = random.choice(nis)
ctep12 = random.choice(nis)
ctep13 = random.choice(nis)
ctep14 = random.choice(nis)
ctep15 = random.choice(nis)
ctep16 = random.choice(nis)
ctep17 = random.choice(nis)
ctep18 = random.choice(nis)
contener = [ctep1,ctep2,ctep3,ctep4,ctep6,ctep7,ctep8,ctep9,ctep10,ctep11,ctep12,ctep13,ctep14,ctep15,ctep16,ctep17,ctep18]
plat = plataforma  + '.txt'
file = open(plat, "w")
file.write( "".join(contener)+ os.linesep)
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













