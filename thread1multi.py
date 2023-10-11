import os
import threading

def task1(value):
	print("PID of task1 is :", os.getpid())
	print("threadid of main thread is : ",threading.get_ident())
	
def task2(value):
	print("PID of task2 is :",os.getpid())
	print("threadid of main thread is : ",threading.get_ident())

def main():
	print("PID of parent process is :",os.getpid())
	print("threadid of main thread is : ",threading.get_ident())
	no = 5
	t1 = threading.Thread(target = task1, args = (no,))
	t2 = threading.Thread(target = task2, args = (no,))
	
	t1.start()
	t2.start()
	
	t1.join()
	t2.join()

if __name__ == "__main__":
	main()
