
import sys
import os
import traceback
from random import randint

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

def q3():
	"""Identifies device that needs troubleshooting and loads relevant questions"""
	
	print ('What device do you need troubleshooting help with?\n Available selections are mobile phone, tablet or laptop')
	device = input().lower()
	print ('What is the Manufacturer of your device? (For example Samsung, Apple)')
	manufacturer = input().lower()
	print("What is the serial number on your device? (this can normally be found on the back of your device. Enter 0 if you don't know)")
	serialnum = input().lower()
	print("Have you bought the product within the last 12 months?")
	warranty = input().lower()

	if ('phone' in device) or ('mobile' in device) or ('mobile phone' in device):
		content = openfileq3('phone')
		# Need to add an android /apple section here
	elif ('laptop' in device):
		content = openfileq3('laptop')
	elif ('tablet'):
		print ('tablet troubleshooting detected')
	else:
		print('Sorry, no help articles were found for your device')
	
	print ('First We will offer you some generic troubleshooting tips for your type of device')
	scan_input()
	print ('Do you need further assistance?')
	ans = input().lower()
	if ans == 'yes':
		print (content)
		print ('Did this solve your problem?')
		ans = input().lower()
		if ans == 'yes':
			print('We are glad we could solve your problem!')
		elif ans == 'no':
			check_casedir()
			case_number = new_casenumber()
			f = open(case_number,'w+')
			f.write(device+'\n')
			f.write(manufacturer+'\n')
			f.write(serialnum+'\n')
			f.write(warranty+'\n')
			f.close()
			print ('Please send your phone in for repair, your case number is {}'.format(case_number))
		else:
			print ('Invalid input, needs to be yes or no')
			sys.exit()

	elif ans == 'no':
		print('We are glad we could solve your problem!')




def check_casedir():
	"""Creates a casenumber directory if it does not already exist"""
	if not os.path.exists('casenumbers'):
		print ("Cases directory does not exist, this will be created now.")
		os.makedirs('casenumbers')

def gen_casenumber():
	"""Generates a random number for the first case number"""
	return str(randint(0,10000))

def new_casenumber():
	"""Creates new unique case number based on existing case numbers"""
	dirs = os.listdir('casenumbers')
	if dirs == []:
		return gen_casenumber()
	else:
		sortedlist = sorted(dirs,key=int)
		newcasenum = int(sortedlist[-1])+1
		return newcasenum

def openfile(problem):
	"""Opens file and prints contents"""
	f = open(problem,'r')
	contents = f.read()
	print (contents)
	f.close()	


def openfileq3(device):
	if device == 'phone':
		f = open('phoneq.txt','r')
	elif device == 'laptop':
		f = open('laptop.txt','r')
	else:
		print('random error')
		sys.exit
	lines = f.readlines()
	return lines

if __name__ == "__main__":
	print ("Please enter a number for the task you wish to run. Valid numbers are 1,2,3")
	q = input()
	if q=='1':
		printq(1)
	elif q=='2':
		scan_input()
	elif q=='3':
		#check_casedir()
		#new_casenumber()
		q3()
	else:
		print ('Error in input')