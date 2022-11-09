import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Limits number of rows to speed up analysis
number_of_rows = 2000

# for graph 4 and 5 used 200 000
number_of_rows = 200000

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
    # df_z_scaled = df.copy().loc[:, ["Severity", "Temperature(F)", "Humidity(%)", "Pressure(in)", "Wind_Chill(F)", "Humidity(%)",
    #  "Pressure(in)", "Visibility(mi)", "Wind_Speed(mph)", "Precipitation(in)"]]

    # # apply normalization techniques
    # for column in df_z_scaled.columns:
    #     df_z_scaled[column] = (df_z_scaled[column] -
    #                         df_z_scaled[column].mean()) / df_z_scaled[column].std() 
    # return df_z_scaled
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
    # average_and_mean(df, "Severity")
    plot_feature_histogram(df, "Severity")

"""
Parent function to start program
"""
def main():
    df = setup()
    prepare_data(df)
    # analysis(df)

    # Graph nr 1: Correlations between the quantitative weather features and severit
    # features = ["Severity", "Temperature(F)", "Humidity(%)", "Wind_Chill(F)",
    #  "Pressure(in)", "Visibility(mi)", "Wind_Speed(mph)", "Precipitation(in)"]
    # visualize_correlations(df, features)

    # Graph nr 2: This shows higher severity has a lower mean temperature
    # group_analysis(df, "Severity", "Temperature(F)")


    # Graph nr 3:
    # nr_of_weather = df["Weather_Condition"].value_counts()
    # grouped_by_severity = df[["Weather_Condition", "Severity"]].groupby("Severity").value_counts()
    # keyList = df["Weather_Condition"].unique()
    # result_dict = {key: None for key in keyList}
    # for index, value in grouped_by_severity.items():
    #     new_value = str(round(value / nr_of_weather[index[1]]* 100, 4) ) + "%"
    #     if result_dict[index[1]] != None:
    #         result_dict[index[1]] = result_dict[index[1]] + (index[0], new_value)
    #     else:
    #         result_dict[index[1]] = (index[0], new_value)
    # print(result_dict)

    # Graph nr 4: 
    # features = ["Amenity", "Bump", "Crossing", "Give_Way", "Junction", "No_Exit", "Railway", "Roundabout", "Stop",  "Traffic_Signal"]
    # result_dict = {key: None for key in features}
    # for feature in features:
    #     rslt_df = df[df[feature] == True] 
    #     feature_result = rslt_df[[feature, "Severity"]].groupby("Severity").value_counts()
    #     for index, value in feature_result.items():
    #         new_value = str(round(value / len(rslt_df)* 100, 4) ) + "%"
    #         if result_dict[feature] != None:
    #             result_dict[feature] = result_dict[feature] + (index[0], new_value)
    #         else:
    #             result_dict[feature] = (index[0], new_value)
    # print(result_dict)


if __name__ == "__main__":
    main()


