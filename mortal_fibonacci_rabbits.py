n = 88                                                                         
m = 17                                                                       
offsprings = [1, 1]                                                               
months = 2                                                                     
while months < n:                                                              
    if months < m:                                                             
        offsprings.append(offsprings[-2] + offsprings[-1])                              
    elif months == m:                                        
        offsprings.append(offsprings[-2] + offsprings[-1] - 1)                          
    else:                                                                      
        offsprings.append(offsprings[-2] + offsprings[-1] - offsprings[-(                  
            m + 1)])                                                           
    months += 1                                                                
print(offsprings[-1])    