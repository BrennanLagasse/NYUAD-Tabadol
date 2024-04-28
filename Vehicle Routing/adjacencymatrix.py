def init_mat(size):
    matrix = []
    for i in range(size):
        row = []
        for j in range(size):
            row.append(0)
        matrix.append(row)
    
    return matrix

file = open("graph.csv", "r")

nameNodeMap = dict()
last_idx = 0


for line in file:
    edge = line.strip().split(",")
    print(edge)
    if(edge[0] not in list(nameNodeMap.keys())):
        nameNodeMap[edge[0]]=last_idx
        last_idx = last_idx + 1
    
    if(edge[1] not in list(nameNodeMap.keys())):
        nameNodeMap[edge[1]]=last_idx
        last_idx = last_idx + 1
print(nameNodeMap)

for key in nameNodeMap.keys():
    print(key,nameNodeMap[key])
        
adjmatrix = init_mat(last_idx)

file2 = open("graph.csv", "r")

for line in file2:
    edge = line.strip().split(",")
    adjmatrix[int(nameNodeMap[edge[0]])][int(nameNodeMap[edge[1]])] = int(edge[2])
    adjmatrix[int(nameNodeMap[edge[1]])][int(nameNodeMap[edge[0]])] = int(edge[2])
    
for row in range(len(adjmatrix)):
    for column in range(len(adjmatrix[0])):
        print(adjmatrix[row][column],end =" ")
    print()