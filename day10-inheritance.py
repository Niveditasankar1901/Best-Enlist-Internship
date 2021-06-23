# Day 10
# Create a real time scenario for inheritance 
# Banking concept

class customer_details:
    def cus(self ,first_name,second_name,acc_no,address):
        self.first_name=first_name
        self.second_name=second_name
        self.acc_no=acc_no
        self.address=address

class amount:
    def amt(self,amount_taken):
        self.amount_taken=amount_taken
        
    def money(self,amount_credited):
        self.amount_credited=amount_credited
        
class account_details:
    def type(self,acc_type,balance):
        self.acc_type=acc_type
        self.balance=balance
        
        
class display(customer_details, account_details,amount):
    def dis(self):
        print("Name           : ",self.first_name,"", self.second_name)
        print("Account Number : ",self.acc_no)
        print("Address        : ",self.address)
        print("Account Type   : ",self.acc_type)
        print("Balance        : ",self.balance-self.amount_taken+self.amount_credited)

amount_taken=float(input("Enter the amount taken : "))    
amount_credited=float(input("Enter the amount deposited : "))
ob=display()
ob.cus("Nivedita","Sankar",12345674567,"xyz,abcd,nm.")
ob.type("Savings",50000.00)
ob.amt(amount_taken)
ob.money(amount_credited)
ob.dis()

#Output :-
#Enter the amount taken : 20000
#Enter the amount deposited : 10000
#Name           :  Nivedita  Sankar
#Account Number :  12345674567
#Address        :  xyz,abcd,nm.
#Account Type   :  Savings
#Balance        :  40000.0



