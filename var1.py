#task 1
########################################
def generate_matrix(n, m):
    matrix = [[0]*n for i in range(m)]
    nums = [i for i in range(1, m*n+1)]
    n_value = n
    m_value = m
    ind = 0
    i = 0
    j = -1
    direction = 1
    while ind != len(nums):
        j += 1
        for k in range(j, n_value+j):
            if ind == len(nums):
                return matrix
            j = k
            matrix[i][j] = nums[ind]
            ind += 1
        m_value -= 1
        i += direction
        for p in range(i, m_value+i):
            if ind == len(nums):
                return matrix
            i = p
            matrix[i][j] = nums[ind]
            ind += 1
        direction *= -1
        n_value -= 1
        for k in range(j-1, j-n_value-1, -1):
            if ind == len(nums):
                return matrix
            j = k
            matrix[i][j] = nums[ind]
            ind += 1
        i += direction
        m_value -= 1
        for p in range(i, abs(m_value-i), -1):
            if ind == len(nums):
                return matrix
            i = p
            matrix[i][j] = nums[ind]
            ind += 1
        direction *= -1
        n_value -= 1
    return matrix

m = generate_matrix(3, 3)
for r in m:
    print(r)
########################################

#task 2
########################################
def task_2(strs = []):
    max_len = 0
    condition = True
    answ = ""
    if strs == []:
        while condition:
            st = input().lower()
            if st == "stop":
                condition = False
                break
            unique_symbols = set()
            for c in st:
                unique_symbols.add(c)
            if max_len < len(unique_symbols):
                max_len = len(unique_symbols)
                answ = st
        return f"{answ} - {max_len}"

#print(task_2())
########################################

#task 5
########################################
def task_5():
    nums = [int(i) for i in input().split()]
    k = int(input())
    if k <= 0:
        raise ValueError("Incorrect K value given")
    avgs = []
    for i in range(len(nums)-(k-1)):
        window = []
        for j in range(k):
            window.append(nums[i+j])
        avgs.append(sum(window)//len(window))
    return avgs

def generate_values_for_task5():
    from random import randint
    nums = [randint(1, 99) for i in range(randint(1, 20))]
    return (sorted(nums), randint(1, 20))
#print(task_5())
########################################

#task 3
########################################
def task_3():
    nums = [int(q) for q in input().split()]
    if not nums:
        return []
    new_nums = []
    current = None
    for n in nums:
        if current != n:
            current = n
            new_nums.append([n, 1])
        else:
            new_nums[-1][1] += 1
    return new_nums

#x = task_3()
#print(x)

def task_3_reverse(nums):
    new_nums = []
    for pair in nums:
        for i in range(pair[1]):
            new_nums.append(pair[0])
    return new_nums

#print(task_3_reverse(x))
########################################


#task 4
########################################
from random import randint

def heuristic(point1, point2):
    x1, y1 = point1
    x2, y2 = point2
    return (x1 - x2)**2 + (y1 - y2)**2

def task_4(vertices, center):
    min_dist = float("inf")
    point = None
    for v in vertices:
        d = heuristic(v, center)
        if d < min_dist:
            min_dist = d
            point = v
    return ((min_dist)**0.5, point)
        
test_data = [(randint(0, 50), randint(0, 50)) for i in range(10)]
test_center = (2, 2)

#print("\n", test_center)

#print(task_4(test_data, test_center))
########################################