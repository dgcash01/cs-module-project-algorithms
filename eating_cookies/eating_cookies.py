'''
Input: an integer
Returns: an integer
'''
def eating_cookies(n, cache=None):
    # Your code here
    # amount = 3
    # for x in range(0, n + 1):
    #     print(x)

    cache = [0]*(n+1)      
    
    total = 0
    for i in range(0,len(cache)):
        if i < 2:
            cache[i]= 1
           
        elif i == 2:
            cache[i] = cache[i-2] + cache[i-1]
        else: 
            cache[i] = cache[i-3] + cache[i-2] + cache[i-1] 
    return cache[i]

    # return amount


if __name__ == "__main__":
    # Use the main function here to test out your implementation
    num_cookies = 5

    print(f"There are {eating_cookies(num_cookies)} ways for Cookie Monster to eat {num_cookies} cookies")
