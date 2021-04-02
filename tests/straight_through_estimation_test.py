import torch

from unittest import TestCase

from gragas.straight_through_estimation import (straight_through_sigmoid,
                                                straight_through_tanh)


class TestStraightThrough(TestCase):
    pass

    # def test_straight_through_sigmoid_gradient(self):
    #     # FIXME
    #     values = torch.ones(5)
    #     result = straight_through_sigmoid(values)
    #     sigmoid = torch.sigmoid(values)
    #     exp_result = sigmoid * (1 - sigmoid)
    #     torch.testing.assert_allclose(result, exp_result)

    # def test_straight_through_tanh_gradient(self):
    #     # FIXME
    #     values = torch.ones(5)
    #     result = straight_through_tanh(values)
    #     cosh = torch.cosh(values)
    #     exp_result = 1. / (cosh * cosh)
    #     torch.testing.assert_allclose(result, exp_result)
