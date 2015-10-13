#Task1.py
# (question,response if yes, response if no)
import sys
questions = {
	1: ('Is your phone turning on?',4,2),
	2: ('Does your phone charge when plugged into the wall?',4,3),
	3: ('Are you using the official charger that came with your phone?',),
	4: ('Are you having display problems?',7,5,),
	5: ('Does the screen appear to be cracked or have black splotches beneath the screen?','',''),
	6: ('Is your battery removable?','',''),
	7: ('Are you having a problem with a specific app on your phone?','fuck off','2nd value'),
}

def fetchanswer(qno,index):
	if isinstance(questions[qno][index],int):
		#print 'here'
		return questions[questions[qno][index]][0]
	else:
		#print 'here2'
		print questions[qno][index]
		sys.exit()


def printq(i):
	print questions[i][0]
	ans = raw_input()
	if ans = 'yes':
		fetchanswer(i,1)
	elif ans = 'no':
		fetchanswer(i,1)
	else:
		print 'error'
		sys.exit

	



printq(1)




# a = raw_input()
# if a=='yes':
# 	print fetchanswer(1,1)
# 	b = 
# # 	print fetchanswer(1,1)
# else:
# 	print fetchanswer(1,2)

# x = 1
# while isinstance(x,int):
#     print questions[x][0]
#     a = 'yes'	
#     if a is "yes": 
#         x = questions[x][1]
#         print x 
#     if a is "no": 
#         x = questions[x][2] 
#         print x

