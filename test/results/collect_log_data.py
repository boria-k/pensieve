import os
import sys

ignore_first_segment = True
file_name_prefix = 'log_sim_rbased'
if len(sys.argv) > 1:
	file_name_prefix = sys.argv[1]
rootdir = '.'
sum_of_bitrates = 0
sum_of_rebufs = 0
num_of_segments = 0
for subdir, dirs, files in os.walk(rootdir):
	for file in files:
		if file.startswith(file_name_prefix):
			#print file
			with open (file, 'r') as log_file:
				firstLine = True
				for line in log_file:
					if not ignore_first_segment or not firstLine:
						if line.strip() :
							splitted_line = line.split('\t')
							bitrate = splitted_line[1]
							rebuf = splitted_line[3]
							if float(rebuf) > 0:
								print file + ' bitrate ' + bitrate + ' rebuf ' + rebuf
							sum_of_bitrates += float(bitrate)
							sum_of_rebufs += float(rebuf)
							num_of_segments += 1          	
					firstLine = False
average_bitrate = sum_of_bitrates/num_of_segments
average_rebuf = sum_of_rebufs/num_of_segments

print 'average bitrate ' + `average_bitrate` + ' average rebuffering ' + `average_rebuf`

