class Solution:
    def addDigits(self, num: int) -> int:
        agg = 0
        while num != 0:
            print('num:', num)
            agg += num % 10
            num //= 10
        if agg >= 10:
#             print('agg:', agg)
            self.addDigits(agg)
        else:
            return agg


    def multiply(self, num1: str, num2: str) -> str:
        if not num1 or not num2: return '0'
        m = len(num1)
        n = len(num2)

        # The len of final output is known, it's m+n
        pos = [0 for i in range(m + n)]
        for i in range(m - 1, -1, -1):
            for j in range(n - 1, -1, -1):
                mul = (ord(num1[i]) - ord('0')) * (ord(num2[j]) - ord('0'))
                p1 = i + j
                p2 = i + j + 1
                sum_cur = mul + pos[p2]
                pos[p2] = mul % 10
                pos[p1] += mul // 10  # notice pos is +=, not =
        idx = 0
        while idx < len(pos) and pos[idx] == 0:
            idx += 1
        res = ''.join([str(i) for i in pos[idx:]])
        return res



sol = Solution()
# sol.addDigits(38)
print(sol.multiply('456','123'))