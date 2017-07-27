import os

def shorten_info (inpath, outpath):
	#print(inpath)
	time=''
	note=''
	outfile = open(outpath,'w') #creates a new file for output
	
	with open(inpath) as f: #tbh im not reaaaally sure that this line is necessary, but i dont wanna risk it

		lines = [line.rstrip('\n') for line in open(inpath)]

		for i in lines:
			#print(i[-21:-12])
			if (i[-3:] == '100') & (i[-21:-12] == 'Note_on_c'): #so now we're only reading lines with notes
				
				#print('working')
				time = i[3:-23] #this is the first thing we care about
				note = i [-11:-5] #this is the only other thing we care about. Seriously, if it's written like this csv, it has no other useful information.
				#print(time + note) #so we can see whats goign on
				f = open(outpath, 'a')
				f.write(time+note+'\n') #should output the same as the print() function
				f.close()

#which is great and all, but I gotta make a new file structure that plays the notes at the same time. Y'know, so it sounds right.
#unless, of course, the neural net learns to count up whenever it makes a new line.
#who knows.

def normalize_time(inpath, outpath): #note to self: if this screws up, change the names of all these variables
	time = ''
	note = ''
	outfile = open(outpath,'w')

	lines = [line.rstrip('\n') for line in open(inpath)] #maybe unnecessary? we'll see.
	
	#ok so now, whereever in 'times' the number matches, I wanna have all the notes record to the same line.
	#note, I will not enjoy converting this back into a csv.

	last_i = ''
	for i in lines:
		if (last_i != '') & (i[:-6] == last_i[:-6]):
			
			#get rid of the last line of stuff in the outfile before we add the new two notes

			with open(outpath,'r') as q:
				foo = q.readlines()
			foo = foo[:-1]

			#moarvariables = open(outpath,'w')
			#moarvariables.close()

			with open(outpath, 'r+') as bar:
				for foobar in foo:
					bar.write(foobar)
			#i know i know im a bad coder yeah yeah

			f = open(outpath, 'a')
			f.write(last_i[-5:] + i[-6:] + '\n')
			f.close()
		else:
			#in case it's a whole new time
			with open(outpath,'a') as g:
				g.write(i[-5:] + '\n')
		last_i = i


for j in os.listdir('incsv'):
	print('incsv/'+j + ' written into ' + j[:-4] + '.cust')
	shorten_info('incsv/' + j, 'outsemi/' + j[:-4] + '.cust')
for k in os.listdir('outsemi'):
	print('outsemi/'+k + ' written into outcsv/' + k)
	normalize_time('outsemi/' + k, 'outcust/' + k)