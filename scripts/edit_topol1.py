import re
import sys

filename=sys.argv[1];
output=sys.argv[2];

f=open(filename,'r');
lines=f.readlines();
f.close();
#print lines
index=0;
d1={};
categ="";
for index in range(len(lines)):
    if lines[index][0]=="[":
        categ=lines[index].split()[1] 
#        print categ
        #dict[categ]=index
    if categ!="" and lines[index][0]!=";":
        try:
            d1[categ].append(lines[index].strip()+" "+str(index))
        except KeyError:
            d1[categ]=[lines[index].strip()+" "+str(index)]

ind_list=[]
atomid_list=[]

for key,value in d1.items():
#    print value
    if key=="bonds" or key=="pairs":
        lists_all=[]
        for items in value:
            if len(items.split())>=2:
                atomid1=items.split()[0]
                atomid2=items.split()[1]
                if atomid1.isdigit() and atomid2.isdigit():
                    list_temp=[atomid1, atomid2]
#                    print list_temp in lists_all
                    if (list_temp not in lists_all):
                        lists_all.append(list_temp)
                    else:
                        #print int(items.split()[-1])
                        ind_list.append(int(items.split()[-1]))

    if key=="angles":
        lists_all=[]
        for items in value:
            if len(items.split())>=3:
                atomid1=items.split()[0]
                atomid2=items.split()[1]
                atomid3=items.split()[2]
                if atomid1.isdigit() and atomid2.isdigit() and atomid3.isdigit():
#                    print atomid1
                    list_temp=[atomid1, atomid2, atomid3]
#                    print lists_all
                    if (list_temp not in lists_all):
                        #print "yes"
                        lists_all.append(list_temp)
                        #print lists_all
                    else:
                        #print int(items.split()[-1])
                        ind_list.append(int(items.split()[-1]))
    if key=="dihedrals":
        lists_all=[]
        for items in value:
            if len(items.split())>=4:
                atomid1=items.split()[0]
                atomid2=items.split()[1]
                atomid3=items.split()[2]
                atomid4=items.split()[3]
                if atomid1.isdigit() and atomid2.isdigit() and atomid3.isdigit() and atomid4.isdigit():
                    list_temp=[atomid1, atomid2, atomid3, atomid4]
                    if (list_temp not in lists_all):
                        lists_all.append(list_temp)
                    else:
                        #print int(items.split()[-1])
                        ind_list.append(int(items.split()[-1]))
    if key=="cmap":
        lists_all=[]
        for items in value:
            if len(items.split())>=5:
                atomid1=items.split()[0]
                atomid2=items.split()[1]
                atomid3=items.split()[2]
                atomid4=items.split()[3]
                atomid5=items.split()[4]
                if atomid1.isdigit() and atomid2.isdigit() and atomid3.isdigit() and atomid4.isdigit() and atomid5.isdigit():
                    list_temp=[atomid1, atomid2, atomid3, atomid4,atomid5]
                    if (list_temp not in lists_all):
                        lists_all.append(list_temp)
                    else:
                        print int(items.split()[-1])
                        ind_list.append(int(items.split()[-1]))
f=open(output,'w')
for index in range(len(lines)):
    if index in ind_list:
        continue
    else:
        f.write(lines[index])

