import torch


def straight_through(hard_values: torch.Tensor,
                     soft_values: torch.Tensor) -> torch.Tensor:
    return (hard_values - soft_values).detach() + soft_values


def straight_through_sigmoid(values: torch.Tensor) -> torch.Tensor:
    hard_values = (values > 0).float()
    soft_values = torch.sigmoid(values)
    return straight_through(hard_values, soft_values)


def straight_through_tanh(values: torch.Tensor) -> torch.Tensor:
    ones = torch.ones_like(values)
    hard_values = torch.where(values > 0, ones, -ones)
    soft_values = torch.tanh(values)
    return straight_through(hard_values, soft_values)
