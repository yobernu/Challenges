# Problem: Product of the Last K Numbers - https://leetcode.com/problems/product-of-the-last-k-numbers/description/

class ProductOfNumbers:

# O(1) approach with prefix sum method
    def __init__(self):
        self.nums = []
        self.products = [1]
        
    def add(self, num: int) -> None:
        self.nums.append(num)
        if num == 0:
            self.products = [1]
        else:
            self.products.append(self.products[-1]*num)
        
    def getProduct(self, k: int) -> int:
        if k >= len(self.products):
            return 0
        return self.products[-1]//self.products[-k-1]
    
        
#Direct method with O(n) approach
    # def __init__(self):
    #     self.nums = []
    # def add(self, num):
    #     self.nums.append(num)
    # def getProduct(self, k):
    #     return prod(self.nums[-k:])







# Your ProductOfNumbers object will be instantiated and called as such:
# obj = ProductOfNumbers()
# obj.add(num)
# param_2 = obj.getProduct(k)