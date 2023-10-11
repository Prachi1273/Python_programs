def Area_rect(w,h):	
	area = w*h
	return area

def main():
	w = float(input("Enter Width of rectangle : "))
	h = float(input("Enter Height of rectangle : "))
	
	Area = Area_rect(w,h)
	
	print("Area of Rectangle : ",Area)
	
if __name__ == "__main__":
	main()
		
