from dataclasses import dataclass
from pathlib import Path
from typing import List

@dataclass(frozen=True)
class DataIngestionConfig:
    root_dir: Path
    local_data_path: Path
 

@dataclass(frozen = True)
class PrepareBaseModelConfig:
    root_dir : Path
    base_model_path : Path
    params_learning_rate : float
    input_shape: List[int]

@dataclass(frozen=True)
class TrainingConfig:
    root_dir : Path
    trained_model_path : Path
    base_model_path : Path
    training_data : Path
    params_epochs : int
    params_batch_size : int
    params_loss_function : str
    params_optimizer : str