class bank:
    def __init__(self,acc_num,hold_name,bal,task):
        self.acc_num=acc_num
        self.hold_name=hold_name
        self.bal=bal
        self.task=task

    def balance(self):
        return self.bal

    def deposit(self,amount):
        self.bal=self.bal+amount
        return self.bal

    def withdrawl(self,amount):
        if(self.bal>amount):
            self.bal = self.bal-amount
            return self.bal


acc_num = int(input("Enter Account Number: "))
hold_name = input("Enter Holder Name: ")
bal = int(input("Enter Initial Balance: "))
print("\n1.Deposit amount\n2.Withdrawl Amount\n3.Check Balance\n4.Exit")
task=input("Enter what do you want to do?")

b1 = bank(acc_num,hold_name,bal,task)

if(task=='1'):
    amount=int(input("Enter the amount to deposit: "))
    print(b1.deposit(amount))
elif(task=='2'):
    amount=int(input("Enter the amount to withdrawl: "))
    print(b1.withdrawl(amount))
elif(task=='3'):
    print(b1.balance())
elif(task=='4'):
    print("Exited!")
else:
    print("Pls enter the valid number!")


