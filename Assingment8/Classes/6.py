class PowerCalculator:
    def pow(self, x, n):
        if n == 0:
            return 1
        if n < 0:
            return 1 / self.pow(x, -n)
        if n % 2 == 0:
            half = self.pow(x, n // 2)
            return half * half
        else:
            return x * self.pow(x, n - 1)
