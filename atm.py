atm_card=input("insert atm card")
if atm_card=="Right side" or atm_card=="right side":
    language=input("enter language")
    if language=="english" or language=="hindi":
        pin=int(input("enter pin"))
        if pin>=1000 and pin<=9999:
            transaction_type=input("enter transaction type")
            if transaction_type=="withdrawl" or transaction_type=="Withdrawl":
                amount=int(input("enter amount"))
                key_name=input("enter key name")
                if amount>=500 and amount<=2000 and amount%500==0:
                    a=amount//2000
                    b=amount%2000
                    c=amount//500
                    d=amount%500
                    print("notes of 2000",a,"notes of 500",c)
                    money_receipt=input("enter money receipt")
                    if money_receipt=="yes" or money_receipt=="no":
                        print("money receipted")
                    else:
                        print("thanks for money transaction")
                else:
                    print("limited amount")
            elif transaction_type=="balance enquiry" or transaction_type=="Balance enquiry":
                account_type=input("enter account type")
                key_name=input("enter key")
                if key_name=="ok" or key_name=="OK":
                    print("thanks for enquiry")
                else:
                    print("invalid key")
            elif transaction_type=="Deposite money" or transaction_type=="deposite money":
                account_no=int(input("enter account no"))
                if account_no>=1000000000 and account_no<=9999999999:
                    bill_atm=int(input("enter bill atm"))
                    if bill_atm>=1000000000 and bill_atm<=9999999999:
                        amount=int(input("enter amount"))
                        key_name=input("enter ok")
                        if key_name=="ok" or key_name=="OK":
                            print("succesfull")
                        else:
                            print("unsuccesfull")
            elif transaction_type=="Bill_payment" or transaction_type=="bill_payment":
                account_no=int(input("enter account no"))
                if account_no>=1000000000 or account_no<=9999999999:
                    bill_id=int(input("enter bill id"))
                    if bill_id>=1000000000 or bill_id<=9999999999:
                        amount=int(input("enter amount"))
                        key_name=input("enter ok")
                        print("succesful")
                    else:
                        print("unsuccesful")
            else:
                print("not succesful")
        else:
            print("invalid pin")
    else:
        print("enter valid language")
else:
    print("rejected")
                    
                



