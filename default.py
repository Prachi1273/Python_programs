def Display(name, age, marks=90):
	print("Name is : ",name)
	print("Age is : ",age)
	print("marks are : ",marks)

def main():
	Display("Prachi",19) #default
	print("---------------------")
	Display("Swati",59,78)
	print("---------------------")
	Display(age = 20,name = "sanika",marks = 88)

if __name__ == "__main__":
	main()
