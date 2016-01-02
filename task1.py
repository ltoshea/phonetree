#Task1.py
# (question,response if yes, response if no)
import sys

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
	6: ('Does the screen appear to be cracked or have black splotches beneath the screen?',102,16),
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

printq(1)