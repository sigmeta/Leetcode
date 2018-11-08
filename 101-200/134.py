class Solution:
    def canCompleteCircuit(self, gas, cost):
        """
        :type gas: List[int]
        :type cost: List[int]
        :rtype: int
        """
        s,t,j=0,0,0
        for i in range(len(gas)):
            s+=gas[i]-cost[i]
            if s<0: 
                s,t,j=0,t+s,i+1
        return j if s+t>=0 else -1
