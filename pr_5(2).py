#13
line="fcgvhjbyvjv(hjgkhkhjkbj)kjhlkljjbbhjk"
cut_1=0
cut_2=0
for i in range(len(line)):
    if line[i]=="(":
        cut_1=i
    if line[i]==")":
        cut_2=i

print(line[cut_1+1:cut_2])
            

        

