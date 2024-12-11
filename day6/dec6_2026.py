from copy import deepcopy

with open("day6/inp.txt") as f:
    inp = f.read()

grid = []
for i in inp.split('\n'):
    grid.append(list(i))

begin = (0,0)
r ,c= len(grid), len(grid[0])
for i in range(r):
    for j in range(c):
        if grid[i][j]=='^':
            begin = (i,j)

print(begin)

directions = { '^' : (-1,0), '>': (0,1), 'v':(1,0),'<':(0,-1) }

next_direction = ['^', '>', 'v', '<']



def part1(grid, centre):
    ans = 1
    x,y = centre[0], centre[1]
    curr = 0
    visited = set()
    counter = 0
    while True:
        # print("="*20)
        # for g in grid:
            # print(g)
        dx = directions[grid[x][y]][0]
        dy = directions[grid[x][y]][1]
        if 0<=(x+dx)<r and 0<=(y+dy)<c:
            state = ((x,y) , grid[x][y])
            # print(len(visited))
            # if state not in visited:
            #     visited.add(state)
            # else:
            #     visited.remove(state)
            # if len(visited)==0:
            #     return "CYCLE"
            
            new_x = x+dx
            new_y = y+dy
            # print(new_x,new_y)
            if grid[new_x][new_y]=='#':
                if counter==3:
                    if state in visited:
                        return 'CYCLE'
                
                counter+=1
                counter = counter%4
                visited.add(state)
                curr = (curr+1)%4
                grid[x][y] = next_direction[curr]
                continue
            elif grid[new_x][new_y]=='.' or grid[new_x][new_y]=='X':
                if grid[new_x][new_y]=='.':
                    ans+=1
                grid[new_x][new_y] = grid[x][y]
                grid[x][y]='X'
                x,y = new_x, new_y
                continue
        else:
            break 
    return ans

def part2(grid, centre):
    ans = 0
    r ,c= len(grid), len(grid[0])
    for i in range(r):
        for j in range(c):
            if grid[i][j]=='^' or grid[i][j]=='#':
                continue
            new_grid = deepcopy(grid)
            new_grid[i][j] = '#'
            # for g in new_grid:
            #     print(g)
            print(i,j)
            if part1(new_grid, centre)=='CYCLE':
                ans+=1
            
    return ans 

# print(f"{part1(grid, begin)=}")
print(f"{part2(grid, begin)=}")







