# LC887  鸡蛋掉落
# 给你 k 枚相同的鸡蛋，并可以使用一栋从第 1 层到第 n 层共有 n 层楼的建筑。
# 已知存在楼层 f ，满足0 <= f <= n ，任何从 高于 f 的楼层落下的鸡蛋都会碎，从 f 楼层或比它低的楼层落下的鸡蛋都不会破。
# 每次操作，你可以取一枚没有碎的鸡蛋并把它从任一楼层 x 扔下（满足1 <= x <= n）。如果鸡蛋碎了，你就不能再次使用它。如果某枚鸡蛋扔下后没有摔碎，则可以在之后的操作中 重复使用 这枚鸡蛋。
# 请你计算并返回要确定 f 确切的值 的 最小操作次数 是多少？
def egg(k, n):
    #  dp(鸡蛋数 t, 需要验证的楼层数nt)
    #  dp(0, k >=1) 均为无效状态，若有状态转移方程中涉及到无效状态则该转移无效，需要排除，转移方程仅与当前i及上一个i相关，因此可以确定边界条件及使用交替dp
    #  每个状态下的检测均有nt种选择， 每个选择对应两种子问题，选其中最大的且可行的解作为当前选择的解
    #  在所有选择中选择最小值
    #  状态转移方程 dp(k, n) = 1 + min(1 <= x <= n)(max((k-1, x-1), (k, n-x)))
    dp = [[0]*(n+1) for _ in range(k+1)]
    for i in range(1, n+1):
        dp[0][i] = None
        dp[1][i] = i  # 当仅有一个鸡蛋时，最差验证次数为层高数
    for i in range(2, k+1):
        for j in range(1, n+1):
            #  因为dp(k, n)为关于n的递增函数， max()中的两个函数为交叉形状，
            #  可以用二分查找寻找最大的dp(i-1,k-1) > dp(i)(n-k)的k值，即可确定min所对应的k值
            # target = n
            # for k in range(1, j+1):
            #     target = min(target, max(dp[i-1][k-1], dp[i][j-k]))
            # dp[i][j] = target + 1
            left = 1
            right = j
            while left <= right:
                mid = left + (right - left) // 2  # 1, 0;  2
                if dp[i - 1][mid - 1] == dp[i][j - mid]:
                    left = mid
                    break
                elif dp[i - 1][mid - 1] < dp[i][j - mid]:
                    left = mid + 1
                else:
                    right = mid - 1
            #  最后返回left
            #  下标返回值对应，细心
            dp[i][j] = min(max(dp[i - 1][left - 1], dp[i][j - left]), max(dp[i - 1][left - 2], dp[i][j - left + 1])) + 1
    return dp[-1][-1]


