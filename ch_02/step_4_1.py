import pandas as pd
from step_3_2 import OUT_3_2 # 이전에 작성한 모듈을 불러옴

N=4
df_raw = pd.read_excel(OUT_3_2)
df_head, df_tail = df_raw.iloc[:N], df_raw.iloc[N:]
df_tail