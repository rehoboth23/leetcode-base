class Solution:
    def arrayNesting(self, nums: [int]) -> int:
        """
        :param nums:
        :return:
        theory: if i can reach an element from another element at any point, the other element will also reach my
        element at some point hence using a visited map to track visiting sizes we can do an optimized brute force
        to find the largest nest
        we could also terminate early if the size of the nest in the size of the array
        """
        def nest(s: set, arr, start, visited):
            if start in visited:
                return visited[start], []
            i = start
            visited = []
            count = 0
            while True and count < len(arr):
                visited.append(i)
                if arr[i] not in s:
                    s.add(arr[i])
                    i = arr[i]
                    count += 1
                else:
                    break
            return len(s), visited

        res = 0
        visited = {}
        for i in range(len(nums)):
            if i in visited:
                continue
            s, joins = nest(set(), nums, i, visited)
            for i in joins:
                visited[i] = res
            res = max(res, s)
        return res
