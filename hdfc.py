class hdfc:
	ROI = 9.5 	#class variable
	
	def __init__(self,Name,Amount):
		self.Balance = Amount	#instance variable
		self.AccountHolder = Name	#instance variable
		print("Welcome  ",self.AccountHolder)
		print("Amount gets successfully created with initial balance : ",self.Balance)
		
	def DisplayB(self):	#instance method
		print("Hello ",self.AccountHolder)
		print("Your account balance is : ",self.Balance)
	
	@classmethod
	def DisplayBankInfo(cls):	#classmethod
		print("Welcome to Hdfc bank portal")
		print("Our bank is PVT LMT bank")
		print("We provide Rate of Interest on saving account is : ",cls.ROI)
		
	@staticmethod
	def DisplayKYCInfo():
		print("Acoording to the rules of RBI you should provide below documents for KYC ")
		print("Your Adhar card ")
		print("Your PAN card")
		print("Your Passport size photo")
		
	def Withdraw(self,Amount):	#instancemethod
		if self.Balance < Amount:
			print("There is no sufficient balance")
		else:
			self.Balance = self.Balance - Amount
			print("Amount withdrawl successfully")
			
	def Deposit(self,Amount):	#instancemethod
		self.Balance = self.Balance + Amount
		print("Amount deposited successfully...")

def main():
	print("ROI of hdfc bank is : ",hdfc.ROI)
	
	hdfc.DisplayBankInfo()
	print("---------------------------------------------------------------------------")

	hdfc.DisplayKYCInfo()
	print("---------------------------------------------------------------------------")

	print("creating new account...")
	Prachi = hdfc("Prachi",5000)     #__init__(100,"Prachi",5000)
	print("---------------------------------------------------------------------------")

	print("creating new account...")
	Barve = hdfc("Barve",3000)	##__init__(200,"Barve",3000)
	print("---------------------------------------------------------------------------")

	Prachi.Deposit(2000)
	Prachi.DisplayB()
	print("---------------------------------------------------------------------------")

	Prachi.Withdraw(1000)
	Prachi.DisplayB()
	print("---------------------------------------------------------------------------")
	
	Barve.Deposit(4000)
	Barve.DisplayB()
	print("---------------------------------------------------------------------------")
	
	Barve.Withdraw(500)
	Barve.DisplayB()
	

if __name__ == "__main__":
	main()
