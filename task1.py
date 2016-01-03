#Task1.py
# (question,response if yes, response if no)
import sys
import os
from random import randint
# answers = {
# 	1: ('Replace the Battery')
# 	2: ('Reset your phone to factory settings')
# 	3: ('Replce your SIM Card')
# 	4: ('Contact your network operator')
# 	5: ('Please replace your charging cable with an official one a retry the guide')

# }
questions = {
	1: ('Is your phone turning on?',5,2),
	2: ('Does your phone charge when plugged into the wall?',4,3),
	3: ('Are you using the official charger that came with your phone?',6,105),
	4: ('Is your battery removable?',101,106),
	5: ('Are you having display problems?',6,7),
	6: ('Does the screen appear to be cracked or have black splotches beneath the screen?',106,106),
	7: ('Are you having a problem with a specific app on your phone?',102,8),
	8: ('Are you having trouble with getting network signal?',9,10),
	9: ('Have you replaced your simcard?',104,103),
	10: ('Is there a problem with your speaker?',106,11),
	11: ('Is there a problem with your camera?',106,1000),
	
	101: ('Replace the Battery',1000,1000),
	102: ('Reset your phone to factory settings',1000,1000),
	103: ('Replce your SIM Card',1000,1000),
	104: ('Contact your network operator',1000,1000),
	105: ('Please replace your charging cable with an official one and retry the guide',1000,1000),
	106: ('Please send the phone in for repair',1000,1000),
	1000: ('Troubleshooting complete','END','END')
}



def nextq(qno,index):
	if isinstance(questions[qno][index],int):
		#if questions[questions[qno][index]][1] == 1000:
			#return 'END'
		return questions[qno][index]
	else:
		print ('An Error has occured')
		sys.exit()	


def printq(i):
	newq = i
	while 1:
		print (questions[newq][0])
		if questions[questions[newq][1]][1] == 'END':
			print('Troubleshooting complete')
			sys.exit()
		ans = input()
		if ans == 'yes':
			newq = nextq(newq,1)
		elif ans == 'no':
			newq = nextq(newq,2)
		else:
			print ('Invalid input. Please answer "yes" or "no"')
			break

def scan_input():
	"""Prints solutions to common device problems"""
	print ("Please enter your problem")
	question = input().lower()
	if ('screen' in question) or ('display' in question):
		print('screen probs')
		openfile('display.txt')
	elif ('power' in question) or ('turn on' in question) or ('charge' in question) or ('battery' in question):
		openfile('power.txt')
	elif ('sound' in question) or ('music' in question) or ('speaker' in question):
		print('sound.txt')
	elif ('signal' in question) or ('reception' in question):
		print('signal.txt')
	else:
		print('Sorry, no help articles were found for your problem')

def dev_identify():
	"""Identifies device that needs troubleshooting"""
	print ("What device do you need troubleshooting help with?\n Available devices are phones,tablets,laptops,")


def write_casenumber():
	"""Writes new case number to a file"""
	f = open('casenumbers.txt','r')
	if is_emptyfile() = 1:
		newnum = gen_casenumber()
		f.write(newnum)
	else:
		linelist = f.readlines()
		try:
			newnum = int(linelist[-1])+1
			f.write((newnum+1)+'\n')

		except StandardError:
			print ('There was a problem generating a new case number - now exiting')
			sys.exit()
	f.close()


def is_emptyfile():
	"""Checks to see if file is empty"""
	try:
		if os.stat('casenumbers.txt').st_size > 0:
			return 0
		else:
			return 1
	except OSError:
		print "No file found!"


def gen_casenumber():
	"""Generates a random number for the first case number"""
	return randint(0,10000)


def openfile(problem):
	"""Opens file and prints contents"""
	f = open(problem,'r')
	contents = f.read()
	print (contents)
	f.close()	

if __name__ == "__main__":
	print ("Please enter a number for the task you wish to run. Valid numbers are 1,2,3")
	q = input()
	if q=='1':
		printq(1)
	elif q=='2':
		scan_input()
	elif q=='3':
		print ("Question 3")
	else:
		print ('Error in input')