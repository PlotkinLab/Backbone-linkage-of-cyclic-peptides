import re
import sys

filename=sys.argv[1];
output=sys.argv[2];
seq=sys.argv[3];

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

value=d1["atoms"];
for items in value:
    if len(items.split())>=3:
        resid=items.split()[2]
        if resid.isdigit() and int(resid)==10:
            ind_list.append(int(items.split()[-1]))
            #print items.split()[0]
            atomid_list.append(int(items.split()[0]))
        if resid.isdigit() and int(resid)==10+len(seq)-1:
            ind_list.append(int(items.split()[-1]))
            atomid_list.append(int(items.split()[0]))    

for key,value in d1.items():
    if key=="bonds" or key=="pairs":
        for items in value:
            
            if len(items.split())>=2:
                atomid1=items.split()[0]
                atomid2=items.split()[1]
                if atomid1.isdigit() and atomid2.isdigit() and ((int(atomid1) in atomid_list) or int(atomid2) in atomid_list):
                    #print atomid1
                    ind_list.append(int(items.split()[-1]))
    if key=="angles":
        for items in value:
            if len(items.split())>=3:
                atomid1=items.split()[0]
                atomid2=items.split()[1]
                atomid3=items.split()[2]
                if atomid1.isdigit() and atomid2.isdigit() and atomid3.isdigit() and ((int(atomid1) in atomid_list) or int(atomid2) in atomid_list or int(atomid3) in atomid_list):
#                    print atomid1
                    ind_list.append(int(items.split()[-1]))
                    
    if key=="dihedrals":
        for items in value:
            if len(items.split())>=4:
                atomid1=items.split()[0]
                atomid2=items.split()[1]
                atomid3=items.split()[2]
                atomid4=items.split()[3]
                if atomid1.isdigit() and atomid2.isdigit() and atomid3.isdigit() and atomid4.isdigit() and ((int(atomid1) in atomid_list) or int(atomid2) in atomid_list or int(atomid3) in atomid_list or int(atomid4) in atomid_list):
#                    print atomid1
                    ind_list.append(int(items.split()[-1]))

    if key=="cmap":
        for items in value:
            if len(items.split())>=5:
                atomid1=items.split()[0]
                atomid2=items.split()[1]
                atomid3=items.split()[2]
                atomid4=items.split()[3]
                atomid5=items.split()[4]
                if atomid1.isdigit() and atomid2.isdigit() and atomid3.isdigit() and atomid4.isdigit() and atomid5.isdigit() and ((int(atomid1) in atomid_list) or int(atomid2) in atomid_list or int(atomid3) in atomid_list or int(atomid4) in atomid_list or int(atomid5) in atomid_list):
#                    print atomid1
                    ind_list.append(int(items.split()[-1]))

f=open(output,'w')                    
for index in range(len(lines)):
    if index in ind_list:
        continue
    else:
        f.write(lines[index])
                    
    

print atomid_list
print ind_list

    

