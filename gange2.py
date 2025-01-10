tall = [x for x in range(11)]
svar = [x*x for x in range(11)]

#for i in range(len(tall)):
#    print(f"Kvadratet av {tall[i]} er {svar[i]}.")
    
for t, s in zip(tall,svar):
    print(f"Kvadratet av {t} er {s}.")
    
