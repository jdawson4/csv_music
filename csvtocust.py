import os

def meganify(inTim):
	if inTim == '30':
		return'a'
	elif inTim == '31':
		return'b'
	elif inTim == '32':
		return'c'
	elif inTim == '33':
		return'd'
	elif inTim == '34':
		return'e'
	elif inTim == '35':
		return'f'
	elif inTim == '36':
		return'g'
	elif inTim == '37':
		return'h'
	elif inTim == '38':
		return'i'
	elif inTim == '39':
		return'j'
	elif inTim == '40':
		return'k'
	elif inTim == '41':
		return'l'
	elif inTim == '42':
		return'm'
	elif inTim == '43':
		return'n'
	elif inTim == '44':
		return'o'
	elif inTim == '45':
		return'p'
	elif inTim == '46':
		return'q'
	elif inTim == '47':
		return'r'
	elif inTim == '48':
		return's'
	elif inTim == '49':
		return't'
	elif inTim == '50':
		return'u'
	elif inTim == '51':
		return'v'
	elif inTim == '52':
		return'w'
	elif inTim == '53':
		return'x'
	elif inTim == '54':
		return'y'
	elif inTim == '55':
		return'z'
	elif inTim == '56':
		return','
	elif inTim == '57':
		return'.'
	elif inTim == '58':
		return';'
	elif inTim == '59':
		return'`'
	elif inTim == '60':
		#print('just letting you know, im workinggggggggggggggggggggggggggggggggggggggggggggggggggggggg')
		return'A'
	elif inTim == '61':
		return'B'
	elif inTim == '62':
		return'C'
	elif inTim == '63':
		return'D'
	elif inTim == '64':
		return'E'
	elif inTim == '65':
		return'F'
	elif inTim == '66':
		return'G'
	elif inTim == '67':
		return'H'
	elif inTim == '68':
		return'I'
	elif inTim == '69':
		return'J'
	elif inTim == '70':
		return'K'
	elif inTim == '71':
		return'L'
	elif inTim == '72':
		return'M'
	elif inTim == '73':
		return'N'
	elif inTim == '74':
		return'O'
	elif inTim == '75':
		return'P'
	elif inTim == '76':
		return'Q'
	elif inTim == '77':
		return'R'
	elif inTim == '78':
		return'S'
	elif inTim == '79':
		return'T'
	elif inTim == '80':
		return'U'
	elif inTim == '81':
		return'V'
	elif inTim == '82':
		return'W'
	elif inTim == '83':
		return'X'
	elif inTim == '84':
		return'Y'
	elif inTim == '85':
		return'Z'
	elif inTim == '86':
		return'<'
	elif inTim == '87':
		return'>'
	elif inTim == '88':
		return':'
	elif inTim == '89':
		return'~'
	elif inTime == '90':
		return'_'
	else:
		#print('jacob you coded wrong')
		return''

def customize (inpath, outpath):

	CSVnote = ''
	CUSTnote = ''
	time = ''
	greatest_time = '-1'
	timeNumber = 0
	goddammitwhywontyouiterateoverintegers = 0
	seriouslyjustiterateoverintegers = 0
	number_of_spaces = 0
	lastLine = '2, 0, Note_on_c, 0, 79, 100'

	justforthelols = open(outpath,'w')
	#makes/clears a new file in the folder outcust
	justforthelols.close()

	with open(inpath) as jkl:

		lines = [line.rstrip('\n') for line in open(inpath)]
	with open(outpath,'a') as f:

		for e in lines:
			#print(e[-21:-12])
			if (e[-3:] == '100') & (e[-21:-12] == 'Note_on_c'):

				time = e[3:-23]
				#print(time)
				if (int(greatest_time) < int(time)):
					greatest_time = time
		print('greatest time found: '+greatest_time)
		#this whole block of code should just
		#find the highest time in the piece

		for line in lines:
			if (line[-21:-12] == 'Note_on_c') & (line[-3:] == '100'):
				number_of_spaces  = int(line[3:-23]) - int(lastLine[3:-23])
				#print(int(number_of_spaces))
				seriouslyjustiterateoverintegers=0
				while seriouslyjustiterateoverintegers < number_of_spaces:
					#thing
					f.write(meganify(line[-7:-5])+'\n')
					#print(meganify(line[-7:-5]))
					seriouslyjustiterateoverintegers += 1
				#f.write(meganify(line[-7:-5])+'\n')
				#print(line[-7:-5])
				lastLine = line
				#print(lastLine)

for q in os.listdir('incsv'):
	print(q + ' written into outcust/'+q[:-3]+'cust')
	customize('incsv/'+ q , 'outcust/'+q[:-3]+'cust')