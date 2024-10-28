from pathlib import Path
import os

import functools
import os
import random
import secrets
import time

import numpy as np


def set_env(seed: int = -1) -> None:
    if seed == -1:
        seed = secrets.randbelow(1_000_000_000)
    random.seed(seed)
    np.random.seed(seed)


def get_current_dir() -> Path:
    try:
        return Path(__file__).parent.absolute()
    except NameError:
        return Path(os.getcwd())
