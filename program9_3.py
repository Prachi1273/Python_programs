def Convert_Dist(km):
	dist = km*1000
	return dist

def main():
	km= float(input("Enter distance in KM : "))
	
	dist = Convert_Dist(km)
	
	print("Distance in Meter : ",dist)
	
if __name__ == "__main__":
	main()
		
