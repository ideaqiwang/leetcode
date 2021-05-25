'''
134. Gas Station

There are n gas stations along a circular route, where the amount of gas at the ith station is gas[i].
You have a car with an unlimited gas tank and it costs cost[i] of gas to travel from the ith station to its next (i + 1)th station. You begin the journey with an empty tank at one of the gas stations.
Given two integer arrays gas and cost, return the starting gas station's index if you can travel around the circuit once in the clockwise direction, otherwise return -1. If there exists a solution, it is guaranteed to be unique

Example 1:
Input: gas = [1,2,3,4,5], cost = [3,4,5,1,2]
Output: 3
Explanation:
Start at station 3 (index 3) and fill up with 4 unit of gas. Your tank = 0 + 4 = 4
Travel to station 4. Your tank = 4 - 1 + 5 = 8
Travel to station 0. Your tank = 8 - 2 + 1 = 7
Travel to station 1. Your tank = 7 - 3 + 2 = 6
Travel to station 2. Your tank = 6 - 4 + 3 = 5
Travel to station 3. The cost is 5. Your gas is just enough to travel back to station 3.
Therefore, return 3 as the starting index.

Example 2:
Input: gas = [2,3,4], cost = [3,4,3]
Output: -1
Explanation:
You can't start at station 0 or 1, as there is not enough gas to travel to the next station.
Let's start at station 2 and fill up with 4 unit of gas. Your tank = 0 + 4 = 4
Travel to station 0. Your tank = 4 - 3 + 2 = 3
Travel to station 1. Your tank = 3 - 3 + 3 = 3
You cannot travel back to station 2, as it requires 4 unit of gas but you only have 3.
Therefore, you can't travel around the circuit once no matter where you start.
'''

class Solution:
    '''
        Solution 1:
        G0 G1 G2 G3 G4 G5
        C0 C1 C2 C3 C4 C5
        Suppose the car starts at index 0, it would stop at G4.
        Because there's no enough gas to G5.
        Then the next start index should be 5. We don't need to try index 1.
        Because we know it can go G0 - G1, which means the left gas >= 0.
        If gas == 0, then index 1 is same as index 0. It still cannot go to G5 from G4.
        If gas > 0, it's worse. It means when at G4, it has less gas.
        Therefore, no need to consider index 1 to index 4. Just try the next index since last failure. 
    '''
    def canCompleteCircuit(self, gas, cost):
        total_tank = cur_tank = 0
        start = 0
        for i in range(len(gas)):
            diff = gas[i] - cost[i]
            cur_tank += diff
            total_tank += diff
            if cur_tank < 0:
                # The possible start index jumps to i+1
                start = i + 1
                cur_tank = 0
        return start if total_tank >= 0 else -1

    '''
        Solution 2:
        Considering at each index if the gas > cost, means we are gaining some extra gas,
        otherwise, we are losing some gas.
        If a starting point eixits, it must start from the position where we lose the most of gas,
        so it can start to gain gas first to gather all the gas we need before we start losing.
        Therefore, we need to find the minimum total tank and its index.
        Then use the next index as the starting point.
                  [1, 2, 3, 4, 5]
                  [3, 4, 5, 1, 2]
        gas-cost: [-2,-2,-2, 3, 3]
        total_tank:    [-2,-4,-6,-3,-3]
    '''
    def canCompleteCircuit2(self, gas, cost):
        minIndex = 0
        minValue = sys.maxsize
        total_tank = 0
        for i in range(len(gas)):
            total_tank += gas[i] - cost[i]
            if total_tank < minValue:
                minValue = total_tank
                minIndex = i
        return (minIndex+1)%len(gas) if total_tank >= 0 else -1