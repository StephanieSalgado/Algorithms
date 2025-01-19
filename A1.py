import math
def log2(n):
    return math.log(n) / math.log(2)

complexities = [lambda n: math.sqrt(n),
                lambda n: n,
                lambda n: n * log2(n),
                lambda n: n ** 2,
                lambda n: n ** 3,
                lambda n: 2 ** n,
                lambda n: math.factorial(n)]

max_bound = [1e40, 1e20, 1e20, 1e10, 1e10, 100, 100]

times = [1000,
         1000 * 60,
         1000 * 60 * 60,
         1000 * 60 * 60 * 24,
         1000 * 60 * 60 * 24 * 30,]

print(' '.join(map(lambda v: '2^(' + '{:.2e}'.format(v) + ')', times)))

for k in range(len(complexities)):
    c = complexities[k]
    vals = []
    for t in times:
        l, r = 0, int(max_bound[k])
        max_n = 0
        while l <= r:
            mid = (l + r) // 2
            val = c(mid)
            if val == float('inf') or val > t:
                r = mid - 1
            else:
                l = mid + 1
                max_n = max(max_n, mid)
        vals.append(max_n)
    if k < 3:
        print(' '.join(map(lambda v: '{:.2e}'.format(v), vals)))
    else:
        print(' '.join(map(lambda v: str(int(math.floor(v))), vals)))
