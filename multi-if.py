height=float(input("Enter your height:"))
if(height>=3):
    print("you can ride")
    age=(int(input("Enter your age")))
    bill=0
    if(age<12):
        print("the ticket prise is 150")
        bill=150
    elif(age<=18):
        print("the ticket prise is 200")
        bill=200
    else:
        print("the ticket prise is 500")
        bill=500

    want_photo=input("do you want a photo (yes/no):")
    if(want_photo == "yes"):
        bill=bill+50
    print(f"this is your {bill}")

else:
    print("you dont ride")
print("thank you ,enjoy the ride")