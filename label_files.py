
non_redteam_file = 'auth_filtered_only_non_redteam_lines_filtered.txt'
redteam_file = 'auth_filtered_only_redteam_lines.txt'
outfile = open('auth_filtered_all_with_labels_sorted_2.txt', 'w')

def get_redteam_lines():
	redteam_file = 'redteam.csv'
	tmp = []
	line_count = 0	

	for line in open(redteam_file, 'r'):
		if line_count > 0:
			time = line.split(',')[0].strip()
			dest_user = line.split(',')[1].strip()
			src_nt_host = line.split(',')[2].strip()
			dest_nt_host = line.split(',')[3].strip()
			#print(time,dest_user,src_nt_host,dest_nt_host)

			tmp.append([time,dest_user,src_nt_host,dest_nt_host])
		
		line_count += 1

	return tmp

redteam_activity = get_redteam_lines()

#print(redteam_activity)
#print(type(redteam_activity[0][0]), type(redteam_activity[0][1]), type(redteam_activity[0][2]), type(redteam_activity[0][3]))

line_count = 0 


for line in open('auth_filtered_all_with_labels_sorted.txt', 'r'):
#1,C1085$@DOM1,C1085$@DOM1,C1085,C612,Kerberos,Network,LogOn,Success,1
	time = line.split(',')[0].split()
	src_user = line.split(',')[1].split()
	dest_user = line.split(',')[2].split()
	src_nt_host = line.split(',')[3].split()
	dest_nt_host = line.split(',')[4].split()

	line_count += 1
	
#	if line_count % 10000 == 0:
		#print(line)
#		print(time,src_user,dest_user,src_nt_host,dest_nt_host)
#
#	print(src_nt_host[0])

	is_malicious = 0
	
	for i in redteam_activity:
		if i[0]==time[0] and i[2]==src_nt_host[0] and i[3]==dest_nt_host[0]:
			#print("is_malicious")
			is_malicious = 1
			break
		#print(type(i[0]))
		#print(type(src_nt_host))

	outfile_line = time[0] + ',' + src_user[0] + ',' + dest_user[0] + ',' + src_nt_host[0] + ',' + dest_nt_host[0] + ',' + str(is_malicious) + '\n'

	#print(outfile_line)

	outfile.write(outfile_line)


outfile.close()
