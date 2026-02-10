class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        i =0
        arr = []
        for num in range(1,n+1):
            arr.append(num)

        while len(arr) > 1:
            i += k-1 
            i %= len(arr)
            arr.remove(arr[i])
        
        return arr[0]
