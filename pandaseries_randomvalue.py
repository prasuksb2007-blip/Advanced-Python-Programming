"""
Create a Pandas Series with ten random numbers.
"""
import numpy as np
import pandas as pd

random_series = pd.Series(np.random.rand(10))
print(random_series)
print("\n" + "=" * 50 + "\n")

"""
--> Output
0    0.047290
1    0.236791
2    0.852285
3    0.866941
4    0.362581
5    0.102016
6    0.236422
7    0.625535
8    0.242024
9    0.838188
dtype: float64

==================================================
"""