import pandas as pd
import matplotlib.pyplot as plt


def read_and_merge_files(train_path, test_path):
    train_data = pd.read_csv(train_path)
    test_data = pd.read_csv(test_path)

    # test 데이터에는 Transported가 없으므로 열 추가
    if 'Transported' not in test_data.columns:
        test_data['Transported'] = None

    merged_data = pd.concat([train_data, test_data], ignore_index=True)
    return merged_data


def analyze_data(data):
    print('전체 데이터 수량 :', len(data))
    print('\n열 정보 :', list(data.columns))

    # 수치형 컬럼만 선택하여 상관관계 계산
    numeric_data = data.select_dtypes(include='number')
    if 'Transported' in data.columns:
        transported_numeric = data['Transported'].map({True: 1, False: 0})
        data_for_corr = numeric_data.copy()
        data_for_corr['Transported'] = transported_numeric
        correlation = data_for_corr.corr()['Transported'].drop('Transported')
        print('\nTransported와 상관성이 높은 항목:')
        print(correlation.sort_values(ascending=False))
    else:
        print('\nTransported 열이 존재하지 않습니다 (test 데이터).')


def plot_age_transport_relation(data):
    data = data.dropna(subset=['Age', 'Transported'])
    data['Transported'] = data['Transported'].map({True: 1, False: 0})

    bins = [0, 19, 29, 39, 49, 59, 69, 79]
    labels = ['10대 이하', '20대', '30대', '40대', '50대', '60대', '70대']
    data['AgeGroup'] = pd.cut(data['Age'], bins=bins, labels=labels)

    grouped = data.groupby('AgeGroup')['Transported'].mean()
    plt.figure(figsize=(8, 5))
    plt.bar(grouped.index.astype(str), grouped.values, color='skyblue')
    plt.title('연령대별 Transported 비율')
    plt.xlabel('연령대')
    plt.ylabel('Transported 비율')
    plt.grid(axis='y', linestyle='--', alpha=0.7)
    plt.show()


def plot_destination_age_distribution(data):
    data = data.dropna(subset=['Destination', 'Age'])
    bins = [0, 19, 29, 39, 49, 59, 69, 79]
    labels = ['10대 이하', '20대', '30대', '40대', '50대', '60대', '70대']
    data['AgeGroup'] = pd.cut(data['Age'], bins=bins, labels=labels)

    grouped = data.groupby(['Destination', 'AgeGroup']).size().unstack(fill_value=0)
    grouped.T.plot(kind='bar', stacked=True, figsize=(9, 6))
    plt.title('Destination별 연령대 분포')
    plt.xlabel('연령대')
    plt.ylabel('인원 수')
    plt.legend(title='Destination')
    plt.grid(axis='y', linestyle='--', alpha=0.7)
    plt.show()


def main():
    train_path = r'C:\대학프로그래밍폴더\지능형SW설계\train.csv'
    test_path = r'C:\대학프로그래밍폴더\지능형SW설계\test.csv'

    merged_data = read_and_merge_files(train_path, test_path)
    analyze_data(merged_data)
    plot_age_transport_relation(merged_data)
    plot_destination_age_distribution(merged_data)


if __name__ == '__main__':
    main()
