class Solution(object):
    def multiply(self, num1, num2):
        if num1 == "0" or num2 == "0":
            return "0"

        result = [0] * (len(num1) + len(num2))

        for i in range(len(num1) - 1, -1, -1):
            for j in range(len(num2) - 1, -1, -1):
                mul = int(num1[i]) * int(num2[j])
                pos = i + j + 1

                result[pos] += mul
                result[pos - 1] += result[pos] // 10
                result[pos] %= 10

        return ''.join(map(str, result)).lstrip('0')