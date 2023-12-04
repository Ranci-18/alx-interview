#!/usr/bin/python3
""" Prime Game """

def isWinner(x, nums):
    """ script for the prime game """
    if not nums or x < 1:
        return None
    
    round = 0
    nums.sort()

    for i in range(x):
        is_prime_i = True
        for j in range(2, int(nums[i]**0.5) + 1):
            if nums[i] % j == 0:
                is_prime_i = False
                break
        if is_prime_i:
            for k in range(x - 1, i, -1):
                if nums[k] % nums[i] == 0:
                    nums.remove(nums[k])
            nums.remove(nums[i])
            round += 1
            break
                
    if round % 2 == 0:
        return "Maria"
    else:
        return "Ben"