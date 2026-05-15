class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = collections.Counter(nums)
        buckets = [[] for _ in range(len(nums) + 1)]
        for n, f in count.items():
            buckets[f].append(n)
        res = []
        for bucket in range(len(buckets) - 1, 0, -1):
            for elem in buckets[bucket]:
                res.append(elem)
                if (len(res) == k):
                    return res
        return []
