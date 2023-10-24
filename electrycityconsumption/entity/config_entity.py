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