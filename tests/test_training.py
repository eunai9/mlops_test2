from src.mlops_test.train import train
import os

def test_training():
    train()
    assert os.path.isfile("models/model.pth"), "Model file should be created after training"