import os

def convertBackToGoofyNumberSystem(note):
	if (note == 'a'):
		return '30'
	elif (note == 'b'):
		return '31'
	elif (note == 'c'):
		return '32'
	elif (note == 'd'):
		return '33'
	elif (note == 'e'):
		return '34'
	elif (note == 'f'):
		return '35'
	elif (note == 'g'):
		return '36'
	elif (note == 'h'):
		return '37'
	elif (note == 'i'):
		return '38'
	elif (note == 'j'):
		return '39'
	elif (note == 'k'):
		return '40'
	elif (note == 'l'):
		return '41'
	elif (note == 'm'):
		return '42'
	elif (note == 'n'):
		return '43'
	elif (note == 'o'):
		return '44'
	elif (note == 'p'):
		return '45'
	elif (note == 'q'):
		return '46'
	elif (note == 'r'):
		return '47'
	elif (note == 's'):
		return '48'
	elif (note == 't'):
		return '49'
	elif (note == 'u'):
		return '50'
	elif (note == 'v'):
		return '51'
	elif (note == 'w'):
		return '52'
	elif (note == 'x'):
		return '53'
	elif (note == 'y'):
		return '54'
	elif (note == 'z'):
		return '55'
	elif (note == ','):
		return '56'
	elif (note == '.'):
		return '57'
	elif (note == ';'):
		return '58'
	elif (note == '`'):
		return '59'
	elif (note == 'A'):
		return '60'
	elif (note == 'B'):
		return '61'
	elif (note == 'C'):
		return '62'
	elif (note == 'D'):
		return '63'
	elif (note == 'E'):
		return '64'
	elif (note == 'F'):
		return '65'
	elif (note == 'G'):
		return '66'
	elif (note == 'H'):
		return '67'
	elif (note == 'I'):
		return '68'
	elif (note == 'J'):
		return '69'
	elif (note == 'K'):
		return '70'
	elif (note == 'L'):
		return '71'
	elif (note == 'M'):
		return '72'
	elif (note == 'N'):
		return '73'
	elif (note == 'O'):
		return '74'
	elif (note == 'P'):
		return '75'
	elif (note == 'Q'):
		return '76'
	elif (note == 'R'):
		return '77'
	elif (note == 'S'):
		return '78'
	elif (note == 'T'):
		return '79'
	elif (note == 'U'):
		return '80'
	elif (note == 'V'):
		return '81'
	elif (note == 'W'):
		return '82'
	elif (note == 'X'):
		return '83'
	elif (note == 'Y'):
		return '84'
	elif (note == 'Z'):
		return '85'
	elif (note == '<'):
		return '86'
	elif (note == '>'):
		return '87'
	elif (note == ':'):
		return '88'
	elif (note == '~'):
		return '89'
	elif (note == '_'):
		return '90'
	else:
		return '60'
		print('JACOB YOU CODED THE CONVERTION CHECK WRONG NOOOOOOOOOOOOOOO')
	#et cetera, you need to hardcode these later jacob

def returnToCSV (infile,outpath):

	startThingy = '''0, 0, Header, 1, 2, 480
1, 0, Start_track
1, 0, Title_t, "Close Encounters"
1, 0, Text_t, "Sample for MIDIcsv Distribution"
1, 0, Copyright_t, "This file is in the public domain"
1, 0, Time_signature, 4, 2, 24, 8
1, 0, Tempo, 1200000
1, 0, End_track
2, 0, Start_track
2, 0, Instrument_name_t, "Solo Lute or Keyboard"
2, 0, Program_c, 0, 19''' + '\n'

	endThingy = ''', End_track
0, 0, End_of_file'''

	time = 0
	lastLine = ''

	heregoessometext = open(outpath, 'w')
	heregoessometext.write(startThingy)
	heregoessometext.close()

	with open(infile) as asdfghjkl:
		lines = [line.rstrip('\n') for line in asdfghjkl]

	lastLine = lines[0]

	with open(outpath,'a') as f:
		#god this is gonna be weird to algorithmize
		for line in lines:
			if (line != lastLine):
				#print(line)
				#print(lastLine)
				#print('changes at '+str(time))
				f.write('2, '+str(time)+', Note_on_c, 0, '+convertBackToGoofyNumberSystem(lastLine)+', 0'+'\n')
				f.write('2, '+str(time)+', Note_on_c, 0, '+convertBackToGoofyNumberSystem(line)+', 100'+'\n')
			#print(str(time))
			
			time += 1
			lastLine = line
		f.write('2, ' + str(time) + endThingy)

for i in os.listdir('incust'):
	print(i+' printed into outcsv/'+i[:-4]+'csv')
	returnToCSV('incust/'+i,'outcsv/'+i[:-4]+'csv')