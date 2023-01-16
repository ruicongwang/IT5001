
def createZeroMatrix(n,m):
    return [[0 for i in range(m)] for j in range(n)]

def mTightPrint(m):
    for i in range(len(m)):
        line = ''
        for j in range(len(m[0])):
            line += str(m[i][j])
        print(line)
        
def PDMap(r,c,sites):
    result = createZeroMatrix(r,c)
    for i in range(r):
        for j in range(c):
            distance_square_list = []
            for k in sites:
                distance_square = (i - k[0])**2 + (j - k[1])**2
                distance_square_list.append(distance_square)
            min_number = min(distance_square_list)
            index_list = []
            for index, number in enumerate(distance_square_list):
                if number == min_number:
                    index_list.append(index)
            if len(index_list) > 1:
                result[i][j] = 'X'
            else:
                result[i][j] = index_list[0]
    return result

mTightPrint(PDMap(50,80,[[20,10], [30,30],[40,20],[45,55],[10,55],[35,70],[35,60]]))
# mTightPrint(PDMap(10,10,[[2,3],[4,9],[7,2]]))

# mTightPrint(PDMap(60,70,[[10,20],[30,20],[40,50]]))
# ex = PDMap(60,70,[[10,20],[30,20],[40,50]])
    
