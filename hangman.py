import random
def hangman(n):
    print("welcome to")
    print("HANGMAN")
    l=len(n)
    print(l)
    s=random.randint(0,l-1)
    p=n[s]
    pl=len(p)
    list1=[]
    for i in range(pl):
        list1+=["_"]
    k=10
    for i in list1:
        print(i,end=" ")
    j=0
    while(k>0):
        print("(u have",k,"chances left)")
        a=str(input("enter your guess"))
        f=0
        for i in range(pl):
            if a==p[i]:
                f=1
                pos=i
                if list1[i]==a:
                    print("previous guess")
                    break
                else:
                    list1[i]=a
        if f==0:
            k-=1
            print("guess was incorrect")
        elif f==1:
            print("guess was correct")
        for i in list1:
            print(i,end=" ")
        
        if list(p)==list1:
            j=1
            print()
            print("congrats,u won!!!!!!!!!!!!!!!!",sep="")
            break
    if j==0:
        print()
        print("u lost, the correct answer was",p)
def choosesec():
    ch=1
    while(ch!=0):
        print("1.movies")
        print("2.people")
        print("3.animal")
        print("4.thing")
        ch=int(input("enter your choice 1/2/3/4"))
        if ch==1:
            n=["starwars","rango","killbill","ironman","joker","kingsman","superman","fastandfurious"]
            break
        elif ch==2:
            n=["doctor","musician","firefighter","policeman","janitor","painter","architect"]
            break
        elif ch==3:
            n=["lion","tiger","zebra","snake","peacock","eagle","rat","cat","dog","elephant"]
            break
        elif ch==4:
            n=["phone","table","chair"]
            break
    hangman(n)
choosesec()


            
    
    
    
