#Allocate a new memory of size 'size'
def allocateMemory(size):
    assert size >=1
    return [0]*size

#Copy the contents of old list into new
def copyInto(old, new):
    assert len(old) <= len(new), 'Not enough space to copy into'
    m = len(old)
    for i in range (m):
        new[i] = old[i]

#Running Examples
array1 = ["harsh",'vardhan','saxena',6,7,7]
array2 = allocateMemory(6)

copyInto(array1, array2)
print(array2)


class DynamicArray:
    def __init__(self, initial_size=16, initial_fill=0, debug=False):
        self.allocated_size = initial_size
        self.size = 0
        self.array = [initial_fill] * initial_size
        self.debug = debug

    # This allows us to directly access d[idx] 
    def __getitem__(self, idx):
        assert idx >= 0 and idx < self.size
        return self.array[idx]

    # This allows us to write d[idx] = val
    def __setitem__(self, idx, val):
        assert idx >= 0 and idx < self.size 
        self.array[idx] = val

    # please complete this function
    def append(self, x):
        y = self.size
        if y<self.allocated_size and y>=0:
            self.array[y] = x
            self.size= self.size+1
        elif y==self.allocated_size:                     #DOUBT   
            self.allocated_size = self.allocated_size+1  #DOUBT: allocated_size NOT INCREASING ON DEMAND
            self.array[y] = x                            #DOUBT
            self.size= self.size+1                       #DOUBT
        else:
            print("error in appending!!")

l = DynamicArray(initial_size=500, initial_fill=0, debug=True)

for j in range(500):
    l.append(j)
print(f' l[10] = {l[10]}')
l[0] = 30
print(f' l[0] = {l[0]}')

print("allocated size of array = " , l.allocated_size)
print("size of array = " , l.size)
# print("vlaue = " , l[0])
# print("vlaue = " , l[1])
# print("vlaue = " , l[2])

