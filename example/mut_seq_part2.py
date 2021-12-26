import sys
import re
import subprocess
import os

filename=sys.argv[1];
seq=sys.argv[2];
file_mut_seq=sys.argv[3];
file_pdb=sys.argv[4];
file_mut_pdb=sys.argv[5];
file_mut_new=sys.argv[6];
seq_reduced=sys.argv[7];
site_num_l=sys.argv[8];
site_num_r=sys.argv[9];

f=open(filename,'r');
String = f.read().replace('\n', '')
print String
string_for_reg_l="\w{"+site_num_l+"}";
string_for_reg_r="\w{"+site_num_r+"}";
start = re.search(string_for_reg_l+seq_reduced+string_for_reg_r, String).start()
end = re.search(string_for_reg_l+seq_reduced+string_for_reg_r, String).end()
new_String = String[:start]+seq+String[end:]
print new_String
f.close()
# f=open(file_mut_seq,'w');
# f.write(new_String);
# f.close;
# print 'Scwrl4 -i %s -o %s -s %s' % (file_pdb,file_mut_pdb,file_mut_seq)
# rc=subprocess.Popen(['Scwrl4 -i %s -o %s -s %s' % (file_pdb,file_mut_pdb,file_mut_seq)],shell=True);
# #rc.poll()
# #print rc.stdout  # sleep outputs nothing but...
# #print rc.returncode  # you get the exit value
# #f=open(file_mut_pos,'w');
# #f.write("%d %d" % (start,end))
# #f.close()

f=open(file_mut_pdb,'r');
PDB_string=[line.split() for line in f]
f.close();
f=open(file_mut_pdb,'r');
PDB_string1=f.readlines();
index_start=int(PDB_string[0][5]);
#print index_start
#print PDB_string[0][1]
#print PDB_string1[0]
f.close();
f=open(file_mut_new,'w');
for index, item in enumerate(PDB_string1, start=0):   # Python indexes start at zero
    if (int(PDB_string[index][5])>=index_start+start and int(PDB_string[index][5])<index_start+end):
#        print index
#        print item
        f.write(item);
    if int(PDB_string[index][5])>=index_start+end:
        break;
f.close();
