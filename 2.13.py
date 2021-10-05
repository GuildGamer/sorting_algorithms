"""
A simple linear search algorithm
"""

def l_search(i, arr):
    p = 0
    while p < len(arr) and arr[p] != i:
        p = p+1
    if p >= len(arr):
        return None
    else:
        return p
        
    '''
    for e in range(0, len(arr)):
        if arr[e] == i:
            return e
    '''
            
print(l_search(0,[3,2,4,1]))
        
