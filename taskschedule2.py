import datetime
import schedule
import time

def Schedule_minute():
	print("Schedular schedules after a minute ...")
	print("Current time is : ",datetime.datetime.now())
	print()
	
def Schedule_hour():
	print("Schedular schedules after a hour ...")
	print("Current time is : ",datetime.datetime.now())
	print()
	
def Schedule_Sunday():
	print("Schedular schedules after a Sunday ...")
	print("Current time is : ",datetime.datetime.now())
	print()

def main():
	print("Automations using python ")
	
	schedule.every(1).minutes.do(Schedule_minute)
	schedule.every().hour.do(Schedule_hour)
	schedule.every().sunday.do(Schedule_Sunday)
	
	while True:
		schedule.run_pending()
		time.sleep(1)
	
if __name__ == "__main__":
	main()
