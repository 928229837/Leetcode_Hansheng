


def recursive():

    # Python Program for recursive binary search.

    # Returns index of x in arr if present, else -1
    def recusive_binarySearch(arr, l, r, x):
        # Check base case
        if r >= l:
            mid = int(l + (r - l) / 2)
            # If element is present at the middle itself
            if arr[mid] == x:
                return mid
                # If element is smaller than mid, then it
            # can only be present in left subarray
            elif arr[mid] > x:
                return recusive_binarySearch(arr, l, mid - 1, x)
                # Else the element can only be present
            # in right subarray
            else:
                return recusive_binarySearch(arr, mid + 1, r, x)
        else:
            # Element is not present in the array
            return -1


    # Test array
    arr = [2, 3, 4, 10, 40]
    x = 10

    # Function call
    result = recusive_binarySearch(arr, 0, len(arr) - 1, x)

    if result != -1:
        print("Element is present at index %d" % result)

    else:
        print("Element is not present in array")



def iterative():
    ############################################################
    # Python code to implement iterative Binary
    # Search.

    # It returns location of x in given array arr
    # if present, else returns -1
    def iterative_binarySearch(arr, l, r, x):
        while l <= r:

            mid = int(l + (r - l) / 2)

            # Check if x is present at mid
            if arr[mid] == x:
                return mid

                # If x is greater, ignore left half
            elif arr[mid] < x:
                l = mid + 1

            # If x is smaller, ignore right half
            else:
                r = mid - 1

        # If we reach here, then the element
        # was not present
        return -1


    # Test array
    arr = [2, 3, 4, 10, 40]
    x = 10

    # Function call
    result = iterative_binarySearch(arr, 0, len(arr) - 1, x)

    if result != -1:
        print("Element is present at index %d" % result)

    else:
        print("Element is not present in array")


if __name__ == "__main__":
    a = 0
    if a: recursive()
    else: iterative()