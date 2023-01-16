d1 = {'D': 'W', '1': 'W', 'Z': 'W', 'C': 'T', '3': 'T', 'F': 'T', '0': '.', '2': '.', '4': '.', 'B': '^', '+': '^', ';': '^', 'Q': 'E', '7': 'E', '8': 'E', 'X': 'M', 'P': 'M', '!': 'M', '(': ':', ')': ':', '9': ':', '*': ' ', '|': ' ', '#': ' '}
d2 = {'C': 'W', '3': 'W', 'F': 'W', '0': 'T', '2': 'T', '4': 'T', 'B': '.', '+': '.', ';': '.', 'Q': '^', '7': '^', '8': '^', 'D': 'E', '1': 'E', 'Z': 'E', '(': 'M', ')': 'M', '9': 'M', '*': ':', '|': ':', '#': ':', 'X': ' ', 'P': ' ', '!': ' '}
        
def decode_map(mapfile,ddict,outfile):
    with open (mapfile, 'r') as read_file:
        result_list = []
        for line in read_file:
            line = line.rstrip('\n')
            result = []
            for str in line:
                if str in ddict.keys():
                    result.append(ddict[str])
                else:
                    result.append(str)
            result = ''.join(result)
            result_list.append(result)
    with open(outfile, 'w') as write_file:
        for write_str in result_list:
            write_file.write(write_str)
            write_file.write('\n')


def find_treasure(mapfile):
    with open(mapfile, 'r') as file:
        matrix = []
        for line in file:
            line = line.rstrip('\n')
            matrix.append(list(line))
    print(len(matrix))
    #Skip the first row and the last five rows
    for i in range(1,len(matrix)-5):
        # Skip the first and the last column
        for j in range(1,len(matrix[0])-1):
            if (matrix[i][j]=='T') and (matrix[i-1][j]=='T') and (matrix[i+1][j]=='T') and (matrix[i][j-1]=='T') and (matrix[i][j+1]=='T'):
                return (i,j)




print("Map 1")
decode_map('encoded_map.txt',d1,'decoded_map.txt')
print(find_treasure('decoded_map.txt'))

# Uncomment the following for your test cases

print("Map 2")
decode_map('encoded_map2.txt',d1,'decoded_map2.txt')
print(find_treasure('decoded_map2.txt'))

print("Map 3")
decode_map('encoded_map3.txt',d1,'decoded_map3.txt')
print(find_treasure('decoded_map3.txt'))

print("Map 5")
decode_map('encoded_map5.txt',d1,'decoded_map5.txt')
print(find_treasure('decoded_map5.txt'))

print("Map 1 B")
decode_map('encoded_mapB.txt',d2,'decoded_mapB.txt')
print(find_treasure('decoded_mapB.txt'))

