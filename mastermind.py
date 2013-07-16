#Created by Gaurav Singha Roy 
#Date : 26 Jun 2013

#This is a Mastermind algorithm implementation with constant size memory
#Here this is a memory restriction for the algorithm, where we are allowed only two strings, viz. x and y in the memory to store our data. 
#The main strategy would be that of figuring the right combination of block string from the x memory and forgetting the data from x memory after that
#The codebreaker is referred to as Paul and the codemaker as Carol


import datetime
import itertools
import math
import random
import sys

n = 0 #This is the number of positions in the game
k = 0 #This is number of possible of colors, if say k = 3 then, the possible colors would be digits 0,1,2
z = ""  #z is carole's secret code
y = [] 	#This is the first memory, where we store our sampling reference string. our objective would be to get eq(z,y) = n
x = [] #This the second memory where we store carole's responses. Now for simplicity of implementation we are using this as an array instead of a binary encoded string. There is a restriction to the size of x. We can store only k number of carole's responses here.
s = 0 #This is the block size
t = 0 #This will be the max number of guesses and its responses we can store in the memory x
i = 0 #This is the iterator for the block to find the secret code for that block


def get_time_diff(start_time,end_time):
	diff = (end_time - start_time).total_seconds()
	return str(diff) +"s"


#This functions returns an integer value between 0 and 10. It returns the number of positions in which the guess and the secret coincide
def eq(secret,guess): 	
	result = 0
	for a in range(0,n):
		if secret[a] == guess[a]:
			result += 1
	print "Guessing : "+guess+" | returned = "+str(result)	
	return result		

#this function evaluates the block level eq(z,x), eg b_eq('111') in the 1st block with y = "000000" and z = "113456" will check eq('113456','111000')
def b_eq(b_s):
	guess = ""
	for a in range(0,n):
		if a >= i*s and a < (i*s) + s:
			guess += b_s[a-(i*s)]
		else:
			guess += y[0][a]
	return eq(z,guess)		

#this function 
def single_b_eq(color,pos):
	guess = ""
	for a in range(0,n):
		if a != pos:
			guess += y[0][a]
		else:
			guess += color	
	return eq(z,guess) 

#in this function we update y with the correctly founded block in x. This is the substitute function of the algorithm
def update_y_with_block(block_val):
	global x,y
	original_y = y[0]
	new_y = ""
	for a in range(0,n):
		if a >= i*s and a < (i*s) + s:
			new_y += block_val[0][a-(i*s)]
		else:
			new_y += y[0][a]
	y[0] = new_y
	y[1] = block_val[1]	
	x = []

#This function generates the s_consistent string, which stores the string for the block in which currently
def generate_s_consistent(colors):
	perm_l =  sorted(set(list(itertools.permutations(colors,s))))
	final_list = []
	for l in perm_l:
		final_list.append(''.join(str(elem) for elem in l))
	return final_list	

#This function checks if the current block to be guessed is present in 
def is_block_present(block):
	result = False
	for ind_x in x:
		if block == ind_x[0]:
			result = True
			break
	return result	

#In this function we forget/delete specific entries in x which are marked for forgetting
def forget_x():
	global x
	result = []
	for x_ind in x:
		if x_ind[0] != "$":
			result.append(x_ind)
	x = result	

#This function updates only one element in the position 'pos'
def update_single_element_of_y(x_block,pos):
	global x,y
	final_y = ""
	for a in range(0,n):
		if a != pos:
			final_y += y[0][a]
		else:
			final_y += x_block[0]
	y = [final_y,x_block[1]]
	x = []			

#This function checks if the inputted values are proper or not
def check_vals():
	global s
	result = True
	if len(z) != n:
		print "The length of secret code is not "+str(n)
		result =  False
	else:
		for a in range(0,n):
			if int(z[a]) >= k:
				print "Invalid color '"+z[a]+"' in z"
				result = False
				break 
		if s > 4: #This condition is put to improve the worst case
			if k <= 4:
				s = k -1
			else:
				s = 4						
	
	return result
#This function initializes the values
def initialize():
	global y, x, i, z, n, k, s, t
	#f = open(sys.argv[1])
	f = open("input/"+sys.argv[1])
	lines = f.readlines()
	f.close
	lines[0] = lines[0].replace("\n","").replace(" ","").replace("z","").replace("=","")
	lines[1] = lines[1].replace("\n","").replace(" ","").replace("k","").replace("=","")
	 
	k = int(lines[1]) 
	z = lines[0]	
	n = len(z)
	print "z = "+z
	print "k = "+str(k)
	s = int(math.sqrt(n)) 
	t = int(s/math.log10(s))
	new_y = ""
	for a in range(0,n):
		new_y += "0" #Initializing y
	y.append(new_y)	
	y.append(eq(z,y[0]))


#This function starts the mastermind guessing game
def start_mastermind():
	global y, x, i
	initialize()
	if check_vals() == True:
		continue_loop = True
		while(continue_loop):
			if i < (n-1)/s:
				min_delta = y[1]
				x_counter = 0
				delta_total = 0
				for k_counter in range(1,k):
					guess_str = ""
					for s_counter in range(0,s):
						guess_str += str(k_counter)
					x.append([guess_str, b_eq(guess_str)])
					if x[x_counter][1] < min_delta:
						min_delta = x[x_counter][1] 
					elif x[x_counter][1] - min_delta == s: #Paul goes into this block if the block matches carol's code. It will go here in cases like (222 for i = 1 and the secret code z is 0132224552 )
						print "Found block"+str(i)+" : "+x[x_counter][0]
						update_y_with_block(x[x_counter])
						x = []
						i+=1
						break
					elif y[1] - x[x_counter][1] == s:
						print "Found block"+str(i)+" : "+y[0][i*s:(i*s)+s]
						x = []
						i+=1
						break	
					if x[x_counter][1] > min_delta:
						delta_total += x[x_counter][1] - min_delta
						if delta_total >= s:
							break
					x_counter += 1

				if len(x) > 0:
					possible_colors = ""
					if y[1] > min_delta:
						for a in range(0,y[1]-min_delta):
							possible_colors += "0"
					x_counter = 0
					for individual_x in x:
						if individual_x[1] > min_delta:
							for a in range(0,individual_x[1]-min_delta):
								possible_colors += individual_x[0][0]
						elif individual_x[1] == min_delta:
							individual_x[0] = "$" #marked for forgetting/deletion
						x_counter += 1	
					forget_x()				
					s_consistent =  generate_s_consistent(possible_colors)
					while True: #In this block, we try to randomly guess the correct sequence in the block with the values from s_consistent
						curr_block_guess = s_consistent[random.randint(0,len(s_consistent)-1)]
						if is_block_present(curr_block_guess) == False:
							if len(x) == t:
								x.pop() 
							x.append([curr_block_guess,b_eq(curr_block_guess)])
							if x[-1][1] - min_delta == s:
								if x[-1][1] == n:
									continue_loop = False
								print "Found block"+str(i)+" : "+x[-1][0]
								update_y_with_block(x[-1])

								i+=1
								x = []
								break 
			else:	#This is the last part of the string. in this individual element is randomly tried to guess correctly
				for i_counter in range(i*s,n):
					while True:
						curr_color = str(random.randint(1,k-1))
						if is_block_present(curr_color) == False:
							if len(x) == t:
								x.pop()
							x.append([curr_color,single_b_eq(curr_color,i_counter)])
							if x[-1][1] > y[1]:
								update_single_element_of_y(x[-1],i_counter)	 
								if y[1] == n:
									continue_loop = False
									break
							elif x[-1][1] < y[1]:
								x = []
								break	

start_time = datetime.datetime.now()
start_mastermind()
end_time = datetime.datetime.now()
print "Total time taken : " + get_time_diff(start_time,end_time)

