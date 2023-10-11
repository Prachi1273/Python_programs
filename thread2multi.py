import os
import threading

def task1(value):
	print("PID of task1 is :", os.getpid())
	print("threadid of main thread is : ",threading.current_thread())
	
def task2(value):
	print("PID of task2 is :",os.getpid())
	print("threadid of main thread is : ",threading.current_thread())

def main():
	print("PID of parent process is :",os.getpid())
	print("threadid of main thread is : ",threading.current_thread())
	no = 5
	t1 = threading.Thread(target = task1, args = (no,))
	t2 = threading.Thread(target = task2, args = (no,))
	
	t1.start()
	t2.start()
	
	t1.join()
	t2.join()

if __name__ == "__main__":
	main()
