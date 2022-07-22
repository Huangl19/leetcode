# 设置交集大小至少为2

# 以下解有问题，无法通过[[1,3],[4,9],[0,10],[6,7],[1,2],[0,6],[7,9],[0,1],[2,5],[6,8]]
# def intersectionSizeTwo(intervals):
#     # 参考LC452， 最少的2元素重合区间数
#     intervals.sort(key=lambda x: x[0])
#     start = intervals[0][0]
#     end = intervals[0][1]
#     pre_end = None
#     ans = 0
#     for i in intervals[1:]:
#         # 判断是否有交集
#         if i[0] < end:  # 相交区间大于2个
#             start = max(start, i[0])
#             end = min(end, i[1])
#         else:
#             if start == pre_end:  # 当前重叠区间的start与前一个重叠区间的end相同，此start元素已计入前一个区间中
#                 ans += 1
#             else:
#                 ans += 2
#             if i[0] == end:
#                 pre_end = end
#             else:
#                 pre_end = None
#             start = i[0]
#             end = i[1]
#     if start == pre_end:
#         ans += 1
#     else:
#         ans += 2
#     return ans


# 按区间end从小到大排序，在每个区间都贪心选择最后两个数字，思路参照Pein,该贪心解即为最优解
# 排序后，区间的情况既分三种：1.相邻区间无重叠；2.仅重叠一个端点；3.重叠两个端点以上
# 3情况下分为3.1 a<i[0]<b 3.2 i[0]<a 3.2情况无需再填加另外点
# 3.1又分为2种情况 3.1.1 i[1]>b 3.1.2i[1]=b 影响贪心点的选择
def intersectionSizeTwo(intervals):
    intervals.sort(key=lambda x:x[1])
    a, b = intervals[0][1]-1, intervals[0][1]
    ans = 2
    for i in intervals[1:]:
        # 分三种情况
        if i[0] > b:
            ans += 2
            a, b = i[1]-1, i[1]
        elif i[0] == b:
            ans += 1
            a, b = b, i[1]
        elif a < i[0] <b:
            if i[1] > b:
                ans += 1
                a, b = b, i[1]
            else:  # 即只有i[1] == b情况
                ans += 1
                a, b = i[1]-1, i[1]
    return ans