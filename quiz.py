print("WELCOME TO MY QUIZ GAME!")

print("IT IS ALL ABOUT INDIA")

playing=input("do you want to play?")

if playing!="yes":
    quit()

print("Okay!Let's play :)")
score=0

answer=input("1. Who is known as the Father of the Nation? ")
if answer.lower() == "mahatma gandhi":
    print("Correct")
    score += 1
else:
    print("Wrong")
    
    print("Correct Answer is mahatma gandhi!")

print("Your score is:", score)

answer=input("2. What is the capital of India? ")
if answer.lower() == "new delhi":
    print("Correct")
    score += 1
else:
    print("Wrong")
    
    print("Correct Answer is New Delhi!")

print("Your score is:", score)

answer=input("3.Which festival is known as the Festival of Colors? ")
if answer.lower() == "holi":
    print("Correct")
    score += 1
else:
    print("Wrong")
    
    print("Correct Answer is Holi!")

print("Your score is:", score)

answer=input("4.Who was the first Prime Minister of India? ")
if answer.lower() == "jawaharlal nehru":
    print("Correct")
    score += 1
else:
    print("Wrong")
    
    print("Correct Answer is Jawaharlal Nehru!")

print("Your score is:", score)

answer=input("5.Which is the national animal of India?")
if answer.lower() == "tiger":
    print("Correct")
    score += 1
else:
    print("Wrong")
    
    print("Correct Answer is Tiger!")

print("Your score is:", score)

print(" Final Score:", score, "/5")