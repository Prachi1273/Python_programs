
# function accept more parameter and return nothing 
def Exellent(name,age,city):
	print("Inside Exellent function")
	print("Welcome : ",name)
	print("your age is : ",age)
	print("your city is : ",city)
	
def main():
	Exellent("Prachi",19,"Pune")
	Exellent(city = "Nashik",age = 20,name = "Barve")	
	
if __name__ == "__main__":
	main()
