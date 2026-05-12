#!/usr/bin/env python
# coding: utf-8

# In[ ]
import pandas as pd
import numpy as np

def preprocess():

    # 데이터 불러오기
    df = pd.read_csv('data/RIE.csv', header=None)
    
    pressure = df.iloc[:, 0].values
    cf4 = df.iloc[:, 1].values
    top = df.iloc[:, 4].values
    r = df.iloc[:, 17].values
    g = df.iloc[:, 18].values
    b = df.iloc[:, 19].values
    
    X_base = np.stack([cf4, pressure, top, r, g, b], axis=1)
    
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

