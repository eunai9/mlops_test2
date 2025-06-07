from torch.utils.data import Dataset
from src.mlops_test.data import corrupt_mnist
import os.path
import pytest

@pytest.mark.skipif(not os.path.exists("data/raw"), reason="Data files not found")
def test_my_dataset():
    """Test the MyDataset class."""
    train_set, _ = corrupt_mnist()
    assert isinstance(train_set, Dataset), "Dataset should be an instance of torch.utils.data.Dataset"
