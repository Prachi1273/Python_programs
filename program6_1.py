class BookStore:
	NoofBks = 0
	
	def __init__(self,Bk_Name,poet):
		self.Name=Bk_Name
		self.Author=poet
		BookStore.NoofBks=BookStore.NoofBks+1
		
	def Display(self):
		print(self.Name ,"by",self.Author,".")
		print("No. of Books : ",BookStore.NoofBks)
		print()

def main():
	obj1=BookStore("Linux System Programming ","Robert Love")
	obj1.Display()
	
	obj2=BookStore("C Programming ","Dennis Ritchie")
	obj2.Display()

if __name__ == "__main__":
	main()
