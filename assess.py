from inspect import currentframe
import operator

def get_linenumber():
    cf = currentframe()
    return cf.f_back.f_lineno

# Assess basic knowledge from each subject
topic = ['Literature','Economics','Music','Technology','Politics']
print "\nWELCOME !!!"
print "\nTest your knowledge from the field of literature, economics, music, technology and politics and know your strong and weak areas."
print "\nInstruction: You will be given only one chance for each topic. So choose the order of topics wisely."

print "\nCaution: Don't press 'Ctrl + C' by any chance. Please complete all the topics in one session.\n"
print 'Hello There !!!'
while True:
	name = raw_input('Kindly tell me your name : ')
	if not name:
		print "I need a name to know you better, Please tell me :)"
	else:
		break
		
print "\nHi",name,"It's good to have you here. Enjoy :)"
print "\nNow, %s, you will have five MCQ in each topic. These are few basic questions." % name
	
print "All the very best !!!\n"

def take_input():
	sub = raw_input('Choose a topic by inserting the index corresponding to it: ')
	val = chk_inp(sub)
	if not val:
		print "\nOops: Wrong entry, please input a correct entry"
		return take_input()
	else:
		return val
	
def print_top():
	i = 1;
	for top in topic:
		print '[%d]:%s\t'%(i,top),
		i += 1
	print '\n'

def chk_inp(entry):
	try:
		val = int(entry)
		if val in range(1,len(topic)+1):
			return val
	except ValueError:
		if entry in topic:
			return topic.index(entry)+1

count = 1
#https://interestingliterature.com/2015/11/30/the-best-literature-quiz/

Lit = [['Which actor first played Hamlet on film?','Henry Irving','Sarah Bernhardt','Charlie Chaplin','b'],["Who coined the phrase 'Wars of the Roses'?",'William Shakespeare','Sir Thomas More','Sir Walter Scott','c'],['Who came up with the name Gotham City?','Washington Irving','Bill Finger','Tim Burton','a'],["What is the name of the world in which The Lord of the Rings is set?",'Middle-Earth','Arda','Boxen','b'],['Which Scottish author first killed off Sherlock Holmes?','J. M. Barrie','Sir Arthur Conan Doyle','Robert Louis Stevenson','a']]

Eco = [['What economic policy would most likely be used to combat a recession when inflation is low?','An increase in taxes','An increase in the money supply','An increase in stock market prices','b'],['Which of the following is the most widely used measure of inflation?','The Consumer Price Index','The Index of Leading Economic Indicators','The prime rate','a'],['What are the three basic economic questions?','What, where, whom','What, how, whom','How, whom,when','b'],['What are the four factors of production?','Land, capital, money, entrepreneurs','Land, capital, labor, entrepreneurs','Labor, capital, supply, demand','b'],['The opportunity cost of an item is:','What you give up to get that item','The currency value of the item','The number of hours needed to earn money to buy the item','a']]

Mus = [['Which one of these songs did Ludwig van Beethoven write?','Ode to Joy','Hallelujah Chorus','Rejoice','a'],['A bass is in the _______ family.','Percussion','Woodwind','String','c'],['Mixture of long and short sounds adds a :','rhythm','bass effect','beat effect','a'],["The Eagles' _______ song is considered to be their most famous and most mysterious song. ",'Hotel California','Witchy Woman',"Lyin' Eyes",'a'],["Pink Floyd's song _______ on the album 'Wish You Were Here' was sung by Roy Harper, a folk singer who was not a member of Pink Floyd(only Pink Floyd recording to feature guest lead vocals).",'Welcome to the Machine','Wish You Were Here','Have a Cigar','c']]

Tech = [['The technologically advanced humanoid robot ASIMO is made by which car company?','Suzuki','Honda','Toyota','b'],['Along with whom did Bill Gates found Microsoft?','Paul Allen','Andrea Lewis','Marla Wood','a'],['What is the name of the first satellite sent into space?','Echo','Explorer','Sputnik','c'],['How many bones do sharks have in their bodies?','0','164','356','a'],['What type of artificial intelligence (AI) program, first developed in the mid-1900s, is designed to differentiate a human from a computer?','Blue Brain project','Google Brain','Turing Test','c']]

#http://global.oup.com/uk/orc/politics/intro/garner2e/01student/mcqs/
Pol = [['Which three states do not have a codified constitution?','Cuba, China, and Russia','The UK, New Zealand, and Israel','The UK, Iraq, and Afghanistan','b'],["Who wrote that the state is an institution which claims 'a monopoly of the legitimate use of physical force in enforcing order within a given territorial area'?",'Max Weber','William Blackstone','Robert Dahl','a'],['Typically, Marxist structuralists argue that...','individuals are capable of shaping their own destinies','capitalists are inherently immoral','even well-intentioned capitalists are forced by the logic of the system to exploit their workers','c'],['Direct democracy is the system in which...','citizens are allowed to debate with their representatives in open public meetings','citizens represent themselves in the decision-making process',"senior political leaders are known as 'Directors'",'b'],['The most potent criticism of classical pluralism is that...','the theory is naive, because some groups are much more influential than others','it fosters existing divisions within society','it makes people think that all viewpoints are equally valid','a']]

options = ['a','b','c']
def display_all():
	print "\n\nLiterature\n"
	for que in range(0,5):
		print "\nQ.%d" % (que+1),
		print "%s" % Lit[que][0]
		print "[A]: %s\t [B]: %s\t [C]: %s\t Answer:%s\t You Selected:%s" % (Lit[que][1],Lit[que][2],Lit[que][3],Lit[que][4].upper(),Lit[que][5].upper())
	
	print "\n\nEconomics\n"
	for que in range(0,5):
		print "\nQ.%d" % (que+1),
		print "%s" % Eco[que][0]
		print "[A]: %s\t [B]: %s\t [C]: %s\t Answer:%s\t You Selected:%s" % (Eco[que][1],Eco[que][2],Eco[que][3],Eco[que][4].upper(),Eco[que][5].upper())
	
	print "\n\nMusic\n"
	for que in range(0,5):
		print "\nQ.%d" % (que+1),
		print "%s" % Mus[que][0]
		print "[A]: %s\t [B]: %s\t [C]: %s\t Answer:%s\t You Selected:%s" % (Mus[que][1],Mus[que][2],Mus[que][3],Mus[que][4].upper(),Mus[que][5].upper())
	
	print "\n\nTechnology\n"
	for que in range(0,5):
		print "\nQ.%d" % (que+1),
		print "%s" % Tech[que][0]
		print "[A]: %s\t [B]: %s\t [C]: %s\t Answer:%s\t You Selected:%s" % (Tech[que][1],Tech[que][2],Tech[que][3],Tech[que][4].upper(),Tech[que][5].upper())
		
	print "\n\nPolitics\n"
	for que in range(0,5):
		print "\nQ.%d" % (que+1),
		print "%s" % Pol[que][0]
		print "[A]: %s\t [B]: %s\t [C]: %s\t Answer:%s\t You Selected:%s" % (Pol[que][1],Pol[que][2],Pol[que][3],Pol[que][4].upper(),Pol[que][5].upper())
	
res = {}
def begin_quiz(set):
	right = 0
	raw_input("Carefully choose the correct option. Press Enter when ready >")
	for que in range(0,5):
		print "\nQ.%d" % (que+1),
		print "%s" % set[que][0]
		print "[A]: %s\t [B]: %s\t [C]: %s" % (set[que][1],set[que][2],set[que][3])
		user_choice = raw_input('Your Answer:')
		if user_choice.lower() not in options:
			user_choice = raw_input('Please answer A,B or C. Your Answer:')
		set[que].append(user_choice)
		if user_choice.lower() == set[que][4]:
			right += 1
	
	return right
	
while count<=5:
	print_top()
	index = take_input()
	print "\nStarting Quiz: %d, Topic: %s" % (count,topic[index-1])
	if topic[index-1] == 'Literature':
		pos = begin_quiz(Lit);
	elif topic[index-1] == 'Economics':
		pos = begin_quiz(Eco);
	elif topic[index-1] == 'Music' :
		pos = begin_quiz(Mus)
	elif topic[index-1] == 'Technology' :
		pos = begin_quiz(Tech)
	else :
		pos = begin_quiz(Pol)
	res[topic[index-1]] = pos
	if count<=4:
		print '\nI hope it was fun!! Lets proceed to the next topic now.'
	else:
		print '\nI hope you enjoyed the questions and the overall experience' 
	del topic[index-1]
	count += 1
	
raw_input("Relax now !!!  Press Enter whenever you are ready for results >>>")
print "\nPlease find your score from each topic and your aggregate score \n"
sorted_x = [(k, res[k]) for k in sorted(res, key=res.get, reverse=True)]
total=0
for element in sorted_x :
	print '%-15s\t|\t%s/5'%(element[0],element[1])
	total += element[1]
	
print '\n%-15s\t|\t%s/25\n'%('Total',total)
key = raw_input('Do you want to see the answer key? (y/n) > ')
if key == 'y' or not key :
	display_all()

print '\nThanks for playing\nWISH YOU A VERY HAPPY NEW YEAR\n'
new_inp=raw_input('Do you want to know which are the first and last places to witness NEW YEAR? (y/n)> ')

if new_inp == 'y' or not new_inp:
	print "\nFirst: Kiritimati, Nukualofa, Apia, Neiafu\nLast: Baker Island, Howland Island\n"
	
print "Have a good day\n"
	

