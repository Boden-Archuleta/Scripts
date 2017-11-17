import sys
import datetime 
import time 
import webbrowser

def main():
	if len(sys.argv) != 6:
		print("This script requires five arguements: Year, month, day, hour, and minute")
		sys.exit()
	year = int(sys.argv[1])
	month = int(sys.argv[2])
	day = int(sys.argv[3])
	hour = int(sys.argv[4])
	minute = int(sys.argv[5])
	alarmTime = datetime.datetime(year, month, day, hour, minute, 0)
	print("alarm set!")
	while datetime.datetime.now() < alarmTime:
		time.sleep(1)
	webbrowser.open("https://www.youtube.com/watch?v=k2a30--j37Q&t=31s")



if __name__ == "__main__":
    main()