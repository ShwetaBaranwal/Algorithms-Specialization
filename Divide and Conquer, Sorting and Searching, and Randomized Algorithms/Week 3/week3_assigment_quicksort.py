import pandas as pd
import numpy as np

def swap(a,b):
    return b,a

def FindMedian(A):
    minvalue = min(A)
    maxvalue = max(A)
    for i in range(3):
        if A[i] != minvalue and A[i] != maxvalue:
            return A[i]

def QuickSort(x, q):
    x_len = len(x)
    # print (x)
    if x_len>1:
        if q==1:
            par_pos = 0
        elif q==2:
            par_pos= x_len-1
        elif q==3:
            k = (x_len/2)-1 if x_len%2==0 else int(x_len/2)
            middle = x[k]
            first = x[0]
            final = x[x_len-1]
            B = [first,middle,final]
            med = FindMedian(B)
            if med==B[0]:
                par_pos = 0
            elif med==B[1]:
                par_pos = k
            else:
                par_pos = x_len-1
        else:
            print ("wrong choice!")
        # print ("pivot:{}".format(x[par_pos]))
        # print ("par_pos is {}".format(par_pos))
        #making pivot first element of array
        x[0], x[par_pos] = swap(x[0],x[par_pos])
        #sorting
        i = 1
        for j in range(1, x_len):
            if x[0]>x[j]:
                x[i],x[j] = swap(x[i],x[j])
                i = i+1
        #putting pivot in its right place
        x[0], x[i-1] = swap(x[0],x[i-1])
        #calling recursive partitions
        x[0:i-1], l = QuickSort(x[0:i-1], q)
        x[i:], r = QuickSort(x[i:], q)
        return x, l+r+x_len-1
    else:
        return x, 0


data = pd.read_csv('./algorithms_coursera/_QuickSort.txt', header = None, sep = '\n', names = ['arr_val'])
lst = list(data.arr_val)
lst1, res_count1 = QuickSort(lst, 1)
lst = list(data.arr_val)
lst2, res_count2 = QuickSort(lst, 2)
lst = list(data.arr_val)
lst3, res_count3 = QuickSort(lst, 3)
print (res_count1, res_count2, res_count3)

(162085, 164123, 138382)
