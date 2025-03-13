
print("******************")
print("Welcome to ATM !")
print("******************")
accounts={
    1000:["jyothi","28-08-2003",10000,1234],
    1001:["meena","14-5-2000",20000,5678],
    1002:["tejasri","28-7-2001",30000,None]
    }
dobm = {1:"Jan",2:"Feb",3:"Mar",4:"apr",5:"May",6:"June",7:"July",8:"Aug",9:"Sep",10:"Oct",11:"Nov",12:"Dec"}
while True:
    print("Choose Your Option")
    print("1.Withdrawl")
    print("2.Deposit")
    print("3.Pin Generation")
    print("4.Mini statement")
    print("5.Exit")
    option = int(input("Enter Your option: "))
    print()
    if option == 1:
        print("*********************")
        accno= int(input("Enter Account Number: "))
        if accno not in accounts:
            print("Account Does not Exit !")
        else:
             pin=int(input("Enter Pin: "))
             if accounts[accno][-1] == None:
                 print("Generate pin")
             else:
                 if accounts[accno][-1] != pin:
                     print("Invalid Pin")
                 else:
                    amt=int(input("Enter Amount to Withdraw: "))
                    if amt > accounts[accno][-2]:
                        print("Insufficient Funds ")
                    else:
                         print("Withdraw Successful !")
                         accounts[accno][-2] -= amt
             print(accounts[accno])
        print("*********************")
    elif option ==2:
        print("***********************")
        accno=int(input("Enter Account Number: "))
        if accno not in accounts:
            print("Account does not exit")
        else: 
            amt=int(input("Enter Account to depasit: "))
            accounts[accono][-2] += amt
            print("DepositebSuccesfull")
            print(accounts[accono])
        print("******************")
    elif option ==3:
        print("********************")
        account=int(input("Enter Account Number: "))
        if accono not in accounts:
            print("Account Does not Exists")
        else:
            if accounts[accono][-1] == None:
                pin=int(input("Enter Pin: "))
                cpin=int(input("confirm pin: "))
                if pin != cpin:
                    print("Pin Does not Match")
                else:
                    accounts[accno][-1] = pin
                    print("pin generated Sucessfully")
            else:
                print("Pin already Exit")
            print(accounts[accno])
        print("************************")
    elif option ==4:
        print("**********************")
        accono = int(input("Enter Account Name: "))
        if accno not in accounts:
            print("Account Does not Exits")
        else:
            pin = int(input("Enter Pin:"))
            if pin != accounts[accno][-1]:
                print("Invalid pin")
            else:
                print(f"Name: (accounts[accno][0]")
                print(f"Account number: [accono]")
                dob = accounts[accno][1].split("-")

                
                date = dob[0]
                month = dobm[int(dob[1])]
                year = dod[2]
                dob = date + "-" + month + "=" + year
                print(f"Date of Birth: (dob)")
                print(f"Account Balance: (accounts[accno][-2]")
                
        print("*******************")  
                
    elif option == 2:
        print("Deposit")
    elif option == 3:
        print("Pin Generator")
    elif option == 4:
        print("Mini statement")
    else:
         break
     
