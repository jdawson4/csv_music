import os

def return_to_csv(infile,outfile):
	time = 0
	time_increment = 120
	opening_text = """0, 0, Header, 1, 2, 480
1, 0, Start_track
1, 0, Title_t, "Close Encounters"
1, 0, Text_t, "Sample for MIDIcsv Distribution"
1, 0, Copyright_t, "This file is in the public domain"
1, 0, Time_signature, 4, 2, 24, 8
1, 0, Tempo, 500000
1, 0, End_track
2, 0, Start_track
2, 0, Instrument_name_t, "Solo Lute or Keyboard"
2, 0, Program_c, 0, 19
"""
	with open(outfile,'w') as x:
		x.write(opening_text)

	lines = [line.rstrip('\n') for line in open(infile)]

	for i in lines:
		time += time_increment
		#print(len(i))
		if len(i) == 5:
			with open(outfile,'a') as f:
				f.write('2, '+str(time)+', Note_on_c, '+i+''', 100
''')
		elif len(i) == 11:
			with open(outfile,'a') as f:
				#print('2, '+str(time)+', Note_on_c, '+i[5:]+', 100\n')
				#print('2, '+str(time)+', Note_on_c, '+i[:5]+', 100\n')
				f.write('2, '+str(time)+', Note_on_c,'+i[5:]+''', 100
''')#maybe now it will be windows compliant?
				f.write('2, '+str(time)+', Note_on_c, '+i[:5]+''', 100
''')
	with open(outfile,'a') as jkl:
		time += time_increment
		jkl.write('''2, '''+str(time)+''', End_track
0, 0, End_of_file
''')

for i in os.listdir('incust'):
	print('incust/'+i+' written into outcsv/'+i[:-4]+'csv')
	return_to_csv('incust/'+i,'outcsv/'+i[:-4]+'csv')