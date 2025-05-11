# Coin Box Assignment Problem

## Problem Statement

John works in a coin factory where each coin has an ID. He has an array `nums` of size `N`. In the factory, coins are assigned to boxes based on the sum of the digits of their IDs. For example, if the ID of a coin is 321, the sum of its digits is 6 (since 3 + 2 + 1 = 6), so the coin will be placed in box 6.

John has been given a task to work with coins that have IDs in the range from the smallest number in `nums`, called the `low-limit`, to the largest number in `nums`, called the `high-limit`. For each number in this range (from `low-limit` to `high-limit`, inclusive), John needs to calculate the sum of the digits and place the coin in the corresponding box.

Help John determine which box contains the most coins and output the number of coins in that box.

**Note**: The factory has coins with IDs ranging from 0 to infinity, but John only needs to work with coins whose IDs lie between the low-limit and high-limit (inclusive).

## Input Format

- The first line contains an integer `N`, representing the number of elements in `nums`.
- The second line contains `n` space-separated integers representing the elements of the array `nums`.

## Output Format

- Print a single integer representing the maximum number of coins placed in any one box.

## Constraints

- `1 <= N <= 10^5`
- `0 <= nums[i] <= 10^4`

## Sample Testcase 0

### Input

5
26 19 21 28 20


### Output

2


### Explanation

The smallest number (`low-limit`) is `19` and the largest (`high-limit`) is `28`.

Coins ID's: `19, 20, 21, 22, 23, 24, 25, 26, 27, 28`

Box Numbers: `1+9, 2+0, 2+1, 2+2, 2+3, 2+4, 2+5, 2+6, 2+7, 2+8`

Box Numbers: `10, 2, 3, 4, 5, 6, 7, 8, 9, 10`

Box 10: IDs `19, 28` → 2 coins.

Other boxes have fewer coins.

The maximum number of coins in any box is `2`.

## Sample Testcase 1

### Input

3
5 15 7 


### Output

2

r
Copy
Edit

### Explanation

The smallest number (`low-limit`) is `5` and the largest (`high-limit`) is `15`.

Coins ID's: `5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15`

Box Numbers: `5, 6, 7, 8, 9, 1+0, 1+1, 1+2, 1+3, 1+4, 1+5`

Box Numbers: `5, 6, 7, 8, 9, 1, 2, 3, 4, 5, 6`

Box 5: IDs `5, 14` → 2 coins.

Box 6: IDs `6, 15` → 2 coins.

Other boxes have fewer coins.

The maximum number of coins in any box is `2`.

## Python Code Solution

    #Enter your code here. Read input from STDIN. Print output to STDOUT
    def sum_of_digits(n):
    total = 0
    while n > 0:
        total += n % 10
        n //= 10
    return total

    def solve(nums):
    # Step 1: Determine the low-limit and high-limit
    low_limit = min(nums)
    high_limit = max(nums)

    # Step 2: Dictionary to count coins in each box
    box_count = {}

    # Step 3: Process each coin ID from low-limit to high-limit
    for coin_id in range(low_limit, high_limit + 1):
        digit_sum = sum_of_digits(coin_id)
        if digit_sum in box_count:
            box_count[digit_sum] += 1
        else:
            box_count[digit_sum] = 1

    # Step 4: Find the maximum number of coins in any box
    max_coins_in_box = max(box_count.values())
    
    # Output the result
    print(max_coins_in_box)

    #Input reading and function calling
    if __name__ == "__main__":
    N = int(input())  # number of elements in nums
    nums = list(map(int, input().split()))  # list of coin IDs

    solve(nums)

