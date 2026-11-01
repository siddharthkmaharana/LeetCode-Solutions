from typing import List
from bisect import bisect_right

class Solution:
    def pathExistenceQueries(self, n: int, nums: List[int], maxDiff: int, queries: List[List[int]]) -> List[int]:
        vals = sorted(set(nums))
        m = len(vals)
        if m == 0:
            return [-1] * len(queries)

        LOG = 18
        up = [[0] * m for _ in range(LOG)]
        down = [[0] * m for _ in range(LOG)]

        for i in range(m):
            target = vals[i] + maxDiff
            j = bisect_right(vals, target) - 1
            up[0][i] = j

            target_down = vals[i] - maxDiff
            k = bisect_right(vals, target_down - 1)
            down[0][i] = k

        for step in range(1, LOG):
            for i in range(m):
                up[step][i] = up[step - 1][up[step - 1][i]]
                down[step][i] = down[step - 1][down[step - 1][i]]

        val_to_idx = {v: i for i, v in enumerate(vals)}
        ans = []

        for u, v in queries:
            if u == v:
                ans.append(0)
                continue
            val_u, val_v = nums[u], nums[v]
            if val_u == val_v:
                ans.append(1 if abs(val_u - val_v) <= maxDiff else -1)
                continue

            idx_u = val_to_idx[val_u]
            idx_v = val_to_idx[val_v]

            if idx_u < idx_v:
                steps = 0
                curr = idx_u
                for step in range(LOG - 1, -1, -1):
                    nxt = up[step][curr]
                    if nxt < idx_v:
                        curr = nxt
                        steps += (1 << step)
                if up[0][curr] >= idx_v:
                    ans.append(steps + 1)
                else:
                    ans.append(-1)
            else:
                steps = 0
                curr = idx_u
                for step in range(LOG - 1, -1, -1):
                    nxt = down[step][curr]
                    if nxt > idx_v:
                        curr = nxt
                        steps += (1 << step)
                if down[0][curr] <= idx_v:
                    ans.append(steps + 1)
                else:
                    ans.append(-1)

        return ans
