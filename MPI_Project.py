import random
import time


def RandomNrGenerator():
    afile = open("Fluid.txt", "w" )

    for i in range(int(input('How many random numbers?: '))):
        line = str(random.randint(1, 1000))
        afile.write(line + '\n')
    

    afile.close()
def AllreadyDone():
    afile = open("Fluid.txt", "w")
    print("What is the largest number?")
    r = int(input())
    m = 1
    for i in range(r):
        line = str(m)
        m = m + 1
        afile.write(line + '\n')

def ReverseGenerator():
    afile = open("Fluid.txt", "w" )
    print("What is the biggest number?")
    k = int(input())
    for i in range(k):
        line = str(k)
        k = k - 1
        afile.write(line + '\n')
    

    afile.close()

def ListReader():
    ls = []
    with open("Fluid.txt", 'r') as f:
        for i in range(1, 1000000):
            x = f.read()
            ls = x.split("\n")
            for y in ls:
                if y != "":
                    l.append(int(y))


def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    
    mid = len(arr) // 2
    left_half = arr[:mid]
    right_half = arr[mid:]
    
    left_half = merge_sort(left_half)
    right_half = merge_sort(right_half)
    
    return merge(left_half, right_half)
   


def merge(left, right):
    result = []
    i = j = 0
    
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    
    result += left[i:]
    result += right[j:]
    
    return result

def bubble_sort(arr):
    n = len(arr)
    
    
    for i in range(n):
        
        
        for j in range(0, n-i-1):
            
            
            if arr[j] > arr[j+1] :
                arr[j], arr[j+1] = arr[j+1], arr[j]
                
    return arr

def radix_sort(arr):
    max_digit = max(arr)
    exp = 1
    
    while max_digit // exp > 0:
        counting_sort(arr, exp)
        exp *= 10
    
    return arr

def counting_sort(arr, exp):
    n = len(arr)
    output = [0] * n
    count = [0] * 10
    
    for i in range(n):
        index = arr[i] // exp
        count[index % 10] += 1
        
    for i in range(1, 10):
        count[i] += count[i-1]
        
    i = n - 1
    while i >= 0:
        index = arr[i] // exp
        output[count[index % 10] - 1] = arr[i]
        count[index % 10] -= 1
        i -= 1
        
    for i in range(n):
        arr[i] = output[i]

def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i-1
        while j >=0 and key < arr[j] :
                arr[j+1] = arr[j]
                j -= 1
        arr[j+1] = key
    return arr

def quicksort(arr):
    if len(arr) <= 1:
        return arr
    else:
        pivot = arr[0]
        left = []
        right = []
        for i in range(1, len(arr)):
            if arr[i] < pivot:
                left.append(arr[i])
            else:
                right.append(arr[i])
        return quicksort(left) + [pivot] + quicksort(right)


def selection_sort(arr):
    for i in range(len(arr)):
        min_index = i
        for j in range(i+1, len(arr)):
            if arr[j] < arr[min_index]:
                min_index = j
        arr[i], arr[min_index] = arr[min_index], arr[i]
    return arr

def heapify(arr, n, i):
    largest = i  
    l = 2 * i + 1    
    r = 2 * i + 2     
 
    if l < n and arr[i] < arr[l]:
        largest = l
 
    if r < n and arr[largest] < arr[r]:
        largest = r
 
    if largest != i:
        arr[i],arr[largest] = arr[largest],arr[i]  # swap
 
        heapify(arr, n, largest)
 
def heapsort(arr):
    n = len(arr)
 
    for i in range(n, -1, -1):
        heapify(arr, n, i)
 
    for i in range(n-1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i] # swap
        heapify(arr, i, 0)
 
    return arr

def count_sort(arr):
    max_val = max(arr)
    counts = [0] * (max_val + 1)
    output = [0] * len(arr)
    for num in arr:
        counts[num] += 1
    for i in range(1, max_val + 1):
        counts[i] += counts[i-1]
    for num in arr:
        output[counts[num] - 1] = num
        counts[num] -= 1
    return output

print("Do you want a new list?\n 0.NO \n 1.Random \n 2.ReverseOrdered \n 3.AlreadySorted\n")
nl = 0
nl = int(input())
if nl == 1:
    RandomNrGenerator()
elif nl == 2:
    ReverseGenerator()
elif nl == 3:
    AllreadyDone()
    

l = []
print("What kind of sorting do you want to do?")
print("0.ALL OF THEM" + "\n" + "1.QuickSort" + "\n" + "2.HeapSort" + "\n" + "3.RadixSort" + "\n" + "4.CountingSort" + "\n" + "5.MergeSort" + "\n" + "6.BubbleSort" + "\n" + "7.SelectionSort" + "\n" + "8.InsertionSort")
m = int(input())
ListReader()
l0=[]

if m == 0:
    """
    l0[:]= l
    time0 = time.time()
    sorted_list = quicksort(l0)
    time1 = time.time()
    print("Time taken for QuickSort:", time1 - time0,"seconds")
    """
    l0[:]= l
    time0 = time.time()
    sorted_list = heapsort(l0)
    time1 = time.time()
    print("Time taken for Heapsort:", time1 - time0,"seconds")

    l0[:]= l
    time0 = time.time()
    sorted_list = radix_sort(l0)
    time1 = time.time()
    print("Time taken for RadixSort:", time1 - time0,"seconds")

    l0[:]= l
    time0 = time.time()
    sorted_list = count_sort(l0)
    time1 = time.time()
    print("Time taken for CountingSort:", time1 - time0,"seconds")

    l0[:]= l
    time0 = time.time()
    sorted_list = merge_sort(l0)
    time1 = time.time()
    print("Time taken for MergeSort:", time1 - time0,"seconds")

    l0[:]= l
    time0 = time.time()
    sorted_list = bubble_sort(l0)
    time1 = time.time()
    print("Time taken for BubbleSort:", time1 - time0,"seconds")

    l0[:]= l
    time0 = time.time()
    sorted_list = selection_sort(l0)
    time1 = time.time()
    print("Time taken for SelectionSort:", time1 - time0,"seconds")

    l0[:]= l
    time0 = time.time()
    sorted_list = insertion_sort(l0)
    time1 = time.time()
    print("Time taken for InsertionSort:", time1 - time0,"seconds")
elif m == 1:
    l0[:]= l
    time0 = time.time()
    sorted_list = quicksort(l0)
    time1 = time.time()
    print("Time taken for QuickSort:", time1 - time0,"seconds")
elif m == 2:
    l0[:]= l
    time0 = time.time()
    sorted_list = heapsort(l0)
    time1 = time.time()
    print("Time taken for Heapsort:", time1 - time0,"seconds")
elif m == 3:
    l0[:]= l
    time0 = time.time()
    sorted_list = radix_sort(l0)
    time1 = time.time()
    print("Time taken for RadixSort:", time1 - time0,"seconds")
elif m == 4:
    l0[:]= l
    time0 = time.time()
    sorted_list = count_sort(l0)
    time1 = time.time()
    print("Time taken for CountingSort:", time1 - time0,"seconds")
elif m == 5:
    l0[:]= l
    time0 = time.time()
    sorted_list = merge_sort(l0)
    time1 = time.time()
    print("Time taken for MergeSort:", time1 - time0,"seconds")
elif m == 6:
    l0[:]= l
    time0 = time.time()
    sorted_list = bubble_sort(l0)
    time1 = time.time()
    print("Time taken for BubbleSort:", time1 - time0,"seconds")
elif m == 7:
    l0[:]= l
    time0 = time.time()
    sorted_list = selection_sort(l0)
    time1 = time.time()
    print("Time taken for SelectionSort:", time1 - time0,"seconds")
elif m == 8:
    l0[:]= l
    time0 = time.time()
    sorted_list = insertion_sort(l0)
    time1 = time.time()
    print("Time taken for InsertionSort:", time1 - time0,"seconds")









