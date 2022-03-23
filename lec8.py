def my_function(a,b=0):
    result = a + b
    
    print(a)
    return result

    print(b)
   
#print ( my_function(1))

#print(a)
# ^ does not work, it is outside of the function

#ex1

def cal_abs(a):
    if type(a) is str:
        return "wrong data type"
    elif a >=0:
        return a
        
        
    else:
        return -a
        
print(cal_abs(0))

#ex2

def cal_sigma(n,m):
    
    result = 0

    for i in range(n,m+1):
    
     result = result + i
    
    print(result)
    
print(cal_sigma(1,6))

def cal_pi(n,m):

    result = 1
    
    for i in range(n,m+1):
        
        result = result * i
        
    return(result)
print(cal_pi(1,6))

#ex3
def cal_f(m):
    if m ==0:
        return 1
    else:
        return m * cal_f(m-1)
print(cal_f(5))


def cal_p(m,n):
    return cal_f(m)/cal_f(m-n)
    
print(cal_p(5,3))