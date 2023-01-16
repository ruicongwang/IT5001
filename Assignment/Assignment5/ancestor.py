parent = {'Amy':'Ben', 'May':'Tom', 'Tom':'Ben',
          'Ben':'Howard', 'Howard':'George', 'Frank':'Amy',
            'Joe':'Bill', 'Bill':'Mary', 'Mary':'Philip', 'Simon':'Bill',
          'Zoe':'Mary'}


def is_ancestor(name1,name2,parent): # check if name1 is an ancestor of name2
    ancestor_list = []
    current = name2
    while current in parent.keys():
        ancestor_list.append(parent[current])
        current = parent[current]
    if name1 in ancestor_list:
        return True
    else:
        return False


def is_related(name1,name2,parent):
    ancestor_list1 = [name1]
    current = name1
    while current in parent.keys():
        ancestor_list1.append(parent[current])
        current = parent[current]
    ancestor_list2 = [name2]
    current = name2
    while current in parent.keys():
        ancestor_list2.append(parent[current])
        current = parent[current]
    result = False
    for i in ancestor_list1:
        if i in ancestor_list2:
            result = True
    return result

print("Is Mary an ancestor of Simon?")
print(is_ancestor('Mary','Simon',parent))
print("Is Zoe an ancestor of Joe?")
print(is_ancestor('Zoe','Joe',parent))
print()


print("Is Joe is_related to Philip?")
print(is_related('Joe','Philip',parent))
print("Is Amy is_related to May?")
print(is_related('Amy','May',parent))
print("Is Amy is_related to Philip?")
print(is_related('Amy','Philip',parent))    
print()


parent['Ben']='Philip' #modify the dictionary so that Philip is Ben's parent
print("After Philip became Ben\'s parent...")
print("Is Amy is_related to Philip?")
print(is_related('Amy','Philip',parent))

