def Convert_temp(far):
	temp = ((far-32)*(5/9))
	return temp

def main():
	far = float(input("Enter Temperature in Farhenheit : "))
	
	temp = Convert_temp(far)
	
	print("Temperature in celsius : ",temp)
	
if __name__ == "__main__":
	main()
		
