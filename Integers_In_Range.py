class Solution:
    def isCovered(self, ranges: List[List[int]], left: int, right: int) -> bool:
    
        for i in range(left, right+1):
            for start, end in ranges:
                is_covered = False
                if start<= i <= end:
                    is_covered = True
                    break
            if is_covered == False:
                return False
        return True
