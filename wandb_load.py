import wandb
import torch
from src.mlops_test.model import MyAwesomeModel

run = wandb.init()
artifact = run.use_artifact('eunai9/model-registry/corrupt_mnist_model:latest', type='model')
artifact_dir = artifact.download("corrupt_mnist_model")
model = MyAwesomeModel()
model.load_state_dict(torch.load("corrupt_mnist_model/model.pth"))
print(model)