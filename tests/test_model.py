from src.mlops_test.model import MyAwesomeModel
import torch

def test_model():
    model = MyAwesomeModel()
    x = torch.randn(1, 1, 28, 28)
    y = model(x)
    assert y.shape == (1, 10), "Output shape should be (1, 10) for MNIST classification"