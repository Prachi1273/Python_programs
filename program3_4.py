		
def Accept():
	print("Enter one character : ")
	ch = input()
	
	def Caps_Small(ch):
		if(ch>='A' and ch<='Z'):
			ch = chr(ord(ch)+32)
			print(ch)
		elif(ch>='a' and ch<='z'):
			ch = chr(ord(ch)-32)
			print(ch)
	
	return Caps_Small(ch)

def main():
	Accept()

if __name__ == "__main__":
	main()
