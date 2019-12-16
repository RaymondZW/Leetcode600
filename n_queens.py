def n_queens(n):
    res = []
    xy_dif = set()
    xy_sum = set()
    def dfs(queens, xy_dif, xy_sum):
        p = len(queens)
        if p == n:
            res.append(['.'*i + 'Q' + '.'*(n-1-i) for i in queens])
            return
        for q in range(n):
            if q in queens or p-q in xy_dif or p+q in xy_sum: continue
            xy_dif.add(p-q)
            xy_sum.add(p+q)
            dfs(queens + [q], xy_dif, xy_sum)
            xy_dif.remove(p-q)
            xy_sum.remove(p+q)
    dfs([], xy_dif, xy_sum)
    return res

sol = n_queens(4)
print(len(sol))
print(sol)

