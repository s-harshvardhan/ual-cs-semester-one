class Item:
    def __init__(self, value, weight):
        self.value = value
        self.weight = weight
    def PWratio(self):
        return self.value/self.weight

def fractionalKnapsack(W,arr):
    max_val = 0
    ratioArr = [0] * len(arr)
    remainingW = 0
    
    for i in range(len(arr)):
        ratioArr[i] = arr[i].PWratio()
    
    ratioArr.sort(reverse = True)
    sortedArr = [0] * len(arr)
    
    for i in range(len(arr)):
        for j in range(len(arr)):
            if ratioArr[i] == arr[j].PWratio():
                sortedArr[i] = arr[j]
        
    for i in range(len(sortedArr)):
        if W <=0:
            break
        elif sortedArr[i].weight <= W:
            max_val += sortedArr[i].value
            W = W - sortedArr[i].weight
            print('*')
            print(max_val, W, sortedArr[i].weight)
        elif sortedArr[i].weight > W:
            max_val += sortedArr[i].value * (W/sortedArr[i].weight)
            W = W - (W/sortedArr[i].weight)*sortedArr[i].weight
            print('!')
            print(max_val, W, W/sortedArr[i].weight)

    return max_val
        
Total_Weight = 75       
arr = [Item(60, 10), Item(100, 20), Item(120, 30), Item(30, 15), Item(80, 25), Item(40, 15)]
max_val = fractionalKnapsack(Total_Weight, arr)
print(max_val)