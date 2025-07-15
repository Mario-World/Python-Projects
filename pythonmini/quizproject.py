print("Never Give up") # Two projects -python and react project-todo.

playing = input("Do you want to play? ")


if playing.lower() != "yes":
    quit()

print("okay let's play :) ")
score = 0 

answer = input("What does CPU stand for? ")

if answer.lower() == "central processing unit": 

   print("Correct")
   score += 1
else:
      print("Wrong") 
      
answer = input("what does GPU stands for? ")

if answer.lower() == "graphical processing unit":
   print("Correct")
   score += 1

else: 
     print("Wrong")
answer = input("what stands for RAM? ")
if answer.lower() == "random access memory":  
    print("Correct")
    score += 1
else: 
    print("Wrong")
answer = input("What does PSU stand for? ")
if answer.lower() == "power supply":
  print("Correct!")
  score += 1
else: 
    print("Wrong")
    
print("You got " +  str(score) + " questions correct!")
print("You got " + str((score / 4) * 100 ) + "%.")
