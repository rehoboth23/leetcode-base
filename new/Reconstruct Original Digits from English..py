import collections


class Solution:
    def originalDigits(self, s: 'str') -> 'str':
        # building hashmap letter -> its frequency
        count = collections.Counter(s)

        res = {}
        res["0"] = count["z"]
        res["2"] = count["w"]
        res["4"] = count["u"]
        res["6"] = count["x"]
        res["8"] = count["g"]
        res["3"] = count["h"] - res["8"]
        res["5"] = count["f"] - res["4"]
        res["7"] = count["s"] - res["6"]
        res["9"] = count["i"] - res["5"] - res["6"] - res["8"]
        res["1"] = count["o"] - res["0"] - res["2"] - res["4"]

        nums = [k * res[k] for k in sorted(res.keys())]
        return "".join(nums)