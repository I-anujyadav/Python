ques=[" ","what is your name?\n1)Harry\n2)Anuj\n3)Ram\n4)Shyam","how old are you?\n1)19\n2)20\n3)18\n4)17","where do you live?\n1)J&K\n2)Gujarat\n3)Haryana\n4)UP"]
a=int(input("enter the question number"))

if a==1:
    print(ques[1])
    opts=["harry","Anuj","Ram","Shyam"]
    c=int(input(" "))
    if c==2:
        print("Answer- ",opts[1],"\nGood your answer is right\ncongratulation  You won 100 rupees")
    elif c==1:
        print("Wrong answer")    
    elif c==3:
        print("wrong answer")
    else:
        print("Wrong answer")
elif a==2:
    print(ques[2])
    opts=["19","20","18","17"]
    c=int(input(" "))
    if c==2:
        print("Answer- ",opts[1],"\nGood your answer is right\ncongratulation  You won 100 rupees")
    elif c==1:
        print("Wrong answer")    
    elif c==3:
        print("wrong answer")
    else:
        print("Wrong answer")
elif a==3:
    print(ques[3])
    opts=["J&K","Gujarat","Haryana","UP"]
    c=int(input(" "))
    if c==4:
        print("Answer- ",opts[1],"\nGood your answer is right\ncongratulation  You won 100 rupees")
    elif c==2:
        print("Wrong answer")    
    elif c==3:
        print("wrong answer")
    else:
        print("Wrong answer")        
        
else:
    print("not available")