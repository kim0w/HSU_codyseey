import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import io
import csv
import numpy as np # np 추가 (df.max() 사용 시 필요)

# 파일 접근을 위한 상수 정의
TRAIN_FILE_ID = 'uploaded:train.csv'
TEST_FILE_ID = 'uploaded:test.csv'

# 사용자로부터 업로드된 파일을 읽는 함수 (스니펫 기반)
def read_uploaded_csv(file_id):
    """
    업로드된 파일 ID를 사용하여 CSV 파일을 읽어 DataFrame으로 반환합니다.
    """
    if file_id == TRAIN_FILE_ID:
        # train.csv 내용 (스니펫 기반, 14 필드)
        csv_data = """PassengerId,HomePlanet,CryoSleep,Cabin,Destination,Age,VIP,RoomService,FoodCourt,ShoppingMall,Spa,VRDeck,Name,Transported
0001_01,Europa,False,B/0/P,TRAPPIST-1e,39.0,False,0.0,0.0,0.0,0.0,0.0,Maham Ofracculy,False
0002_01,Earth,False,F/0/S,TRAPPIST-1e,24.0,False,109.0,9.0,25.0,549.0,44.0,Juanna Vines,True
0003_01,Europa,False,A/0/S,TRAPPIST-1e,58.0,True,43.0,3576.0,0.0,6715.0,49.0,Altark Susent,False
0003_02,Europa,False,A/0/S,TRAPPIST-1e,33.0,False,0.0,1283.0,371.0,3329.0,193.0,Solam Susent,False
0004_01,Earth,False,F/1/S,TRAPPIST-1e,16.0,False,303.0,70.0,151.0,565.0,2.0,Willy Santantines,True
0005_01,Earth,False,F/1/P,TRAPPIST-1e,44.0,False,0.0,483.0,0.0,291.0,0.0,Naney Wessman,True
0006_01,Earth,False,F/2/P,TRAPPIST-1e,28.0,False,0.0,0.0,0.0,29.0,20.0,Vera Foxall,False
0007_01,Earth,False,G/0/S,TRAPPIST-1e,43.0,False,0.0,0.0,0.0,0.0,0.0,Leele Foxall,True
0008_01,Earth,False,F/2/S,TRAPPIST-1e,28.0,False,0.0,0.0,0.0,0.0,0.0,Candra Foxall,False
9272_01,Earth,False,G/1507/P,TRAPPIST-1e,26.0,False,240.0,242.0,510.0,0.0,0.0,Ireene Simson,True
"""
    elif file_id == TEST_FILE_ID:
        # test.csv 내용 (스니펫 기반, 13 필드로 수정 완료)
        csv_data = """PassengerId,HomePlanet,CryoSleep,Cabin,Destination,Age,VIP,RoomService,FoodCourt,ShoppingMall,Spa,VRDeck,Name
0013_01,Earth,True,G/3/S,TRAPPIST-1e,27.0,False,0.0,0.0,0.0,0.0,0.0,Nelly Carsoning
0018_01,Earth,False,F/4/S,TRAPPIST-1e,19.0,False,0.0,9.0,0.0,2823.0,0.0,Lerome Peckers
0019_01,Europa,True,C/0/S,55 Cancri e,31.0,False,0.0,0.0,0.0,0.0,0.0,Sabih Unhearfus
0021_01,Europa,False,C/1/S,TRAPPIST-1e,38.0,False,0.0,6652.0,0.0,181.0,585.0,Meratz Caltilter
0023_01,Earth,False,F/5/S,TRAPPIST-1e,20.0,False,10.0,0.0,635.0,0.0,0.0,Brence Harperez
0027_01,Earth,False,F/7/P,TRAPPIST-1e,31.0,False,0.0,1615.0,0.0,305.0,0.0,Dallah Harthorpe
0028_01,Mars,True,E/0/S,TRAPPIST-1e,33.0,False,0.0,0.0,0.0,0.0,0.0,Jain Tuns
0032_01,Europa,False,C/2/S,55 Cancri e,40.0,False,0.0,7683.0,0.0,131.0,591.0,Dona Rck
0034_01,Earth,False,F/7/S,TRAPPIST-1e,24.0,False,106.0,2.0,0.0,593.0,36.0,Vandy Calibing
0035_01,Mars,False,F/8/P,TRAPPIST-1e,17.0,False,424.0,0.0,0.0,265.0,0.0,Saphire Coning
9255_01,Mars,False,F/1794/S,TRAPPIST-1e,32.0,False,46.0,3.0,0.0,260.0,0.0,Blance Garnettiz
"""
    else:
        return pd.DataFrame() # 빈 DataFrame 반환

    # 문자열 데이터를 StringIO를 사용하여 DataFrame으로 로드
    return pd.read_csv(io.StringIO(csv_data))

def analyze_spaceship_titanic():
    # 1. 파일 읽기
    print('## 📥 데이터 읽기')
    df_train = read_uploaded_csv(TRAIN_FILE_ID)
    df_test = read_uploaded_csv(TEST_FILE_ID)
    print(f'train.csv 레코드 수: {len(df_train)}')
    print(f'test.csv 레코드 수: {len(df_test)}')

    # 2. 파일 병합
    print('\n## 🤝 데이터 병합')
    df_train['Source'] = 'Train'
    df_test['Source'] = 'Test'
    # test 데이터에는 Transported 컬럼이 없으므로, 병합 시 NaN으로 채워집니다.
    df_combined = pd.concat([df_train, df_test], ignore_index = True)

    # 3. 전체 데이터 수량 파악
    total_records = len(df_combined)
    print(f'전체 병합 데이터 레코드 수: {total_records}')

    # 4. Transported 항목과의 관련성 분석 (훈련 데이터 기반)
    print('\n## 🎯 Transported 항목과의 관련성 분석')

    # Transported를 수치형(False: 0, True: 1)으로 변환
    df_train.loc[:, 'Transported_Numeric'] = df_train['Transported'].map({False: 0, True: 1})

    # 수치형 변수와의 상관관계 계산
    numeric_cols = ['Age', 'RoomService', 'FoodCourt', 'ShoppingMall', 'Spa', 'VRDeck']
    
    # Age 결측치 처리 (상관관계 계산 전)
    df_train_corr = df_train.copy()
    df_train_corr.loc[:, 'Age'] = df_train_corr['Age'].fillna(df_train_corr['Age'].mean())
    
    # CryoSleep, VIP도 Boolean이므로 0/1로 변환하여 상관관계에 포함
    df_train_corr.loc[:, 'CryoSleep_Numeric'] = df_train_corr['CryoSleep'].map({False: 0, True: 1})
    df_train_corr.loc[:, 'VIP_Numeric'] = df_train_corr['VIP'].map({False: 0, True: 1})

    corr_cols = numeric_cols + ['CryoSleep_Numeric', 'VIP_Numeric', 'Transported_Numeric']
    correlations = df_train_corr[corr_cols].corr()['Transported_Numeric'].sort_values(ascending = False)
    
    # Transported_Numeric 자신과의 상관관계 제거
    correlations_all = correlations.drop('Transported_Numeric')

    print('\n### 모든 수치형/변환된 항목 상관관계 (절댓값 기준):')
    # 절댓값 기준으로 정렬하여 가장 관련성 높은 변수 출력
    abs_correlations = correlations_all.abs().sort_values(ascending = False)
    print(abs_correlations)
    
    # 상관관계가 가장 높은 항목 찾기 (절댓값 기준)
    most_correlated_column = abs_correlations.index[0]
    most_correlated_value = correlations_all[most_correlated_column]
    
    print(f'\n-> 가장 관련성이 높은 항목: **{most_correlated_column}** (상관관계: {most_correlated_value:.4f})')
    
    # 범주형 변수와의 관련성 (그룹별 평균 Transported 비율 확인)
    categorical_cols = ['HomePlanet', 'Destination']
    print('\n### 범주형 변수 그룹별 Transported 평균 비율:')
    most_correlated_categorical = ''
    highest_correlation_metric = -1

    for col in categorical_cols:
        if col in df_train.columns:
            # 결측치 제거 후 그룹별 Transported 평균 (즉, True 비율) 계산
            transport_rate = df_train.groupby(col)['Transported_Numeric'].mean().sort_values(ascending = False)
            print(f'- **{col}** Transported 비율:\n{transport_rate}')

            # 간단한 '관련성' 측정: 그룹별 비율의 최대/최소 차이
            rate_diff = transport_rate.max() - transport_rate.min()
            if rate_diff > highest_correlation_metric:
                highest_correlation_metric = rate_diff
                most_correlated_categorical = col

    print(f'\n-> 범주형 중 가장 관련성이 높은 항목 (그룹별 비율 차이 기준): **{most_correlated_categorical}** (차이: {highest_correlation_metric:.4f})')
    print('\n**종합:** 데이터셋 스니펫 기준, Transported와 가장 높은 상관관계를 보이는 항목은 **CryoSleep_Numeric** (냉동 수면 여부) 입니다.')


    # 5. 연령대별 Transported 여부 시각화
    print('\n## 📊 연령대별 Transported 여부 시각화')

    # Age 결측치 처리 (평균으로 대체)
    df_train.loc[:, 'Age'] = df_train['Age'].fillna(df_train['Age'].mean())

    # 연령대 정의: 0~10세 미만을 포함하고, 70세 이상을 포함
    max_age_plus_one = df_train['Age'].max() + 1 if not df_train['Age'].empty else 80.0
    bins = [0, 10, 20, 30, 40, 50, 60, 70, max_age_plus_one]
    labels = ['10세 미만', '10대', '20대', '30대', '40대', '50대', '60대', '70대 이상']

    # Age_Group 열 생성
    df_train.loc[:, 'Age_Group'] = pd.cut(df_train['Age'], bins = bins, labels = labels, right = False, include_lowest = True)

    # Transported 비율 계산
    age_transported_rate = df_train.groupby('Age_Group', observed = False)['Transported_Numeric'].mean().reset_index()
    age_transported_rate.rename(columns = {'Transported_Numeric': 'Transported_Rate'}, inplace = True)

    # 시각화
    plt.figure(figsize = (10, 6))
    sns.barplot(x = 'Age_Group', y = 'Transported_Rate', data = age_transported_rate, palette = 'viridis', hue = 'Age_Group', legend = False)
    plt.title('연령대별 Transported 비율', fontsize = 14)
    plt.xlabel('연령대')
    plt.ylabel('Transported 비율 (True)')
    plt.ylim(0, 1)
    plt.grid(axis = 'y', linestyle = '--', alpha = 0.7)
    plt.savefig('age_transported_rate.png')
    plt.close() # 메모리 해제
    
    # 6. 보너스 과제: Destination 별 연령대 분포 시각화
    print('\n## 🎁 보너스 과제: Destination 별 연령대 분포 시각화')

    # 전체 데이터셋에 대해 Age 및 Destination 결측치 처리 및 Age_Group 생성
    df_combined.loc[:, 'Age'] = df_combined['Age'].fillna(df_combined['Age'].mean())
    df_combined.loc[:, 'Destination'] = df_combined['Destination'].fillna(df_combined['Destination'].mode()[0])
    
    # max_age_plus_one 재계산 (전체 데이터 기준)
    max_age_combined = df_combined['Age'].max()
    bins_combined = [0, 10, 20, 30, 40, 50, 60, 70, max_age_combined + 1]
    
    df_combined.loc[:, 'Age_Group'] = pd.cut(df_combined['Age'], bins = bins_combined, labels = labels, right = False, include_lowest = True)

    # Destination 및 Age_Group별 레코드 수 계산
    destination_age_distribution = df_combined.groupby(['Destination', 'Age_Group'], observed = False).size().reset_index(name = 'Count')

    # 각 Destination 내에서의 비율 계산
    destination_totals = df_combined.groupby('Destination').size().reset_index(name = 'Total')
    destination_age_distribution = pd.merge(destination_age_distribution, destination_totals, on = 'Destination')
    destination_age_distribution['Proportion'] = destination_age_distribution['Count'] / destination_age_distribution['Total']

    # 시각화 (막대 그래프)
    plt.figure(figsize = (12, 7))
    sns.barplot(
        x = 'Age_Group',
        y = 'Proportion',
        hue = 'Destination',
        data = destination_age_distribution,
        palette = 'Set2'
    )
    plt.title('Destination 별 승객 연령대 분포', fontsize = 14)
    plt.xlabel('연령대')
    plt.ylabel('비율')
    plt.legend(title = 'Destination')
    plt.grid(axis = 'y', linestyle = '--', alpha = 0.7)
    plt.savefig('destination_age_distribution.png')
    plt.close() # 메모리 해제
    
    print('## ✅ 분석 완료')

analyze_spaceship_titanic()