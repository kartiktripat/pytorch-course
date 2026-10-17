import torch

w = torch.tensor(0.0, requires_grad=True)
lr = 0.1

for i in range(1,21):
    loss = (w - 5)**2
    loss.backward()
    with torch.no_grad():
        w -= lr * w.grad
        w.grad.zero_()
    print(w)

