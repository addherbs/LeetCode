"""
Course Schedule II

Solution
There are a total of n courses you have to take labelled from 0 to n - 1.

Some courses may have prerequisites, for example, if prerequisites[i] = [ai, bi] this means you must take the course bi before the course ai.

Given the total number of courses numCourses and a list of the prerequisite pairs, return the ordering of courses you should take to finish all courses.

If there are many valid answers, return any of them. If it is impossible to finish all courses, return an empty array.

 

Example 1:

Input: numCourses = 2, prerequisites = [[1,0]]
Output: [0,1]
Explanation: There are a total of 2 courses to take. To take course 1 you should have finished course 0. So the correct course order is [0,1].
Example 2:

Input: numCourses = 4, prerequisites = [[1,0],[2,0],[3,1],[3,2]]
Output: [0,2,1,3]
Explanation: There are a total of 4 courses to take. To take course 3 you should have finished both courses 1 and 2. Both courses 1 and 2 should be taken after you finished course 0.
So one correct course order is [0,1,2,3]. Another correct ordering is [0,2,1,3].
Example 3:

Input: numCourses = 1, prerequisites = []
Output: [0]
 

Constraints:

1 <= numCourses <= 2000
0 <= prerequisites.length <= numCourses * (numCourses - 1)
prerequisites[i].length == 2
0 <= ai, bi < numCourses
ai != bi
All the pairs [ai, bi] are distinct.
"""

class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        from collections import defaultdict, deque
        vis = set()
        pre_req_dic = defaultdict(set)
        fan_ins = defaultdict(int)
        total = set()
        ans = []
        
        for x, y in prerequisites:
            fan_ins[x] += 1
            pre_req_dic[y].add(x)
        
        zero_fan_ins = deque([k for k in range(numCourses) if k not in fan_ins])
        
        while zero_fan_ins:
            current = zero_fan_ins.popleft()
            ans.append(current)
            if current in pre_req_dic:
                for neighbor in pre_req_dic[current]:
                    fan_ins[neighbor] -= 1
                    
                    if fan_ins[neighbor] == 0:
                        zero_fan_ins.append(neighbor)
        
        return ans if len(ans) == numCourses else []