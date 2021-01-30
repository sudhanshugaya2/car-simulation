print("Menu")
print("Press 1 to start the car")
print("Press 2 to stop the car")
print("Press 3 to shift gears of the car")
print("Press 4 to apply brakes of the car")
print("Press 5 to quit the app")
indicator = False #reference for the car position
counter = 0
while(True):
    choice = int(input("Enter your choice"))
    if choice==1:
        if indicator==False:
            print("started")
            indicator=True
        else:
            print("Already started")
    elif choice==2:
        if indicator==True:
            print("Stop")
            indicator=False
        else:
            print("Already stopped")
    elif choice==3:
        if indicator==True and counter<=3:
            print("Shifted to gear ",counter)
            if counter==3:
                print("Maximum shift achived")
            counter=counter+1

        else:
            print("Start the car")
    elif choice==4:
        if indicator == True:
            print("Brakes applied")
            indicator=False
        else:
            print("Start the car")
    elif choice==5:
        print("Thankyou")
        break
    else:
        print("Incorrect response")