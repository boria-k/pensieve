import os
import sys


rootdir = sys.argv[1]

for subdir, dirs, files in os.walk(rootdir):
	for file_in in files:
		if file_in.endswith('.log'):
			#print file
			with open (rootdir + file_in, 'r') as in_log_file:
				file_out = file_in + '.pens'
				with open (file_out, 'w') as out_log_file:
					firstLine = True
					for line in in_log_file:
						if line.strip() :
							splitted_line = line.split(' ')
							num_of_bytes = splitted_line[4]
							delta_t = splitted_line[5]
							if not firstLine:
								timestamp = timestamp + int(delta_t)
							else:
								timestamp = 0
								firstLine = False
	
							bandwidthMbitSec = 8.0*(float(num_of_bytes)/float(delta_t))/1000.0
							out_log_file.write(`timestamp/1000.0` + ' ' +  `bandwidthMbitSec` + '\n')
				out_log_file.close()
			in_log_file.close()




