#Suppose LeetCode will start its IPO soon. In order to sell a good price of its shares to Venture Capital, LeetCode would like to work on some projects to increase its capital before the IPO. Since it has limited resources, it can only finish at most k distinct projects before the IPO. Help LeetCode design the best way to maximize its total capital after finishing at most k distinct projects.

#You are given n projects where the ith project has a pure profit profits[i] and a minimum capital of capital[i] is needed to start it.

#Initially, you have w capital. When you finish a project, you will obtain its pure profit and the profit will be added to your total capital.

#Pick a list of at most k distinct projects from given projects to maximize your final capital, and return the final maximized capital.

#The answer is guaranteed to fit in a 32-bit signed integer.

#Example 1:
#Input: k = 2, w = 0, profits = [1,2,3], capital = [0,1,1]
#Output: 4

#Explanation: Since your initial capital is 0, you can only start the project indexed 0.
#After finishing it you will obtain profit 1 and your capital becomes 1.
#With capital 1, you can either start the project indexed 1 or the project indexed 2.
#Since you can choose at most 2 projects, you need to finish the project indexed 2 to get the maximum capital.
#Therefore, output the final maximized capital, which is 0 + 1 + 3 = 4.

#Example 2:
#Input: k = 3, w = 0, profits = [1,2,3], capital = [0,1,2]
#Output: 6
 

#Constraints:

#1 <= k <= 105
#0 <= w <= 109
#n == profits.length
#n == capital.length
#1 <= n <= 105
#0 <= profits[i] <= 104
#0 <= capital[i] <= 109



import heapq

class Solution(object):
    def findMaximizedCapital(self, k, w, profits, capital):
        """
        :type k: int
        :type w: int
        :type profits: List[int]
        :type capital: List[int]
        :rtype: int
        """
        # Initialize a list to store projects as (capital, profit) pairs
        projects = [(capital[i], profits[i]) for i in range(len(profits))]
        
        # Sort the projects based on capital required in ascending order
        projects.sort(key=lambda x: x[0])
        
        # Initialize a max heap for profits we can afford
        available_projects = []
        
        # Initialize an index for projects list
        project_index = 0
        
        # Loop until we have completed k projects or there are no more projects we can afford
        for _ in range(k):
            # Add all projects to the heap that we can afford with our current capital
            while project_index < len(projects) and projects[project_index][0] <= w:
                # Push the profit onto the heap as a negative number because heapq is a min heap
                heapq.heappush(available_projects, -projects[project_index][1])
                project_index += 1
            
            # If there are no available projects we can afford, break out of the loop
            if not available_projects:
                break
            
            # Pop the project with the maximum profit from the heap and add it to our capital
            w -= heapq.heappop(available_projects)
        
        return w

# Example usage:
# sol = Solution()
# print(sol.findMaximizedCapital(k=2, w=0, profits=[1,2,3], capital=[0,1,1]))  # Output: 4
