
A=['''
 +---+
 |   |
 O   |
/|\  |
/ \  |
     |
=========''', '''
 +---+
 |   |
 O   |
/|\  |
/    |
     |
=========''', '''
 +---+
 |   |
 O   |
/|\  |
     |
     |
=========''', '''
 +---+
 |   |
 O   |
/|   |
     |
     |
=========''', '''
 +---+
 |   |
 O   |
 |   |
     |
     |
=========''', '''
 +---+
 |   |
 O   |
     |
     |
     |
=========''', '''
 +---+
 |   |
     |
     |
     |
     |
=========''']
q=len(A)
a=[]
ss=0
hhh={"ankit","shubhash","vishal","pawan","nasir"}
for i in hhh:
    b=i
    break
print(b)
e=" "*len(b)
c=[]
for  i in range(len(b)):
    a.append(b[i])
    c.append(e[i])
while True:
    x=1
    y=q+1
    e=0
    while y>0:
        d=0
        while True:
            guess=input("guess the charactor\n")
            if guess in c:
                if x== len(A)+1:
                    break
                if ss==1:
                    print(A[-x])
                    x+=1
                else:
                    ss+=1
                    print("already have this")
                    continue
            d=0
            for i in range(len(a)):
                if guess in a:
                    if a[i]==guess:   
                        c[i]=a[i]
                        d+=1
                    if a==c:
                        pass
                if a==c:
                    pass
            if guess not in a:
                print(A[-x])
                y-=1
                x+=1
                if x== len(A)+1:
                    break
            print(*c)   
            if a==c:
                break
        if c==a:
            print("you won")
            print(*c)
            break
        else:
            print("you are lose")
            print(x)
            break
    s=input(" Do you want to play ?     yes/no")
    if s=="yes" :
        print("thanks")
        c="0"
    else:
        print("bye")
        break    

    
 