# https://leetcode.com/problems/best-time-to-buy-and-sell-stock 


'''
Stock I:- Simple, single-pass.
        -One transaction allowed
Stock II:- Greedy for multiple transactions; efficient but no transaction limits.
        -Multiple transactions allowed
Stock III:- More computationally intensive due to tracking two transactions.
        -At most two transactions allowed

'''

'''
You can complete only one transaction (buy once and sell once).
Goal: Maximize profit.
Approach:
Track the minimum price seen so far while traversing the array.
Calculate the profit for each day as price - min_price.
Keep track of the maximum profit.
Code Complexity:-
Time Complexity: O(N)
Space Complexity:O(1)

'''


