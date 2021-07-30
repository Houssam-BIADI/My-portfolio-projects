class Category:
    def __init__(self,z):
        self.name=z
        self.ledger=list()

    def deposit(self,amount,desc=""):
       self.dep=dict()
       self.dep["amount"]=amount
       self.dep["description"]=desc
       self.ledger.append(self.dep)

    def check_funds(self,amount):
        fund = 0
        n = len(self.ledger)
        for i in range(n):
            fund = fund + self.ledger[i]["amount"]
        if fund < amount:
            return False
        else:
            return True

    def withdraw(self, amount, description=""):
        # checking if total amount less than or greaten than amount to be withdrawn
        l = self.check_funds(amount)

    def get_balance(self):
        fund = 0
        n = len(self.ledger)
        for i in range(n):
            fund = fund + self.ledger[i]["amount"]

    def transfer(self, amount, obname):
        objectname = obname.name
        a = self.withdraw(amount, f"Transfer to {objectname}")
        b = obname.deposit(amount, f"Transfer from {self.name}")
        if (a == True):
            return True
        else:
            return False

    def __str__(self):
        title = f"{self.name:*^30}\n"
        items = ""
        total = 0
        for i in range(len(self.ledger)):
            items += f"{self.ledger[i]['description'][0:23]:23}{self.ledger[i]['amount']:>7.2f}\n"
            total += self.ledger[i]['amount']

        output = title + items + "Total: " + str(total)
        return output

