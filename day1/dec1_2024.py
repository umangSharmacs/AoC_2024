l1 = []
l2 = []
with open('/Users/umangsharma/Documents/GitHub/AoC_2024/day1/inp.txt',"r") as f:
    a = f.readlines()
    # print(a)
for i in a:
    l1.append(int(i.split(' ')[0]))
    l2.append(int(i.split(' ')[3].split('\n')[0]))
l1.sort()
l2.sort()
sum = 0

l1_dict = {}
l2_dict = {}
for i,j in zip(l1,l2):
    if i in l1_dict:
        l1_dict[i]+=1
    else:
        l1_dict[i]=1

    if j in l2_dict:
        l2_dict[j]+=1
    else:
        l2_dict[j]=1 

score = 0
for k,v in l1_dict.items():
    if k in l2_dict:
        score+=k*l2_dict[k]*v
print(score)
