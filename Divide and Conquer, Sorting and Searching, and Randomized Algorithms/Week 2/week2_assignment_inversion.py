import pandas as pd

data = pd.read_csv('./algorithms_coursera/IntegerArray.txt', sep='\n', header=None)
data.columns = ["col"]
l = list(data['col'])

def Inversion(a):
    l = len(a)
    if l>2:
        l1 = l/2 if l%2==0 else (l+1)/2
        l2 = l-l1
        a_left = a[:l1]
        assert len(a_left)==l1
        a_right = a[l1:]
        assert len(a_right)==l2
        insertion_left, count_left = Inversion(a_left)
        insertion_right, count_right = Inversion(a_right)
        count = 0
        i = 0
        j = 0
        insertion_split = []
        for k in range(l):
            if (i<len(insertion_left)) & (j<len(insertion_right)):
                if insertion_left[i]<insertion_right[j] :
                    insertion_split.append(insertion_left[i])
                    i = i+1
                else:
                    count = count + len(insertion_left[i:])
                    insertion_split.append(insertion_right[j])
                    j = j+1
            else:
                if (i<len(insertion_left)): insertion_split.extend(insertion_left[i:])
                if (j<len(insertion_right)): insertion_split.extend(insertion_right[j:])
                break
        return insertion_split, count + count_left + count_right
    else:
        if (l==1):
            return a, 0
        if ((l==2) & (a[0]<a[1])):
            return a, 0
        elif ((l==2) & (a[0]>a[1])):
            return [a[1], a[0]], 1
        else:
            pass




arr, count_inv = Inversion(l)
