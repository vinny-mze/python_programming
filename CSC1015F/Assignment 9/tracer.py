print('***** Program Trace Utility ****')
prog=input('Enter the name of the program file: ')
f=open(prog,'r')
r=f.readlines()
f.close()
x=[]
set=0
for i in r:
    if '"""DEBUG"""' in i:
        set=1
        continue
    else:
        i=i.strip('\n')
        x=x+[i]
            
if set==0:
    x=[]
    r=['"""DEBUG"""']+r
    for line in r:
        line=line.strip('\n')
        if 'def' in line:
            x=x+[line]+['    """DEBUG""";print(\''+line[4:line.find('(')]+'\')']
        else:
            x=x+[line]     
f=open(prog,'w')
for item in x:
    print(item,file=f)
f.close()
