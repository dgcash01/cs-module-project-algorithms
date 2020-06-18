'''
Input: a List of integers where every int except one shows up twice
Returns: an integer
'''
def single_number(numbers):
    counts = {}

    # loop through input list O(n)
    for number in numbers:
        # if item in counts
        if number in counts:
            # remove item
            del counts[number]
        # otherwise
        else:
            counts[number] = 1
            # add item

    for key, value in counts.items(): # O(1)
        if value == 1:
            return key

if __name__ == '__main__':
    # Use the main function to test your implementation
    arr = [1, 1, 4, 4, 5, 5, 3, 3, 9, 0, 0, 123456789, 123456789]

    print(f"The odd-number-out is {single_number(arr)}")

       