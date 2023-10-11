	
def chkvwl(ch):
	if(ch=='a' or ch=='e' or ch=='i' or ch=='o' or ch=='u' or ch=='A' or ch=='E' or ch=='I' or ch=='O' or ch=='U'):
		return True	
	
def main():
	print("Enter one character : ")
	ch = input()
	
	ret = chkvwl(ch)
	if(ret==True):
		print("Vowel")
		print()
	else:
		print("NOT vowel")
		print()
	
if __name__ == "__main__":
	main()
