import numpy as np
import pandas as pd


data = np.array([
    12, 15, 18, 20, 22,
    24, 25, 27, 30, 32,
    35, 36, 38, 40, 42
])


series = pd.Series(data)


df = pd.DataFrame({
    "salary": [
        30000, 35000, 40000, 42000,
        45000, 48000, 50000, 55000,
        60000, 65000
    ]
})