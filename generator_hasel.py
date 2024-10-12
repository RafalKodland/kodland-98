import random

def gen_pass(pass_lenght):
    znaki = "+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
    haslo = ""

    for i in range(pass_lenght):
        haslo += random.choice(znaki)

    return haslo
