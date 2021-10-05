from random import randint
from typing import runtime_checkable

def i_sort(arr):
    #we set our range of values of j to all values each index in the array except the first index
    for j in range(1,len(arr)):
        #key has been set to the value within the current index j
        key = arr[j]
        #i has been set to the index before j
        i=j-1
        #loop check for if i is greater or equal to 0 and if the value of the index before the key is greater than the key
        """
        Every element j below is added to the loop invariant after the conditions for the while loop are no longer satisfied.
        """
        while i >= 0 and arr[i] > key:
            #the value of the index after i is set to the value of the current index of i
            arr[i+1] = arr[i]
            #i is supposed to be the index before our key, since our key has swiched places, our i needs to move as well
            i = i-1
        #we re-assign key to the current index our key is in i.e the one after i
        arr[i+1] = key
    #THE LOOP GOES ON FOR ALL OTHER VALUES WITHIN THE ARRAY GOING TO THE RIGHT

    return arr

tarr = []
for i in range(0,5000):
    n = randint(0,10000)
    if n not in tarr:
        tarr.append(n)

print(f"Array Lenght: {len(tarr)}\n")
print(i_sort(tarr))

