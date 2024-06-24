
##Simple program

print("hello world")
print(12*3)
print(15.7+15) 
a="XYZ"
print(a) 

##Comments,Escape sequences

#please write some input here
print("\"hello anuj\"")
print("I m okay \'how are you?\'")
print("kaise ho app?\nand you also")

##Type casting

    #Explicit
a="34"
b="87"
print(int(a) + int(b))

    #Implicit
a="23"
b=23.5
print(int(a) + b)

##Index

a="qwertyuiop"
print(a[4])
print(a[4:8])
print(len(a))
print(a[-4:-2])
print(a.find("yui"))

##Case

a="ASqwe rtDF DFGyu"
print(a.upper())
print(a.lower())
print(a.islower())
print(a.isupper())
print(a.swapcase())
print(a.capitalize())

##Other

a="harry"
print(a.replace("harry","john"))
a="harry is the man "
print(a.split(" "))
print(a.isspace())
a="asdfg001"
print(a.isalnum())
print(a.isalpha())

##if else conditional statement

##   1

a=int(input("enter the number"))
b=int(input("enter the number"))

if a<10:
    if b<15:
        print(b,"b is less than 15")
    elif b>30:
        print(b,"b is greater than 30")
    else:
        print("b is out of range")
elif a>10:
    print(a,"greater than 10")
elif a==10:
    print(a,"equal to 10")
else:
    print(a,"invalid number")

##   2

a=float(input("enter the first number"))
b=float(input("enter the second number"))
c=input("enter the operator")

if c == '+':
    print(a+b)
elif c == '*':
    print(a*b)
elif c == "/":
    print(a/b)
elif c == "-":
    print(a-b)
elif c == "//":
    print(a//b)
elif c == "**":
    print(a**b)
elif c == "%":
    print(a%b)    
else:
    print("operator is not valid")    

##Match case statement
    
##    1

a=int(input("enter the number"))
b=int(input("enter the number"))
c=input("enter the operator")

match c:
    case '+':
        print(a+b)
    case '-':
        print(a-b)
    case '*':
        print(a*b)
    case '/':
        print(a/b)
    case '%':
        print(a%b)
    case '**':
        print(a**b)
    case '//':
        print(a//b)
    case _:
        print("operator is wrong")
        
##    2

a=int(input("enter the number"))
b=int(input("enter the number"))

match a:
    case _ if a>10:
        print("a>10")
    case _ if a<10:
        print("a<10")
    case _ if a==10:
        print("a=10")
    case _:
        print("match a is invalid")
match b:
    case _ if b>10:
        print("b>10")
    case _ if b<10:
        print("b<10")
    case _ if b==10:
        print("b=10")
    case _:
        print("match b is invalid")        

##For loop

##     1
        
a=["Red","Blue","green","Yellow"]
for i in a:
    print(a)
    for b in a:
        print(b)
        for c in b:
            print(c)

##     2
 
for i in range(0,11,3):
    print(i)

for i in range(0,11,3):
    print(i+1)

##     3
    
a=int(input("enter the first number"))
b=int(input("enter the second number"))
c=input("enter the operator")

for i in a,b:
    if c == '+':
        print(a+b)
        break
    elif c == '-':
        print(a-b)
        break
    elif c == '*':
        print(a*b)
        break
    elif c == '/':
        print(a/b)
        break
    elif c == '**':
        print(a**b)
        break
    elif c == '//':
        print(a//b)
        break
    elif c == '%':
        print(a%b)
        break
    else:
        print("sorry")    

##While loop

##    1

a=0
while(a<3):
    print(a)
    a=a+1

##    2
    
a=int(input("enter the number"))
b=int(input("enter the number"))
c=input("enter the operator")
d=0
while(d==0):
    if c == "+":
        print(a+b)
        break
    elif c == "-":
        print(a-b)
        break
    elif c == "*":
        print(a*b)
        break
    elif c == "/":
        print(a/b)
        break
    elif c == "**":
        print(a**b)
        break
    elif c == "//":
        print(a//b)
        break
    elif c == "%":
        print(a%b)
        break
    else:
        print("sorry")    

##Break statement in for loop

for i in range(0,15):
    if (i == 11):
        break
    print("5 x ",i,"=",5*i)

##break statement in while loop
    
a=0
while(a<15):
    if (a == 11):
        break
    print("5 x ",a,"=",5*a)
    a=a+1

##Continue statement in for loop

for i in range(0,13):
    if (i == 11):
        print("11th is absence")
        continue
    print("5 x ",i,"=",5*i)

##continue statement in while loop

a=0
while(a<16):
    if (a==14):
        print("over")
        a=a+1
        continue
    print("5 x ",a," = ",5*a)
    a=a+1

##Function

def table(a,b):
    for i in range(a,b):
        for g in range(1,11):
            print(i," x ",g,"=",i*g)

   
a=1
b=5
table(a,b)


##list

l=[2,3,4,"Harry","Hello"]
print(l)
print(l[2])#index to item
print(l.index("Harry"))#item to index
print(l[0:4:2])
l.append(5)
print(l)
print(len(l))


          ##Check whether an item is present in the list

l=[2,3,4,5,6,"Harry","Hello"]
if 3 in l:
    print("yes")
else:
    print("no")

          ##Change list to tuple

lis=[2,3,4,6,7]
lis2=tuple(lis)
print(lis2)

          ##List comprehension

l=[i for i in range(2,10)]
print(l)
l1=[i*i for i in range(2,20)]
print(l1)
l2=[i*i for i in range(2,30) if i%2==0]
print(l2)
l3=[2,3,4,5,6,7,8,9,10]
l4=[i for i in l3 if i<6]
print(l4)

##tuple

t=(2,3,4,5,"Harry","Hello")
print(t)
print(t[3])#index to item
print(t.index("Harry"))#item to index
print(t[1:6:2])
print(len(t))

            ##Check whether an item is present in the list

t=(2,3,4,5,6,"Harry","Hello")
if 3 in t:
    print("yes")
else:
    print("no")

            ##Change tuple to list

tup=[2,3,4,6,7]
tup2=list(tup)
print(tup2)

            ##No list comprehension in tuple


##F-String

s="My name is {} and I m {}"
a="xyz"
b="abc"
print(s.format(a,b))

    #OR

s="My name is {a} and I m {b:.2f}"
print(s.format(a="xyz",b=432.76235))

    #OR

a="xyz"
b="abc"
print(f"My name is {a} and I m {b}")

    #OR

a="xyz"
b="abc"
print(f"My name is {{a}} and I m {b}")

##Doc-string

def square(n):
    '''Takes in a number n, returns the
square of n'''
    print(n**2)
square(5)
print(square.__doc__)

##Def Function

def calculate(a,b):
    mean=(a*b)/(a+b)
    print(mean)
def greater(a,b):
    if b>a:
        print("yes")
    elif a>b:
        print("no")
    else:
        print("sorry")
def power(a,b=3):
    p=a**b
    print(p)
def square(b):
    print(b**2)
def aveg(a,b,c):
    print((a+b+c)/3)


a=5
b=2
c=4
calculate(a,b)
greater(a,b)
power(a,b)
square(b)
aveg(a,b,c)


def avg(*numbers):
    sum=0
    for i in numbers:
        sum=sum+i
    print(sum/len(numbers))       

avg(5,6,7)
        ##OR
def avg(*numbers):
    sum=0
    for i in numbers:
        sum=sum+i
    return(sum/len(numbers))       

a=avg(5,6,7)
print(a)