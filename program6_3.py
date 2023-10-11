class BankAcc:
	ROI = 10.5
	
	def __init__(self,Name,Amount):
		self.Name_acc=Name
		self.balance=Amount

		
	def Display(self):
		print("Name of Account : ",self.Name_acc)
		print("Available Balance : ",self.balance)
		print()
		
	def Deposit(self,Rs):
		self.balance=self.balance+Rs
		print("Depositiong....",Rs)
	
	def Withdraw(self,Rs):
		self.balance=self.balance-Rs
		print("withdrawing....",Rs)
	
	def Interest(self):
		interest=self.balance*(BankAcc.ROI/100)
		print("Interest : ",interest)

def main():
	obj1=BankAcc("Prachi Barve",5000)
	obj1.Display()
	obj1.Withdraw(1000)
	obj1.Display()
	obj1.Interest()
	obj1.Display()
	obj2=BankAcc("Anand Barve ",10000)
	obj2.Display()
	obj2.Deposit(2000)
	obj2.Display()
	obj2.Interest()
	obj2.Display()

if __name__ == "__main__":
	main()
