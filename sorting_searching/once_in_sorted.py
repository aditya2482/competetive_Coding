def search(arr, low, high):

	# Base cases
	if low > high:
		return None

	if low == high:
		return arr[low]

	# Find the middle point
	mid = low + (high - low)//2

	# If mid is even and element next to mid is
	# same as mid, then output element lies on
	# right side, else on left side
	if mid % 2 == 0:

		if arr[mid] == arr[mid+1]:
			return search(arr, mid+2, high)
		else:
			return search(arr, low, mid)

	else:
		# if mid is odd
		if arr[mid] == arr[mid-1]:
			return search(arr, mid+1, high)
		else:
			return search(arr, low, mid-1)

# Driver Code
# Test Array
arr = [1, 2, 2]

# Function call
result = search(arr, 0, len(arr)-1)
print(result)
