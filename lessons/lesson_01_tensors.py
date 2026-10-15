import torch
'''a = torch.tensor([1.0, 2.0, 3.0])
b = torch.tensor([[1, 2, 3], [4, 5, 6]])
print(a.shape, a.dtype)
print(b.shape, b.dtype)
print(a * 2)
print(a + a) '''

##print(torch.tensor([1, 2, 3.5]).dtype)

#zero_t = torch.zeros(2,4)
##print(a.shape)

nums = torch.arange(12)
##print(b.shape)

grid = torch.reshape(nums, (3,4))
##grid = torch.reshape(nums, (5,3))
##print(c.shape)

#print(zero_t)
#print(nums)
#print(grid)

'''print(grid[1])
print(grid[:,-1])
print(grid[:,0])'''

A = torch.tensor([[1, 2], [3, 4]])

#print(A*A)
#print(A@A)

print(grid)