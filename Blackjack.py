from random import randint
number = randint (2, 21)
number2 = randint (1, 10)
number3 = randint (1, 10)
dealer1 = randint(1, 10)
dealer2 = randint(1, 10)

play = input ("Play?")
if (play == "yes"):
    print("You have:", number)
else:
    exit()

#dealer number (problem for later)
print("Dealer has:", dealer1)

choiceround1 = ""
#hit round 1
Continue = input ("Hit or Stand?")
if (Continue == "hit"):
    choiceround1 = "hit"
    print("You now have:", number2+number)
elif (Continue == "stand"):
    print(number)
#vvv printing after checking numbers and input vvv
    print ("Dealer now has:", dealer1+dealer2)
if number+number2 > 21:
    print("BUST!")
elif number+number2 == dealer1:
    print("Push (fuck you:))")
#stand function works but not for last round

#hit round 2
Continue = input("Hit?")
if (Continue == "yes"):
    print(number3+number2+number)
elif (Continue == "no"):
    print(number+number2)
else:
    print(number)
#vvv printing after checking numbers vvv 
print ("Dealer has:", dealer1+dealer2)

if number3+number2+number > 21:
    print ("BUST!")
if number+number2 <= 21:
    print ("Big money-man!")
    
#if (playertot > dealertot, playertot < 21):
#print ("Major money-bag!")
#elif (playertot < dealertot, playertot < 21):
#print ("Dealer wins (you suck)")
#elif (playertot < dealertot, playertot > 21):
#print ("BUST!")
    
#exit()
