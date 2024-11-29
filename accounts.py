accounts={
    "ahmad":2000,
    "mohamed": 5000,
    "hana":1500,
    "tasnim":10000 }
def withdraw (amount, balance):
    if amount<=balance:
        print("processingg..")
        balance=balance-amount
        return balance
    else:
        print("invalid amount")

        
def balance_info():
    pass
def deposite(amount,balance):
    balance+=amount
    return balance
def transformation():
    
while True:
    account = input('we have 4 accounts, which account do you have?')
    for key, value in accounts.items():
        if key == account:
        balance = value
        procces=input ("""Choose which prossec do you need (w / d / bi/t)""")
        if procces == 'w':
            withdraw_ammount = int (input('how much money do you want ?'))
            new_balance = withdraw (withdraw_ammount, balance)
            accounts [account]=new_balance
            print (f" your balance become {new_balance}")
        
        elif procces=='deposit':
            dep_amount=int(input(" enter the deposite Ust"))
            new_balance deposite (dep_amourt, balancs)
            accounts [account]+= new balance
            print (f" your balance become thew_balance}")
        elif procces=='balance information':
            balance info (balance)
            else:
                trasn_acc=input("enter the account you want transfer money to ")
                trans_amount=int(input("how much money you want to transfer"))
                transformation
