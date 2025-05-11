# Problem: Widest Separation Between Cars with Different Features

## Problem Statement

Ram spots a line of N cars on the busy street, each with a unique feature. You're provided with an array called `features`, where `features[i]` represents a distinctive feature of the i-th car.

Ram's quest is to discover the widest separation between two cars with **different features**. This distance is determined by the **absolute difference in their indices**: `abs(i - j)`.

---

## Input Format

- The first line contains an integer `N`, the number of cars.
- The second line contains `N` space-separated integers, where each integer denotes the feature of the i-th car.

## Output Format

- Print a single integer, which is the widest separation between any two cars that have different features.

## Constraints

- 2 <= N <= 100
- 0 <= features[i] <= 1000

---

## Sample Testcase 0

**Input:**

20
32 8 23 90 19 29 16 40 95 11 51 9 24 50 36 100 84 60 79 63


**Output:**
19


**Explanation:**  
The maximum distance between two cars with distinctive features is between index 0 and 19: `|0 - 19| = 19`.

---

## Sample Testcase 1

**Input:**
8
9 9 5 4 2 9 9 9 


**Output:**
5


---

## Sample Testcase 2

**Input:**
6
4 3 3 6 2 4


**Output:**
4

---

## Approach

### Step-by-Step Plan:

1. **Iterate through the array**: Loop through the list of cars to identify their features and positions.
2. **Track the first occurrence**: Use a dictionary to track the first index where each feature occurs.
3. **Compare with other features**: For every car, compare its position with all previously encountered cars that have **different** features.
4. **Maximize the distance**: Update the maximum distance when a larger one is found.

---

## Python Code

```python
def max_distance_between_cars(features):
    # Dictionary to store the first occurrence of each feature
    first_occurrence = {}
    
    # Variable to track the maximum distance
    max_dist = 0
    
    # Loop through the features list
    for i in range(len(features)):
        # If the feature has not been encountered before
        if features[i] not in first_occurrence:
            first_occurrence[features[i]] = i
        
        # Loop through all other previously encountered features
        for feature, index in first_occurrence.items():
            if feature != features[i]:  # Check for different features
                max_dist = max(max_dist, abs(i - index))
    
    return max_dist

# Input reading
N = int(input())  # Number of cars
features = list(map(int, input().split()))  # Features of the cars

# Output the maximum distance
print(max_distance_between_cars(features))
```

## ⏱️ Time Complexity

**Worst-case Time Complexity:** `O(N²)`  
- In the worst case, for each car (at index `i`), we may compare it with up to `i` previously seen features.
- Since the maximum value for `N` is 100, this results in at most `100 × 100 = 10,000` comparisons, which is computationally acceptable for this problem.

---

## ✅ Conclusion

This solution efficiently calculates the **maximum distance between cars with different features** by:
- Tracking the first occurrence of each unique feature.
- Comparing each car with all previously seen cars that have a different feature.
- Maximizing the distance during each comparison.

Given the constraints, the algorithm is both **correct** and **efficient**, ensuring accurate results even in the worst-case scenarios.


**img**
![image](https://github.com/user-attachments/assets/48df7de1-8810-4f42-a657-c40f7e6239c6)
