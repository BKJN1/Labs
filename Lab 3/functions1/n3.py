def func(numh, numl):
    for chi in range(numh +1):
        rab = numh-chi
        if 2*chi + 4*rab == numl:
            return chi, rab

numh = 35
numl = 94
chi, rab = func(numh, numl)
print(f"Chickens: {chi}, Rabbits: {rab}")