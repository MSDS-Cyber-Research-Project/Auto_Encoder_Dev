#!/Users/alexaubrey/anaconda/envs/msds5013/bin/python

redteam_src_hosts = ["C17693","C18025","C19932","C22409"]

redteam_dest_hosts = ["C1","C10","C10005","C1003","C1006","C1014","C1015","C102","C1022","C1028","C10405","C1042","C1046","C10577","C1065","C108","C10817","C1085","C1089","C1096","C11039","C11178","C1119","C11194","C1124","C1125","C113","C115","C11727","C1173","C1183","C1191","C12116","C1215","C1222","C1224","C12320","C12448","C12512","C126","C1268","C12682","C1269"]

non_redteam_src_hosts = ["C606","C1356","C2656","C463","C902","C1185","C1496","C2291","C3680","C676","C954","C1370","C3442","C1398","C1262","C387","C2454","C2130","C1237","C2431","C27137","C4059","C3393","C2652","C3701","C3833","C3990","C4116","C5436","C3271","C158","C4733","C4902","C4942","C5771","C678","C2582","C5427","C2260","C5753","C5974","C6153","C6338","C6519","C6705","C6895","C7083","C7279","C7469","C7656","C7845","C8040","C8234","C8429","C8615","C8800","C8988","C9165","C9353","C9542","C9723","C9912","C10105","C10297","C10482","C10670","C10860","C11044","C11231","C11423","C11596","C11775","C11928","C12152","C12333","C12508","C12693","C12872","C13043","C13232","C13414","C13589","C13776","C13944","C14122","C14296","C14464","C14638","C14808","C14988","C15158","C15335","C15508","C15687","C15857","C16021","C16204","C16383","C16565","C16739","C25121","C17083","C17262","C17427","C17595","C17774","C26347","C18106","C18265","C18440","C18628","C18817","C19006","C19181","C19369","C19554","C19741","C19924","C20104","C20282","C20458","C20625","C20802","C20982","C21132","C21304","C21472","C21649","C21816","C21978","C24870","C22311","C22469","C22632","C22792","C22958","C23133","C23309","C23505","C23677","C23840","C24009","C24174","C24342","C24512","C24668","C24834","C24998","C25148","C25306","C25476","C25632","C25786","C25960","C26139","C26299","C26464","C26634","C26823","C27019"]

#outfile = open('auth_filtered_only_redteam_lines.txt', 'w')
outfile = open('auth_filtered_only_non_redteam_lines_filtered.txt', 'w')
for line in open('auth_filtered.txt', 'r'):
	src_hostname = line.split(",")[3].strip()
	dest_hostname = line.split(",")[4].strip()

	#if src_hostname in redteam_src_hosts or src_hostname in redteam_dest_hosts:
	#if not src_hostname in redteam_src_hosts and not src_hostname in redteam_dest_hosts:
	if src_hostname in non_redteam_src_hosts: 
		outfile.write(line)
outfile.close()
