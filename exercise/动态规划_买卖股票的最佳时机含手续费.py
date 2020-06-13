from typing import List

from exercise.getMaxProfitFee import getMaxProfitFee
from exercise.myUtils import timer


class Solution:
    @timer
    def maxProfit(self, prices: List[int], fee: int) -> int:
        # 3
        # def next(i, j):
        #     if i == len(prices):
        #         return 0
        #     in2 = prices[i] - prices[j] - fee + next(i + 1, i + 1)
        #     in3 = next(i + 1, j)
        #     print([i, j, max(in2, in3)])
        #     return max(in2, in3)
        #
        # return next(0, 0)
        #
        # 2
        # cash = [0]
        # for i in range(1, len(prices)):
        #     maxIncome = cash[-1]
        #     for j in range(i):
        #         res = cash[j] + prices[i] - prices[j] - fee
        #         print([i, j, res])
        #         maxIncome = max(maxIncome, res)
        #
        #     cash.append(maxIncome)
        # print(cash)
        # return cash[-1]
        # 3
        # cash = [0]
        # for i in range(1, len(prices)):
        #     print('i:', i, ',value:', prices[i], '--------------------------------')
        #     maxIncome = cash[-1]
        #     print('-1:', maxIncome)
        #     for j in range(i):
        #         res = cash[j] + prices[i] - prices[j] - fee
        #         print(j, ':', res)
        #         maxIncome = max(maxIncome, res)
        #     cash.append(maxIncome)
        # print(cash[-1])
        # return cash[-1]
        # 4
        # if len(prices) < 2:
        #     return 0
        # cash = prices[1] - prices[0] - fee
        # hold = max(0, cash)
        # for i in range(2, len(prices)):
        #     in1 = prices[i] - prices[i - 1] + cash
        #     in2 = prices[i] - prices[i - 1] - fee + hold
        #     cash = max(in1, in2)
        #     hold = max(hold, cash)
        # return hold
        # 5
        # dp = [[0, -prices[0]]]
        # for i in range(1, len(prices)):
        #     dp.append([])
        #     dp[i].append(max(dp[i - 1][0], dp[i - 1][1] + prices[i] - fee))
        #     dp[i].append(max(dp[i - 1][0] - prices[i], dp[i - 1][1]))
        # return dp[-1][0]
        # 6
        keep, nokeep = -prices[0], 0
        for i in range(1, len(prices)):
            # temp = keep
            keep = max(keep, nokeep - prices[i])
            nokeep = max(keep + prices[i] - fee, nokeep)
        return nokeep


s = Solution()
assert s.maxProfit([1, 3, 2, 8, 8, 4, 9], 2) == 8
assert s.maxProfit([1, 3, 7, 5, 10, 3], 3) == 6
assert s.maxProfit(
    [1036, 2413, 2776, 825, 2640, 31, 1560, 2917, 4282, 783, 3146, 2600, 1939, 694, 4284, 3881, 554, 167, 372, 4620,
     3037, 1175, 1075, 3845, 4981, 4495, 3406, 4228, 2807, 4774, 4526, 3914, 2633, 3762, 1570, 2334, 616, 1648, 1914,
     2900, 349, 2428, 4013, 1964, 4020, 1882, 629, 240, 2595, 2902, 3419, 292, 224, 4437, 4918, 632, 3701, 3840, 3996,
     2129, 3345, 3979, 1954, 781, 1576, 1084, 3250, 4517, 3106, 2133, 309, 4520, 2225, 4366, 4628, 1303, 4373, 1266,
     3181, 558, 3855, 3447, 4335, 2115, 4603, 661, 1715, 3972, 2846, 342, 686, 787, 273, 2575, 100, 2860, 3587, 4236,
     3862, 2238, 3471, 3123, 431, 4489, 1551, 596, 4037, 4986, 594, 2386, 326, 628, 1363, 2377, 4986, 3780, 3853, 2670,
     2852, 3519, 2998, 4083, 3392, 2394, 1083, 3958, 4082, 1506, 2322, 2715, 4901, 2555, 4097, 3748, 4717, 3901, 3329,
     4616, 3334, 2603, 3705, 631, 3541, 555, 508, 464, 4495, 4463, 3616, 31, 2177, 3307, 1011, 2759, 751, 1537, 1000,
     292, 3921, 1442, 2726, 4677, 792, 82, 2580, 609, 4758, 3190, 1958, 913, 955, 1259, 1634, 4729, 2672, 1761, 1467,
     2347, 4295, 2049, 4708, 1452, 3411, 1428, 4078, 2627, 3785, 2432, 2916, 492, 1108, 1691, 972, 3823, 4086, 2115,
     1925, 1454, 291, 3266, 300, 2539, 2681, 2084, 4633, 1084, 1061, 1043, 1304, 2205, 410, 4332, 2567, 703, 529, 4273,
     3684, 308, 3164, 4876, 3108, 4993, 4555, 1237, 4753, 549, 2795, 3426, 819, 2897, 825, 2514, 3419, 1854, 3209, 3766,
     2794, 4117, 4668, 2162, 1571, 2446, 1480, 974, 1090, 3903, 4655, 4452, 1451, 2953, 1241, 842, 1750, 3847, 3053,
     4395, 4338, 1493, 1660, 1569, 3418, 3029, 4416, 2056, 2283, 3392, 2032, 4354, 803, 4959, 3630, 2080, 1553, 873,
     4050, 1986, 2328, 55, 4602, 1430, 4238, 4326, 3382, 4845, 4968, 1903, 423, 4717, 2427, 4618, 2644, 4541, 380, 3404,
     4880, 2577, 1640, 189, 2692, 3788, 818, 4091, 4730, 611, 1776, 3594, 4746, 580, 2083, 4183, 3355, 3063, 658, 4532,
     3318, 3902, 556, 2249, 4653, 2118, 1529, 4793, 4935, 4259, 3542, 1705, 2839, 1436, 3918, 564, 3277, 2988, 2460,
     3213, 4445, 4238, 1954, 2213, 1748, 939, 1149, 1408, 2408, 1781, 1618, 1457, 2123, 3366, 826, 2094, 16, 1161, 3337,
     1864, 433, 1303, 4800, 4667, 4769, 1026, 3440, 1072, 4725, 6, 1263, 4184, 2728, 1315, 2091, 3032, 2071, 2672, 4557,
     1916, 638, 2133, 2687, 2408, 1677, 344, 697, 1699, 8, 480, 655, 2656, 4983, 455, 1611, 1726, 692, 392, 1921, 2555,
     3549, 3740, 3840, 3062, 3420, 2428, 1169, 4570, 389, 3509, 2169, 3290, 1680, 1733, 1765, 2518, 3260, 3644, 765,
     4521, 269, 2501, 4014, 1743, 239, 4908, 1656, 4433, 3647, 2612, 4872, 387, 3091, 4011, 564, 4421, 810, 3623, 3451,
     4108, 1428, 475, 3755, 4484, 3527, 3062, 4706, 3424, 2678, 2411, 4446, 2556, 4305, 1305, 646, 1458, 4471, 1689,
     4556, 3851, 1245, 1197, 3785, 1175, 2904, 302, 2422, 4302, 2148, 2338, 4288, 375, 2824, 1623, 3717, 1142, 4254,
     192, 783, 1963, 2225, 1209, 1746, 3072, 2737, 4640, 4919, 3614, 804, 4029, 1751, 2360, 3789, 4445, 2283, 2769,
     2833, 4452, 2978, 2809, 4532, 4365, 2124, 3541, 2658, 2902, 4688, 3980, 1543, 4041, 1420, 1452, 1284, 66, 19, 947,
     932, 3244, 3374, 1910, 2561, 3466, 4104, 1667, 589, 3048, 730, 1770, 1241, 2270, 4016, 2835, 604, 4771, 514, 3854,
     3427, 1875, 2038, 3067, 3216, 4732, 3735, 4440, 2855, 4958, 4569, 1685, 3539, 4589, 3512, 3143, 898, 3004, 3072,
     2573, 3163, 2522, 3927, 330, 3874, 363, 1900, 1629, 1156, 4259, 2747, 3445, 4513, 2867, 52, 3870, 1761, 619, 3308,
     4380, 1101, 2592, 4852, 4140, 174, 3997, 4617, 3500, 3028, 907, 2355, 759, 374, 2429, 412, 2132, 3973, 3583, 3028,
     2070, 2235, 2659, 1053, 2558, 753, 1221, 1185, 2225, 1593, 3554, 3703, 332, 2843, 3349, 3871, 4389, 6, 2768, 4382,
     902, 417, 191, 2107, 2838, 4958, 3905, 4966, 3937, 1105, 4150, 2682, 3396, 818, 2297, 2077, 2032, 3340, 2478, 127,
     4379, 954, 2593, 3454, 1230, 2308, 3694, 2179, 4134, 653, 3808, 4043, 2069, 660, 4515, 4189, 4876, 1784, 4166, 342,
     1766, 3305, 1980, 1909, 4115, 4115, 1461, 2061, 838, 3112, 122, 656, 4856, 4822, 3468, 2111, 2700, 4124, 4663,
     2948, 3029, 4182, 3847, 4760, 1323, 1505, 308, 128, 874, 583, 2671, 1315, 747, 2682, 2841, 67, 2712, 2703, 4471,
     2952, 3081, 464, 655, 57, 1460, 1395, 682, 2447, 2590, 4624, 1578, 64, 4060, 2975, 1236, 831, 3313, 1432, 2589,
     3777, 1868, 1720, 45, 3311, 4532, 2672, 454, 752, 4839, 4717, 748, 4323, 2999, 3491, 631, 1407, 1453, 4611, 4263,
     3366, 584, 2014, 2396, 1902, 4569, 3002, 1938, 3998, 4093, 1899, 3071, 2815, 1974, 302, 1641, 2836, 565, 264, 1332,
     3319, 3689, 2181, 3873, 4883, 3849, 1991, 4633, 4556, 3866, 142, 2903, 3181, 740, 3311, 2071, 280, 714, 2440, 3950,
     290, 3580, 738, 1604, 3631, 1989, 1299, 836, 1913, 224, 1066, 1741, 1551, 1735, 4601, 2024, 4570, 4192, 1723, 3949,
     3696, 1419, 1760, 697, 4764, 3405, 4443, 199, 717, 4568, 3252, 2016, 2151, 1741, 2613, 2736, 4053, 814, 4282, 3392,
     615, 1998, 3294, 3663, 559, 4278, 4626, 55, 1418, 2056, 3191, 3181, 1732, 1887, 2517, 3180, 2154, 2166, 3096, 3930,
     2721, 4332, 427, 4332, 4237, 3928, 2262, 4657, 2202, 922, 3711, 1921, 4728, 2236, 2441, 622, 233, 293, 1466, 1891,
     1222, 3693, 3261, 2605, 3486, 102, 3612, 1897, 2698, 3524, 3567, 613, 3834, 1583, 1482, 4734, 2339, 752, 1428,
     4121, 3267, 3518, 4652, 3119, 1818, 4596, 3181, 3159, 4069, 3375, 3762, 1386, 3054, 3052, 67, 2246, 1493, 2738,
     2835, 4906, 303, 1107, 3111, 1525, 1739, 437, 2941, 545, 1458, 993, 1871, 640, 4047, 2017, 4971, 4917, 701, 4811,
     4335, 3221, 4187, 4414, 756, 3069, 3052, 812, 3135, 928, 1264, 3356, 4518, 2136, 2691, 2638, 3156, 4909, 2944,
     3920, 4609, 1856, 654, 4643, 2932, 309, 3613, 4479, 4173, 1848, 165, 1171, 592, 3233, 3151, 4009, 3952, 2624, 38,
     2616, 2056, 841, 1764, 4667, 1526, 125, 3963, 933, 3951, 2151, 2110, 4666, 1000, 1985, 3868, 2735, 635, 277, 1129,
     572, 2136, 980, 2731, 556, 3012, 2900, 2180, 1912, 2799, 1771, 4441, 2666, 3958, 4381, 3677, 4218, 1276, 3512,
     4868, 4579, 2307, 3952, 3544, 651, 1300, 218, 489, 2837, 3737, 509, 3421, 879, 4353, 4695]
    , 655) == 595352
a, b = getMaxProfitFee()
assert s.maxProfit(a, b) == 309432285
