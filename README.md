# Etch Depth Prediction Model
> 공정 변수와 광학 특성(DIC)을 통합한 머신러닝 기반 플라즈마 식각 깊이 예측 프레임워크

## 📌 논문 개요
### 수행 기간
> 2025.05 ~ 2026.02
### DOI
> https://doi.org/10.1116/6.0005255
### 목표
> - 공정 변수뿐만 아니라 비접촉식 광학 데이터를 결합하여 예측 성능을 높이고자 함 </br>
> - 물리 기반 모델의 높은 연산 비용과 실시간 모니터링의 어려움 등의 한계를 대체할 수 있는 시스템 가능성을 보여주고자 함 </br>
> - 각 변수의 SHAP 기여도를 분석하여 조건에 따른 식각율 차이를 분석하고 함


## 📑 논문 결과
### fold 별 모델 예측 비교
> - fold 별 색이 상이함 </br>
> - 전체 데이터셋을 5개의 fold로 나누어 학습과 검증 진행 </br>
> - RF > ANN > Linear 순으로 실제 식각 깊이와 유사한 모습 </br>
> 
> <img src="https://github.com/user-attachments/assets/641733ea-346c-4af7-b476-08c5e1d6a690" width="50%" /> </br>

### 모델의 성능 비교
> <img width="329" height="137" alt="image" src="https://github.com/user-attachments/assets/7a911130-96b4-4fed-88a1-df8196ae0a9f" />


### SHAP 결과
#### 선형 모델
> <img src="https://github.com/user-attachments/assets/c62f33c8-002c-4256-9755-744cd1e91272" width="60%" />

#### ANN 모델
> <img src="https://github.com/user-attachments/assets/0a280939-4ded-4efa-889b-7d715a2625f8" width="60%" />

#### RF 모델
> <img src="https://github.com/user-attachments/assets/29f01af5-55b4-42a8-b233-b513bfb65909" width="60%" />

#### SHAP 분석 결과
> <img width="311" height="206" alt="image" src="https://github.com/user-attachments/assets/9c47daad-420d-4ccb-8f06-a30a1a5e44c2" />

#### 결과 요약
> - 공정 변수 중 PF Power가 영향력이 가장 큰 변수 </br>
> -> 실제 플라즈마 물리 현상과 일치함을 보여줌 </br>
> - 광학 데이터 중 G와 B가 공정 변수보다 상위에 위치하는 경우</br>
> -> 시각적 색상 변화가 실제 식각 깊이의 미세한 차이를 더 정확하게 반영함</br>
> - 머신러닝 모델이 물리적으로 타당한 근거를 바탕으로 예측하고 있음을 검증

## 🚨 트러블슈팅



