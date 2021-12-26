import re
import sys
import subprocess

filename=sys.argv[1];
filename_gro=sys.argv[2];
filename_pores=sys.argv[3];
seq=sys.argv[4];

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
    if categ=="atoms" and lines[index][0]!=";":
        try:
            d1[categ].append(lines[index].strip()+" "+str(index))
        except KeyError:
            d1[categ]=[lines[index].strip()+" "+str(index)]

value=d1["atoms"];
start=int(value[1].split()[0]);
end=int(value[-2].split()[0]);

for items in value:
    if len(items.split())>=3:
        resid=items.split()[2]
        if resid.isdigit() and int(resid)==10+len(seq)-2:
            end_gro=int(items.split()[0])-1
            break;


print './shift.sh %s %d %d' % (filename,start,end)
rc=subprocess.Popen(['./shift.sh %s %d %d' % (filename,start,end)],shell=True)
rc.wait()
ree0=subprocess.Popen(['cp %s %s' % (filename_gro,filename_gro+"1")],shell=True)
ree0.wait()
print 'awk \'{if ($3>=%d && $3<=%d) print $0}\' %s > %s' % (start,end_gro,filename_gro+"1",filename_gro)
ree1=subprocess.Popen(['awk \'{if (($3>=%d && $3<=%d)||NR<3) print $0}\' %s > %s' % (start,end_gro,filename_gro+"1",filename_gro)],shell=True)
ree1.wait()
print 'sed -i \'2s/.*/%d/\' %s' % (end_gro-start+1,filename_gro)
ree2=subprocess.Popen(['sed -i \'2s/.*/%d/\' %s' % (end_gro-start+1,filename_gro)],shell=True)
ree2.wait()
ree3=subprocess.Popen(['./shift.sh %s %d %d' % (filename_gro,start,end_gro)],shell=True)
ree3.wait()
rf0=subprocess.Popen(['cp %s %s' % (filename_pores,filename_pores+"1")],shell=True)
rf0.wait()
rf1=subprocess.Popen(['awk \'{if (($1>=%d && $1<=%d)||NR<8) print $0}\' %s > %s' % (start,end_gro,filename_pores+"1",filename_pores)],shell=True)
rf1.wait()
rf3=subprocess.Popen(['./shift.sh %s %d %d' % (filename_pores,start,end_gro)],shell=True)
rf3.wait()
f=open(filename,'r');
lines=f.readlines();
f.close();

categ="";
d2={};

for index in range(len(lines)):
    if categ=="atoms" and lines[index][0]=="[":        
        delete_ind_end=index;

    if lines[index][0]=="[":
        categ=lines[index].split()[1]
    if categ=="atoms" and lines[index][0]!=";":
        #print categ
        #print lines[index]
        try:
            d2[categ].append(lines[index].strip()+" "+str(index))
        except KeyError:
            d2[categ]=[lines[index].strip()+" "+str(index)]
#print d2
value=d2["atoms"]                
end=int(value[-2].split()[0]);
for items in value:
    if len(items.split())>=3:
        resid=items.split()[2]
        if resid.isdigit() and int(resid)==len(seq)-1:
            start=int(items.split()[0])
            delete_ind_start=int(items.split()[-1])
            break;
print start
print end
print './shift.sh %s %d %d' % (filename,start,end)
rd=subprocess.Popen(['./shift.sh %s %d %d' % (filename,start,end)],shell=True)
rd.wait()
print 'sed -i \'%d,%d d\' %s' % (delete_ind_start,delete_ind_end-1,filename)
rd1=subprocess.Popen(['sed -i \'%d,%d d\' %s' % (delete_ind_start,delete_ind_end-1,filename)],shell=True)
rd1.wait()
f=open(filename,'r')
lines=f.readlines();
d3={};
for index in range(len(lines)):
    if lines[index][0]=="[":
        categ=lines[index].split()[1]
        if categ=="cmap":
            add_map_end=index+3;            
    if categ=="cmap" and lines[index][0]!=";":
        if lines[index][0]=="#":
            break;
        try:
            d3[categ].append(lines[index].strip()+" "+str(index))
        except KeyError:
            d3[categ]=[lines[index].strip()+" "+str(index)]

value=d3["cmap"]
#print value
#print value[-2]
cmap_v1=int(value[-2].split()[3])
cmap_v2=int(value[-2].split()[4])
rg=subprocess.Popen(['sed -i \'%d i\t%d\t%d\t%d\t%d\t%d\t1\' %s' % (add_map_end,cmap_v1,cmap_v2,3,10,12,filename)],shell=True)
