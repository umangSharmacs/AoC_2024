with open("day10/inp.txt") as f:
    inp = f.read()

grid = [list(map(int,list(i))) for i in inp.split('\n')]
# for i in grid:
#     print(i)

# Get 0 pos 
r,c = len(grid), len(grid[0])
pos_0 = []
for i in range(r):
    for j in range(c):
        if grid[i][j]==0: 
            pos_0.append((i,j))

def bfs(begin, grid):
    r,c = len(grid), len(grid[0])

    visited = set()
    queue = [begin]

    ans = 0
    while len(queue)>0:

        curr_x,curr_y = queue.pop(0)
        curr = grid[curr_x][curr_y]
        if curr == 9 and (curr_x,curr_y) not in visited:
            ans+=1

        if (curr_x, curr_y) in visited:
            continue
        visited.add((curr_x,curr_y))
        

        #add children to qeueu 
        if curr_x-1>=0 and grid[curr_x-1][curr_y]==curr+1:
            queue.append((curr_x-1,curr_y))
        if curr_x+1<r and grid[curr_x+1][curr_y]==curr+1:
            queue.append((curr_x+1,curr_y))
        if curr_y-1>=0 and grid[curr_x][curr_y-1]==curr+1:
            queue.append((curr_x, curr_y-1))
        if curr_y+1<c and grid[curr_x][curr_y+1]==curr+1:
            queue.append((curr_x, curr_y+1))

    return ans 


def bfs_part2(begin, grid):
    r,c = len(grid), len(grid[0])

    visited = set()
    queue = [[begin]]

    ans = []
    while len(queue)>0:
        # print(queue)
        path = queue.pop(0)
        curr_x,curr_y = path[-1]
        curr = grid[curr_x][curr_y]
        # print(curr)

        if curr == 9:
            ans.append(path)

        # if (curr_x, curr_y) in visited:
        #     continue
        
        visited.add((curr_x,curr_y))
        
        # print(curr_x+1,curr_y, grid[curr_x+1][curr_y], r)
        #add children to qeueu 
        if curr_x-1>=0 and grid[curr_x-1][curr_y]==curr+1:
            # print('up')
            # path.append((curr_x-1,curr_y))
            queue.append(path[::]+[(curr_x-1,curr_y)])
        if curr_x+1<r and grid[curr_x+1][curr_y]==curr+1:
            # print('down')
            # path.append((curr_x+1,curr_y))
            queue.append(path[::]+[(curr_x+1,curr_y)])
        if curr_y-1>=0 and grid[curr_x][curr_y-1]==curr+1:
            # print('left')
            # path.append((curr_x, curr_y-1))
            queue.append(path[::]+[(curr_x,curr_y-1)])
        if curr_y+1<c and grid[curr_x][curr_y+1]==curr+1:
            # print('right')
            # path.append((curr_x, curr_y+1))
            queue.append(path[::]+[(curr_x,curr_y+1)])

    return ans

def part1(pos_0, grid):
    ans = 0
    for pos in pos_0:
        # print(pos,bfs(pos, grid))
        ans+=bfs(pos, grid)
    return ans 

def part2(pos_0, grid):
    ans = 0
    for pos in pos_0:
        ans+=len(bfs_part2(pos,grid))
    return ans 

part_2 = part2(pos_0,grid)
print(part_2)
