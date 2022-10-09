import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Limits number of rows to speed up analysis
number_of_rows = 2000


"""
Loads data
"""
def setup():
    df = pd.read_csv("data.csv", nrows=number_of_rows)
    print('Dataframe loaded...')
    return df

"""
Data cleaning / processing
"""
def prepare_data(df):
    # print(df.isna().sum())
    pass

"""
Find average and mean of features
"""
def average_and_mean(df, name):
    print(f'Average {name} = {df[name].mean()}. Median {name} = {df[name].median()}')


"""
Plot histogram of feature
"""
def plot_feature_histogram(df, name):
    df[name].plot(kind='hist', title=f'Historgram of {name} distribution', xticks=df[name].unique())
    plt.show()

"""
Find mean for value based on grouping
"""    
def group_analysis(df, groupby, what):
    print(df[[groupby, what]].groupby(groupby).mean())  


"""
Visualize correlations
"""
def visualize_correlations(df, features):
    df = df[features]
    plt.figure()
    corr = df.corr()
    sns.heatmap(corr, annot=True)
    plt.show()


"""
Parent function to start analysis
"""
def analysis(df):
    average_and_mean(df, "Severity")
    plot_feature_histogram(df, "Severity")

"""
Parent function to start program
"""
def main():
    df = setup()
    prepare_data(df)
    # analysis(df)

    # This shows higher severity has a lower mean temperature
    group_analysis(df, "Severity", "Temperature(F)")

    features = ["Severity", "Temperature(F)", "Humidity(%)", "Pressure(in)",]
    visualize_correlations(df, features)


if __name__ == "__main__":
    main()


