number_array = [19740, 17947, 17926, 17273, 17593, 17931]
probabilities = [1.0,1.0,1.0,0.75,0.5,0]
    
exp = 0
for x in range(6):
    exp = exp + 2* number_array[x]*probabilities[x]

print(exp)