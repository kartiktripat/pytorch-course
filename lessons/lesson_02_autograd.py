import torch
x = torch.tensor(3.0, requires_grad=True)
y = x**2 + 2*x
y.backward()
print(x.grad)

#y.backward()

y = x**3 + 3*x
y.backward()
print(x.grad)

# Prediction: the final print will show 8 because the old gradient is cleared first.
x.grad.zero_()
print(x.grad)

y = x**2 + 2*x
y.backward()
print(x.grad)

#torch.tensor(3, requires_grad=True) 