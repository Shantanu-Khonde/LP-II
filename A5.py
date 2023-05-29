print("Welcome,please enter your name..!")
Name=input()
print("Welcome,"+Name+"..!")
print("------------------------------------")
print(" I am chathub,I wil be assiting you for customer services")
print(" ")
print("what service do you want?")
print("1. Mobile Services")
print("2. Model buying guide")
print(" ")
print("Enter option number from following")
A=int(input())
if A==1:
    print("you have choosen Mobile services")
    print(" ")
    print("please enter model no. from below list ")
    print("1. Phone(1)")
    print("2. Phone(2)")
    print(" ")
    p=int(input())
    if p==1:
        print("you have choosen Phone(1)")
    print(" ")
    print("please choose service ")
    print("1. Callback from Expert")
    print("2. Chat with Expert")
    print("3. Book an Appointment")
    s=int(input())
    if s==1:
        print("our Expert will call you soon")
    elif s==2 :
        print("our expert will chat with you soon")
    elif s==3 :
        print("please Enter your Locality name")
        l=input()
        if l==" " :
            print("locality can't be empty,plase enter locality")
        else :
         print("our Representative in"+" " +l+" "+"will confirm your appointent for phone(1)")
        p=int(input())
    else :
        p==2
        print("you have choosen Phone(2)")
    print(" ")
    print("please choose service ")
    print("1. Callback from Expert")
    print("2. Chat with Expert")
    print("3. Book an Appointment")
    s=int(input())
    if s==1:
        print("our Expert will call you soon")
    elif s==2 :
        print("our expert will chat with you soon")
    elif s==3 :
        print("please Enter your Locality name")
        l=input()
        if l==" " :
            print("locality can't be empty,plase enter locality")
        else:
         print("our Representative in"+" " +l+" "+"will confirm your appointent for phone(2)")



