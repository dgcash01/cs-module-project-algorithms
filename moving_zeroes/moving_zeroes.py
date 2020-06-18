'''
Input: a List of integers
Returns: a List of integers
'''
def moving_zeroes(arr):
    # Your code here
    non_zero_pointer = 0
    zero_pointer = len(arr) - 1

    while non_zero_pointer < zero_pointer:
        while arr[non_zero_pointer] != 0 and non_zero_pointer < zero_pointer:
            non_zero_pointer += 1
        while arr[zero_pointer] == 0 and non_zero_pointer < zero_pointer:
            zero_pointer -= 1

        arr[non_zero_pointer] = arr[zero_pointer]
        if non_zero_pointer != zero_pointer:
            arr[zero_pointer] = 0


    return arr


if __name__ == '__main__':
    # Use the main function here to test out your implementation
    arr = [0, 3, 1, 0, -2]

    print(f"The results of moving_zeroes is: {moving_zeroes(arr)}")