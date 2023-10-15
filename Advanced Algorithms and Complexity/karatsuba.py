def karatsuba(x,y):
  n = max(len(str(x)),len(str(y)))   #determine which number has highest decimal places
  if n == 1:
    return x*y                        #if both numbers are single digit then directly multiply and return answer

  n2 = n // 2                          #either 0 or 1: 

  x1 = x // (10**n2)                   #512//10 = 51
    
  x2 = x % (10**n2)                     #512%10 = 2
  
  y1 = y // (10**n2)                    #12//10 = 1

  y2 = y % (10**n2)                     #12%10 = 2


  p1 = karatsuba(x1, y1)
  p2 = karatsuba(x2, y2)
  p3 = karatsuba(x1+x2, y1+y2) - p1 - p2

  return p1 * 10**(2*n2) + p3 * (10**n2) + p2

print(512*12)
print(karatsuba(512, 12))