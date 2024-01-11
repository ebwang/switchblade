# Python Implementation of the above approach
def minMax(arr):
	
	# Initialize the min_value
	# and max_value to 0
	min_value = 0
	max_value = 0
	n=len(arr)
	
	# Sort array before calculating
	# min and max value
	arr.sort()
	j=n-1
	# Will print only the four elements
	for i in range(n-1):
		
		# All elements except
		# rightmost will be added
		min_value += arr[i]
		
		# All elements except
		# leftmost will be added because will decrease from upper to lower
		max_value += arr[j]
		j-=1
	
	# Output: min_value and max_value
	print(min_value," ",max_value)

# Driver Code
arr=[10, 9, 8, 7, 6, 5]
#arr1=[100, 200, 300, 400, 500]

minMax(arr)
#minMax(arr1)

# This code is contributed by ab2127.
