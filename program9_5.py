def feet_meter(feet):
	return (feet*0.0929)

def main():
	feet = float(input("Enter Area in square feet : "))
	
	area = feet_meter(feet)
	
	print("Area in square meter : ",area)
	
if __name__ == "__main__":
	main()
		
