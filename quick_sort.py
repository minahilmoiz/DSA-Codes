# Quick Sort in Python 

def quicksort (sequence):
	length= len(sequence)
	if length<=1:
		return sequence
	else:
		pivot= sequence.pop()
		
	greater_item=[]
	smaller_item =[]
		
	for i in sequence :
		if pivot < i :
			greater_item .append (i)
		else:
			smaller_item.append(i)

	return quicksort(smaller_item)+[pivot]+	quicksort(greater_item)

sequence= [1,4,8,9,3,2]	
a = quicksort(sequence)
print('Sorted Array in Ascending Order:')
print(a)

