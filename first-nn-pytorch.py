from torch import nn
import torch.nn.functional as F

model = nn.Sequential([
    nn.modules.Embedding(27,),
    nn.modules.Flatten()
])
