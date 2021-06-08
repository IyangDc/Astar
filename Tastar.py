import time
import copy
# shape of the Map
m = 15
n = 15
A={'x':3,'y':6}
B={'x':13,'y':3}
ite = 0
# Init the Map
Map = []
for i in range(n):
    Map.append([])
    for j in range(m):
        Map[i].append(0)
# Init A.
Map[A['x']][A['y']] = 200
# Init B.
Map[B['x']][B['y']] = 300
# Init barrier.
Map[5][7] = 100
Map[5][8] = 100
Map[5][4] = 100
Map[4][3] = 100
Map[5][3] = 100
Map[3][3] = 100
Map[2][3] = 100
Map[5][5] = 100
Map[5][6] = 100
Map[5][8] = 100
Map[4][8] = 100
Map[3][8] = 100
Map[2][8] = 100
Map[5][6] = 100
# Init open list.
open_list = [[(A['x'],A['y'])]]
# Init close list.
close_list = []
# Init direction knowledge.
pos = [(0,-1),(0,1),(-1,0),(1,0),(-1,-1),(-1,1),(1,1),(1,-1)]
# Cal cost from current point to next point.
def cal_g(pos):
    if pos == 1:
        return 10
    if pos == 2:
        return 10
    if pos == 3:
        return 10
    if pos == 4:
        return 10
    if pos == 5:
        return 14
    if pos == 6:
        return 14
    if pos == 7:
        return 14
    if pos == 8:
        return 14
# Cal the cost from next point to B.
def cal_h(cur,B):
    dx = abs(cur[0]-B['x'])
    dy = abs(cur[1]-B['y'])
    return min(dx,dy)*14+abs(dx-dy)*10
# Cal total cost.
def cal_f(g,h):
    f = g+h
    return f
# flag at whether found B
flag = False
if __name__ == '__main__':
    while open_list is not None:
        # times of iteration
        ite+=1
        # Pop the first poin of open list
        point = open_list.pop(0)
        # Check the 8 pixel
        for i in range(8):
            if Map[point[0][0]+pos[i][0]][point[0][1]+pos[i][1]] == 0: # walkable or not
                new_point=[(point[0][0]+pos[i][0],point[0][1]+pos[i][1])]
                new_point.append(i+1)
                new_point.append(cal_f(cal_g(i+1),cal_h((point[0][0]+pos[i][0],point[0][1]+pos[i][1]),B)))
                open_list.append(new_point)
            elif Map[point[0][0]+pos[i][0]][point[0][1]+pos[i][1]] == 300:
                flag = True
                close_list.append(point[0])
                close_list.append((B['x'],B['y']))
                break
        if flag:
            break
        # Sort the open list by f()
        open_list.sort(key=lambda ls:ls[2])
        if point[0] not in close_list:
            close_list.append(point[0])
            pass
        else:
            # The point was been arrived. Not alowed to arrive
            Map[point[0][0]][point[0][1]] = 101 
        if ite >= n*m:
            raise OverflowError("Iteration times up to MAX. Check your map!")
    print "Route found."
    print "Iterations: " + "{}".format(ite)
    print "Route:"
    print close_list
    print("-------------------------------------------------------------")
    Mapb=copy.deepcopy(Map)
    for point in close_list:
        Mapb[point[0]][point[1]]= "*"
    Mapb[A['x']][A['y']] = 'A'
    Mapb[B['x']][B['y']] = 'B'
    Map[A['x']][A['y']] = 'A'
    Map[B['x']][B['y']] = 'B'
    for raw in Mapb:
        for col in raw:
            print "{:^3}".format(col),
        print('\r')
    print("-------------------------------------------------------------")
    for raw in Map:
        for col in raw:
            print "{:^3}".format(col),
        print('\r')
    print("-------------------------------------------------------------")        