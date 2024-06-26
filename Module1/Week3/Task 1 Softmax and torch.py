import torch
import torch.nn as nn

class MySoftmax(nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x):
        x_max = torch.max(x, dim=0, keepdims=True)
        x_exp = torch.exp(x - x_max.values)
        partition = x_exp.sum(0, keepdims=True)
        return x_exp / partition

data = torch.Tensor([1, 2, 3])
my_softmax = MySoftmax()
output = my_softmax(data)
print(output)

new_data = torch.Tensor([1, 2, 300000000])
new_output = my_softmax(new_data)
print(new_output)

