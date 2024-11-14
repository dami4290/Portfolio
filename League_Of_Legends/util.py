import csv
import os 
dir=sorted(os.listdir("data"))
print(dir)
my_list=[]
for name in dir:
    with open(("data/"+name), "r") as f:
        #print(f.readlines())
        for line in f.readlines():
            line.replace(";",",")
            my_list.append(line.replace(";",","))      
with open("league.csv","w") as f:
    f.writelines(my_list)