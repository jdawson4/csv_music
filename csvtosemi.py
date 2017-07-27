import os

def customize (inpath, outpath):
	#print(inpath)
	time=''
	note=''
	outfile = open(outpath,'w') #creates a new file for output
	
	with open(inpath) as f:

		lines = [line.rstrip('\n') for line in open(inpath)]

		for i in lines:
			#print(i[-4:])
			if i[-3:] == '100':
				
				print('working')
				time = i[3:-23]
				note = i [-11:-5]
				print(time + note)
				f = open(outpath, 'a')
				f.write(time+ ' ' +note+'\n')
				f.close()

for j in os.listdir('incsv'):
	print(j + ' written into ' + j[:-4] + '.cust')
	customize('incsv/' + j, 'outcust/' + j[:-4] + '.cust')

#JESUS CHRIST IT WORKED.