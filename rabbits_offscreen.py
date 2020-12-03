def Loop_Rabbit(months, offspring):
    parent, child = 1,1
    for itr in range(months -1):
        child, parent = parent, parent + (child * offspring)
    
    return child

print(Loop_Rabbit(35,5))