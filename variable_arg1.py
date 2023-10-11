def Display(*values):
	for i in range(len(values)):
		print(values[i])
	
def main():
	Display(10,20,30,40,50,60)
	print("-----")
	Display(11,21,51)

if __name__ == "__main__":
	main()
