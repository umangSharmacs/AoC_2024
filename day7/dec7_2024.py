import itertools
from copy import deepcopy

with open("day7/inp.txt") as f:
    inp = f.read()

# parse 
eqns = {}
for i in inp.split('\n'):
    test_val = int(i.split(':')[0])
    nums = [int(j) for j in i.split(':')[1].split(' ') if j!=''] 
    eqns[test_val] = nums 

print(eqns)

operations = ['+', '*']

def evaluate(nums, res, operations):
    options = len(nums)-1 
    combinations = list(itertools.product(operations, repeat=options))
    for comb in combinations:
        temp = deepcopy(nums)
        for op in comb:
            # print(op)
            a = temp.pop(0)
            b = temp.pop(0)
            # print(a,b)
            if op=='+':
                # print(a+b)
                temp.insert(0,a+b)
                # print(temp)
            elif op=='*':
                temp.insert(0,a*b,)
            elif op=='||':
                temp.insert(0,int(str(a)+str(b)))
            # print(temp)
        if temp[0]==res:
            return True
    return False

def part1(eqns):
    operations_p1 = ['+', '*']
    ans = 0
    for k,v in eqns.items():
        # print(k,v)
        if evaluate(nums = v, res = k, operations=operations_p1):
            ans+=k
    return ans


def part2(eqns):
    operations_p2 = ['+', '*', '||']
    ans = 0
    for k,v in eqns.items():
        # print(k,v)
        if evaluate(nums = v, res = k, operations=operations_p2):
            ans+=k
    return ans


# print(len(eqns.keys()))

print(f"{part1(eqns=eqns)=}")
print(f"{part2(eqns=eqns)=}")





    
