with open("day4/inp.txt","r") as f:
    inp = f.read()

inp = [list(i) for i in inp.split('\n') ]

c = len(inp[0])
r = len(inp)

directions = {
    "N": (-1,0), "NE": (-1,1),"E":(0,1), "SE": (1,1), "S": (1,0), "SW": (1,-1), "W":(0,-1),"NW":(-1,-1)
}

x_list = []

# get 'x indices:
for i in range(r):
    for j in range(c):
        if inp[i][j]=='X':
            x_list.append((i,j))

# get 'a' indices 
a_list = []
for i in range(r):
    for j in range(c):
        if inp[i][j]=='A':
            a_list.append((i,j))
 
def dist(p1,p2):
    x1,x2 = p1
    y1,y2 = p2
    return abs(x1-x2)+abs(y1-y2)

def check_xmas_p1(centre, inp, r,c):

    ans = 0
    for direction in directions:
        if direction == 'N':
            if centre[0]<3:
                continue 
        if direction == 'NE':
            if centre[1]>=(c-3) or centre[0]<3:
                continue 
        if direction == 'E':
            if centre[1]>=(c-3):
                continue
        if direction == 'SE':
            if centre[1]>=(c-3) or centre[0]>=(r-3):
                continue
        if direction == 'S':
            if centre[0]>=(r-3):
                continue
        if direction == 'SW':
            if centre[1]<(3) or centre[0]>=(r-3):
                continue
        if direction == 'W':
            if centre[1]<(3):
                continue 
        if direction == 'NW':
            if centre[1]<(3) or centre[0]<3:
                continue 
        
        check = ['M' , 'A', 'S']
        correct = True
        for i in range(1,4):
            
            new_x = centre[0] + (i*directions[direction][0])
            new_y = centre[1] + (i*directions[direction][1])
            # print(direction, new_x, new_y, inp[new_x][new_y])
            if inp[new_x][new_y] !=check[i-1]:
                correct = False
        if correct:
            ans+=1 
            # print(centre)
    return ans 


def check_xmas_p2(centre, inp, r,c):
    if centre[0]==0 or centre[0]==c-1 or centre[1]==0 or centre[1]==r-1:
        return 0 
    
    left_diag =  True 
    right_diag = True
    
    if not (inp[centre[0]-1][centre[1]-1]=='M' and inp[centre[0]+1][centre[1]+1]=='S') and not (inp[centre[0]-1][centre[1]-1]=='S' and inp[centre[0]+1][centre[1]+1]=='M'):
        return 0 
    if not (inp[centre[0]+1][centre[1]-1]=='M' and inp[centre[0]-1][centre[1]+1]=='S') and not (inp[centre[0]+1][centre[1]-1]=='S' and inp[centre[0]-1][centre[1]+1]=='M'):
        return 0 
    return 1

# print(check_xmas(centre=(0,5), inp=inp, r=r, c=c))
ans = 0
for centre in x_list:
    ans+=check_xmas_p1(centre=centre, inp=inp, r=r, c=c)

ans_p2 = 0
# print(r,c)
for centre in a_list:
    # print(centre)
    ans_p2+=check_xmas_p2(centre=centre, inp=inp, r=r, c=c)
print("Part 1 :", ans)
print("Part 2 :", ans_p2)