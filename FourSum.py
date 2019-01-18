def fourSumCount(self, A, B, C, D):
    """
    :type A: List[int]
    :type B: List[int]
    :type C: List[int]
    :type D: List[int]
    :rtype: int
    """
    count = 0
    ab_sum = []
    for a in A:
        for b in B:
            ab_sum.append(a + b)

    cd_sum = []
    for c in C:
        for d in D:
            cd_sum.append(-c - d)

    for i in ab_sum:
        for j in cd_sum:
            if i == j:
                count = count + 1

    return count


    count = 0
    ab_sum = {}
    for a in A:
        for b in B:
            if ab_sum.get(a + b) == None:
                ab_sum[a + b] = 1
            else:
                ab_sum[a + b] = ab_sum.get(a + b) + 1

    for c in C:
        for d in D:
            if ab_sum.get(-c - d) != None:
                count += ab_sum.get(-c - d)

    return count
