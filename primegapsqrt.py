def is_prime(num):
    for i in range(2, int(num**0.5)):
        if num % i == 0:
            return False
        
    return True
    
def next_prime(num):
    for i in range(num+1,9999999999999999999999999):
        if is_prime(i):
            return i
        
    return 0




def meets_the_conjecture(x, y):   
    return (((y))**0.5) - (((x))**0.5) < 1
  
  
i = 0
p_1 = 2
p_2 = 3

while True:
    i = i+1

    if meets_the_conjecture(p_1, p_2):
        #if i % 100 == 0:
        print(p_1)
        print(p_2)
    else: 
        print("False")
        print(p_1)
        break        
    
    p_1 = p_2
    p_2 = next_prime(p_2)
    if p_2 == 0:
        print("done")
        break
        
    
    