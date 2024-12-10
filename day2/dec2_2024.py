

with open("/Users/umangsharma/Documents/GitHub/AoC_2024/day2/inp.txt" , "r") as f:
    inp = f.read()

ans = 0

MAX = 3
MIN = 1

def is_safe(rep):
    if rep[0]-rep[1]>0:
        increasing_flag = False
    elif rep[0]-rep[1]<0:
        increasing_flag = True
    else:
        return False
    print(f"{rep=},{increasing_flag=}")

    chance = True
    correct = True 
    for index in range(0,len(rep)-1):
        if increasing_flag:
            if (-1*MAX ) <= rep[index]-rep[index+1] <= (-1*MIN) : 
                continue 
            else:
                correct=False
                break

        elif not increasing_flag:
            if MIN<=rep[index]-rep[index+1]<=MAX:
                continue 
            else:
                correct=False
                break
    if correct:
        return True 
    else:
        return False

for line in inp.split('\n'):
    rep = [int(i) for i in line.split(' ')]

    if is_safe(rep):
        ans+=1
    else:
        for i in range(len(rep)):
            new_rep = rep[:i]+rep[i+1:]
            if is_safe(new_rep):
                ans+=1
                break
print(ans)    
                
                 
