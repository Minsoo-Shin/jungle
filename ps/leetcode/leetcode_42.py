class Solution:
    def trap(self, height: List[int]) -> int:
        square = 0
        maxH = 0
        stack = [0]
        for h in height:
            if h > maxH:
                # square 반영
                while stack:
                    square += maxH - stack.pop()
                maxH = h
            else:
                stack.append(h)

        return square
