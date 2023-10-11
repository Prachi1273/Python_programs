def Area_circle(r):
	pi = 3.14	
	area = pi*r*r
	return area

def main():
	r = float(input("Enter Radius : "))
	
	Area = Area_circle(r)
	
	print("Area of circle : ",Area)
	
if __name__ == "__main__":
	main()
		
