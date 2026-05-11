#!/usr/bin/env python
# coding: utf-8

# In[ ]:
import pandas as pd
import numpy as np

def noise(add_noise=False):
    # 데이터 불러오기
    df = pd.read_csv('data/RIE.csv', header=None)
    
    pressure = df.iloc[:, 0].values
    cf4 = df.iloc[:, 1].values
    top = df.iloc[:, 4].values
    r = df.iloc[:, 17].values
    g = df.iloc[:, 18].values
    b = df.iloc[:, 19].values
    
    X_base = np.stack([cf4, pressure, top, r, g, b], axis=1)

    if add_noise:
        np.random.seed(42)  # 재현성을 위해
        X_base[:, 0] += np.random.normal(0, 0.5, size=X_base.shape[0])  # CF4
        X_base[:, 1] += np.random.normal(0, 0.15, size=X_base.shape[0]) # Pressure
        X_base[:, 2] += np.random.normal(0, 0.01, size=X_base.shape[0]) # Top
        X_base[:, 3:6] += np.random.normal(0, 0.01, size=X_base[:, 3:6].shape) # R,G,B

    T_cols = [6,7,8,9,10,11,12,13,14]
    T_list = [df.iloc[:, col].values for col in T_cols]
    
    y_all = np.concatenate(T_list, axis=0).flatten()
    X_all = np.tile(X_base, (len(T_cols), 1))
    
    feature_names = [
    r'$\dot{Q}_{\mathrm{CF}_4}$',  # CF4 유량 (sccm)
    r'$p$',                        # Pressure (압력)
    r'$P_{\mathrm{RF}}$',          # Top power
    r'$R$',                        # Red intensity
    r'$G$',                        # Green intensity
    r'$B$'                         # Blue intensity
    ]
    
    return X_all, y_all, feature_names

