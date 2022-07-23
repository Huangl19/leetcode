# 剑指 Offer II 115. 重建序列
def sequencereconstruction(org, seqs):
    import collections
    # 标准的topological sort 问题
    # 难点在于如何发现题目的本质是topological
    graph = {}
    indegree = {}
    # 初始化两个字典
    for i in seqs:
        for j in i:
            graph[j] = []
            indegree[j] = 0

    for i in seqs:
        for j in range(0, len(i)-1):
            graph[i[j]].append(i[j+1])
            indegree[i[j+1]] += 1

    q = collections.deque()
    for i in indegree.keys():
        if not indegree[i]:
            q.append(i)
    ans = []

    while q:
        l = len(q)
        if l != 1:
            return False
        temp = q.popleft()
        ans.append(temp)
        for i in graph[temp]:
            indegree[i] -= 1
            if not indegree[i]:
                q.append(i)

    if len(ans) != len(org) or len(ans) != len(graph.keys()):  # 若排序结果长度与输入不同：或者结果长度相同但top存在环 都返回False
        return False

    for i in range(len(ans)):
        if org[i] != ans[i]:
            return False
    return True
