import json
import random 
import string
from pathlib import Path
class Bank:
    __database="data.json"
    data=[]
    try:
        if Path(__database).exists():
            with open(__database) as fs:
                data=json.loads(fs.read())
    except Exception as err:
        print(f"error occured as {err}")
    
    @classmethod
    def Generate_acc(cls):
        alpha=random.choices(string.ascii_letters,k=4)
        digit=random.choices(string.digits,k=8)
        id=alpha+digit
        random.shuffle(id)
        return "".join(id)
    @classmethod
    def update_data(cls):
        with open(cls.__database,'w') as fs:
            json.dump(cls.data,fs)

    def createuser(self):
        info={
            "name":input("enter your name : "),
            "email":input("enter your email : "),
            "age":int(input("enter your age : ")),
            "phonenumber":input("enter your phone number : "),
            "pin":input("enter your pin : "),
            "account" :Bank.Generate_acc(),
            "balance":0
        }
    
        if info["age"]<18:    
            print("your account cannot be created underage")

        elif(len(info["phonenumber"])!=10 or len(info["pin"])!=4):
            print("invalid input please try again")

        else:
            print(f"please keep your account number safe, your account number is {info['account']}")
            Bank.data.append(info)
            Bank.update_data()

    def deposit_money(self):
        ac=input("Enter your account number : ")
        pin=input("enter your pin : ")
        userdata=[i for i in Bank.data if i["account"]==ac and i["pin"]==pin]
        # for i in Bank.data:
        #     if i["account"]==ac and i["pin"]==pin:
        #         userdata=i
        #         break
        if not userdata:
            print("No data found for this user ")
        else:
            amount=int(input("Enter your amount : "))
            if amount<500:
                print("Amount is less than 500")
            elif amount>10000:
                print("amount is greater than 10000")
            else:
                userdata[0]["balance"]+=amount
                Bank.update_data()
                print("balance updated")

    def withdrawl_money(self):
        ac=input("Enter your account number : ")
        pin=input("enter your pin : ")
        userdata=[i for i in Bank.data if i["account"]==ac and i["pin"]==pin]
        if not userdata:
            print("No data found for this user ")
        else:
            amount=int(input("Enter your amount : "))
            if amount<500:
                print("Amount is less than 500")
            elif amount>10000:
                print("amount is greater than 10000")
            else:
                if userdata[0]["balance"]<amount:
                    print("Insufficient amount")
                else:
                    userdata[0]["balance"]-=amount
                    Bank.update_data()
                    print("money withdrawl,balance updated")

    def details(self):
        ac=input("Enter your account number : ")
        pin=input("enter your pin : ")
        userdata=[i for i in Bank.data if i["account"]==ac and i["pin"]==pin]
        if not userdata:
            print("No data found for this user ")
        else: 
            for i in userdata[0]:
                print(f"{i} -> {userdata[0][i]}")

    def update_user(self):
        ac=input("Enter your account number : ")
        pin=input("enter your pin : ")
        userdata=[i for i in Bank.data if i["account"]==ac and i["pin"]==pin]
        if not userdata:
            print("No data found for this user ")
        else: 
            print("you can not change your account number")
            print("now update your details and skip it if you don't want to change")
            newdata={
                "name":input("enter your name : "),
                "age":input("enter your age : "),
                "email":input("enter your email : "),
                "phonenumber":input("enter your number : "),
                "pin":input("enter your pin : ")
            }
            if newdata["name"]=="":
                newdata["name"]=userdata[0]["name"]
            if newdata["age"]=="":
                newdata["age"]=userdata[0]["age"]
            if newdata["email"]=="":
                newdata["email"]=userdata[0]["email"]
            if newdata["phonenumber"]=="":
                newdata["phonenumber"]=userdata[0]["phonenumber"]
            if newdata["pin"]=="":
                newdata["pin"]=userdata[0]["pin"]
            newdata["account"]=userdata[0]["account"]
            newdata["balance"]=userdata[0]["balance"]

            for i in userdata[0]:
                if userdata[0][i]==newdata[i]:
                    continue
                else:
                    if newdata[i].isnumeric():
                        userdata[0][i]=int(newdata[i])
                    else:
                        userdata[0][i]=newdata[i]

        Bank.update_data()
        print("Details updated successfully!!")

    def delete_user(self):
        ac=input("Enter your account number : ")
        pin=input("enter your pin : ")
        userdata=[i for i in Bank.data if i["account"]==ac and i["pin"]==pin]
        if not userdata:
            print("No data found for this user ")
        else: 
            Bank.data.remove(userdata[0])
            Bank.update_data()
            print("account deleted !!")

bank=Bank()
check=int(input("""
press 1 for creating a new user account
press 2 for depositing money
press 3 for withdrawl money
press 4 for your details
press 5 to update your details
press 6 to delete user
enter your response
"""))

if check==1:
    bank.createuser()

if check==2:
    bank.deposit_money()

if check==3:
    bank.withdrawl_money()

if check==4:
    bank.details()

if check==5:
    bank.update_user()

if check==6:
    bank.delete_user()

