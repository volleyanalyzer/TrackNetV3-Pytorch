import numpy as np
import torch
import torch.nn as nn
import torch.nn.functional as F



class FocalLoss(nn.Module):
    """
        This is an implementation of focal-loss.
        see this webpage for more information: https://amaarora.github.io/2020/06/29/FocalLoss.html
    """
    def __init__(self, alpha = 0.9, gamma=2):
        super(FocalLoss, self).__init__()
        self.alpha = alpha
        self.gamma = gamma

    def forward(self, output, targets):
        # Flatten all data
        output = output.view(-1)
        targets = targets.view(-1)

        # Find distance to gound truth
        pt = np.array(list(map(lambda p,y: p.item() if y==1 else 1-p.item(), output, targets)))

        # make log
        log = -1*np.log10(pt)

        # add gamma and alpha
        focal_loss = (1-pt)**self.gamma * log
        focal_loss = list(map(lambda x, y: x*self.alpha if y==1 else x*(1-self.alpha) , focal_loss, y))

        return torch.tensor(np.mean(focal_loss))


# x = torch.from_numpy(np.array([0.2, 0.5]))
# y = torch.from_numpy(np.array([0,1]))

# loss = FocalLoss()
# print(loss.forward(x, y))