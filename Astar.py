import time
#Shape of the Map
m = 15
n = 15
A={'x':3,'y':6}
B={'x':13,'y':3}
 

Map = []
#init the Map
for i in range(n):
    Map.append([])
    for j in range(m):
        Map[i].append(0)
#Init A
Map[A['x']][A['y']] = 200
#init B
Map[B['x']][B['y']] = 300
#init barrier
Map[5][7] = 100
Map[5][8] = 100
Map[5][3] = 100
Map[5][4] = 100
Map[5][5] = 100
Map[5][6] = 100
flag = 0
queue = []
route_queue = []
queue.append((A['x'],A['y']))
ite = 0
while queue is not None:
    ite += 1
    try:
        point = queue.pop(0)
        if point[0]-1>=0 :
            queue.append((point[0]-1,point[1]))
            if Map[point[0]-1][point[1]] == 0 :
                Map[point[0]-1][point[1]] = 1
            elif Map[point[0]-1][point[1]] == 300:
                route_queue.append((point[0]-1,point[1]))
                break 
            
        if min(point[0]+1,point[1])>=0 :    
            if Map[point[0]+1][point[1]] == 0 :
                Map[point[0]+1][point[1]] = 2
                queue.append((point[0]+1,point[1]))
            elif Map[point[0]+1][point[1]] == 300:
                route_queue.append((point[0]+1,point[1]))
                break 

        if point[1]-1>=0 :
            if Map[point[0]][point[1]-1] == 0 :
                Map[point[0]][point[1]-1] = 3
                queue.append((point[0],point[1]-1))
            elif Map[point[0]][point[1]-1] == 300:
                route_queue.append((point[0],point[1]-1))
                break 

        if min(point[0],point[1]+1)>=0 :
            if Map[point[0]][point[1]+1] == 0 :
                Map[point[0]][point[1]+1] = 4
                queue.append((point[0],point[1]+1))
            elif Map[point[0]][point[1]+1] == 300:
                route_queue.append((point[0],point[1]+1))
                break
    except Exception:
        pass

#print(Map)
print("----------------------------")
for raw in Map:
    print(raw)
print(point)
print("----------------------------")


#find the route

if Map[route_queue[-1][0]+1][route_queue[-1][1]]!=0:
    route_queue.append((route_queue[-1][0]+1,route_queue[-1][1]))
elif Map[route_queue[-1][0]-1][route_queue[-1][1]]!=0:
    route_queue.append((route_queue[-1][0]-1,route_queue[-1][1]))
elif Map[route_queue[-1][0]][route_queue[-1][1]+1]!=0:
    route_queue.append((route_queue[-1][0]+1,route_queue[-1][1]))
elif Map[route_queue[-1][0]][route_queue[-1][1]-1]!=0:
    route_queue.append((route_queue[-1][0]+1,route_queue[-1][1]))

while True:
    bit_state = Map[route_queue[-1][0]][route_queue[-1][1]]
    if bit_state==200:#reach A
        break
    Map[route_queue[-1][0]][route_queue[-1][1]] = '*'
    if bit_state==1:
        route_queue.append((route_queue[-1][0]+1,route_queue[-1][1]))
    if bit_state==2:
        route_queue.append((route_queue[-1][0]-1,route_queue[-1][1]))
    if bit_state==3:
        route_queue.append((route_queue[-1][0],route_queue[-1][1]+1))
    if bit_state==4:
        route_queue.append((route_queue[-1][0],route_queue[-1][1]-1))
print("----------------------------")
for raw in Map:
    print(raw)
print(point)
print("----------------------------")
print(route_queue)
