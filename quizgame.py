print("welcome to my computer quiz!")

playing = input("Do you want to play?")

if playing.lower() != "yes":
    quit()
    

print("Okay! let's play: )")

score = 0

answer = input("What does CPU stand for? ")
if answer.lower() == "central processing unit":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")
    

answer = input("What does SaaS stand for? ")
if answer.lower() == "software as a service":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")
    

answer = input("What does IoTs stand for? ")
if answer.lower() == "internet of things":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")
    
    
answer = input("What does AI stand for? ")
if answer.lower() == "artificial intelligence":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")   
    

print("You got " + str(score) + " question correct")