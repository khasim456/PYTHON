#random module

'''import random
a=random.sample(range(10,40),10)
print(a)'''

#randint()
'''import random
a=random.randint(30,50)
print(a)'''

#choice()
'''import random
a=[10,20,30,40,50]
b=random.choice(a)
print(b)'''

while True:
    import random
    n=int(input("enter the roll of dice:"))
    
    a=[1,2,3,4,5,6]
    b=random.choice(a)
    print("random choice",b)
    c=int(input("number:"))
    if c==1:
        print("Yes")
    elif c==2:
        print("No")
        exit()
    
    
