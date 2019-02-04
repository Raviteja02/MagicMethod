class Account:
     def __init__(self,acbal,cname,cacno,cadd):
         self.acbal=acbal
         self.cname=cname
         self.cacno=cacno
         self.cadd=cadd
         print("your ac is successfully created.")
         print("Name",self.cname)
         print("Account NO",self.cacno)
         print("Address",self.cadd)
         print("Ac Bal",self.acbal)

     def deposit(self,damt):
         self.acbal=self.acbal+damt
         print("your updated ac bal is",self.acbal)

     def withdrawl(self,wamt):
         if self.acbal<wamt:
             print("insufficient funds")
         else:
             self.acbal=self.acbal-wamt
             print("your updated ac bal is",
                   self.acbal)

     def getbalance(self):
         print(self.acbal)

class savingsaccount(Account):
     interestrate=7.0

     def __init__(self,acbal,acno):
         Account.acbal=acbal
         self.intrestearned = Account.acbal*savingsaccount.interestrate
         print(self.intrestearned)



class checkingaccount(Account):
    feecharge=3.0

    def __init(self,acbal,cname,cacno,cadd):
        Account.acbal=acbal
        Account.acno=acno
        Account.cname=cname
        Account.cadd=cadd

    def deposit(self,damt):
        Account.acbal=(Account.acbal+damt)-checkingaccount.feecharge
        print(Account.acbal)

    def withdrawl(self,wamt):
        if Account.acbal < wamt:
            print("insufficient funds")
        else:
            Account.acbal=Account.acbal-wamt-checkingaccount.feecharge
            print(Account.acbal)


class currentaccount(Account):
    mol=50000

    def __init__(self,acbal,acno):
        Account.acbal=acbal
        Account.acno=acno


    def withdrawl(self,wamt):
        if Account.acbal ==0 :
            if self.wamt<currentaccount.mol:
                Account.acbal=Account.acbal-self.wamt
        print(Account.acbal)


c1=Account(10000.00,'ravi',1001,'raja')



jaggu=Account(20000.00,'jagadeesh',1004,'Tirupathi')


jaggu.deposit(100000.00)

jaggu.withdrawl(20000.00)


c2=Account(241222.00,'sjk',1005,'hyderabad')

c2.deposit(500000.00)
c2.withdrawl(900000000000000.00)



