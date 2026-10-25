#Q1)

correct_pin="1234"
balance=10000
attempt=0
run=True
l=[]
while attempt<3 and run:
    user_pin=input("Enter the pin :")
    if user_pin!=correct_pin and attempt==0:
        print("Invalid Pin")
        print("Left attempt: 2")
    if user_pin!=correct_pin and attempt==1:
        print("Invalid Pin")
        print("Left attempt: 1")
    if user_pin!=correct_pin and attempt>1:
        print("Card blocked")
    attempt+=1       
    if user_pin==correct_pin:
        while True:
            print("Check Balance")
            print("Deposite")
            print("Withdraw")
            print("Exit")
            choice=int(input("Enter your choice :"))
            if choice==1:
                print("Your current balance is",balance)
            elif choice==2:
                dep=int(input("Enter money for deposite :"))
                print("New Balance is",balance+dep)
                balance=balance+dep
                l.append(dep)
            elif choice==3:
                wit=int(input("Enter money to withdraw :"))
                if wit<balance:
                    print("Remaining Balance is",balance-wit)
                    l.append(wit)
                else:
                    print("Insufficient balance")
                    balance=balance-wit
            elif choice==4:
                print("Exit")
                run=False
                break
            else:
                print("Invalid  choice")
else:
    print("deposite :",dep)
    print("withdraw :",wit)
    print("Thank You")



#Q2)
    
student={"aman":[85,90,78],"riya":[92,88,95],"zoya":[70,65,80]}
for name in student:
    marks=student[name]
    total=0
    for mark in marks:
        total=total+mark
    avg=total/3
    print(name,round(avg,2),"\n")
for name in student:
    marks=student[name]
    total=0
    for mark in marks:
        total=total+mark
        avg=total/3
        if avg>=85:
            grade="A"
        elif avg>=70:
            grade="B"
        elif avg>=50:
            grade="C"
        else:
            grade="F"
    print(name,round(avg,2),grade)
while True:
    print("\n1. Add student")
    print("2. View all")
    print("3. Show topper")
    print("4. Exit")
    choice=int(input("Enter your choice :"))
    if choice==1:
        name=input("Enter student name :")
        if name in student:
            print("Student already exists.")
        else:
            marks=[]
            i=1
            while i<=3:
                mark=int(input("Enter mark :"))
                if mark>=0 and mark<=100:
                    marks.append(mark)
                    i=i+1
                else:
                    print("Invalid mark, try again.")
                student[name]=marks
    elif choice==2:
        print(student)
    elif choice==3:
        topper=" "
        highest=-1
        for name in student:
            total=0
            for mark in student[name]:
                total=total+mark
            avg=total/3
            if avg>highest:
                highest=avg
                topper=name
        print("Topper :",topper)
    elif choice==4:
        print("Good Bye!")
        break
    else:
        print("Invalid choice.")

# github upload practice




































































                   
