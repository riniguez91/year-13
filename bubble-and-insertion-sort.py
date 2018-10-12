'''array = [1,2,3,4,5,6,7,5]
for j in range(len(array)):
  if array[j] == 5:
    print("Found at index no." + str(j))
  else:
    print("Not found")'''

def bubbleSort(a):
  for i in range(1,len(a)):
    for j in range(1,len(a)):
      if a[j-1] > a[j]:
        a[j-1],a[j] = a[j],a[j-1]
  print("Sorted list" , a)
bubbleSort([78,9,5,1,3,2])

def insertion_sort(list):
    for index in range(1,len(list)):
        value = list[index]
        i = index - 1
        while i >= 0:
            if value < list[i]:
                list[i+1] = list[i]
                list[i] = value
                i = i - 1
            else:
                break
insertion_sort([7,1,3,5,9,2,3])
