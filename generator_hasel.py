import random

znaki = "+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
dlugosc = int(input("Jaka ma być długość hasła: "))
haslo = ""

for i in range(dlugosc):
    haslo += random.choice(znaki)

print("Twoje hasło to:", haslo)