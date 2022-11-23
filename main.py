import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Limits number of rows to speed up analysis
# number_of_rows = 20000

# for graph 4 and 5 used 200 000
# number_of_rows = 200000

"""
Loads data
"""
def setup():
    # df = pd.read_csv("data.csv", nrows=number_of_rows)
    df = pd.read_csv("data.csv")
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
Plot relative histogram of feature
"""
def plot__relative_feature_histogram(df, name):
    y_values = []
    x_ticks = [2,3,4]
    nr_of_values = len(df)
    for tick in x_ticks:
        # nr_of_value = df[name == tick].count()
        nr_of_value = df[df[name] == tick][name].count()
        y_values.append(round(nr_of_value/nr_of_values*100, 2))
    return y_values
    # plt.bar(x_ticks, y_values)
    # # df[name].plot(kind='hist', title=f'Historgram of {name} distribution', xticks=x_ticks)
    # plt.show()


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

    # Graph nr 2 v2: This shows higher severity has a lower mean temperature plotted
    # group_analysis(df, "Severity", "Temperature(F)")


    # Graph nr 6: This shows higher severity has a lower mean temperature
    # freeze_df, hotter_df = df[df["Temperature(F)"].astype(int) < 38], df[df["Temperature(F)"].astype(int) >= 38]


    # Graph 7: double bar chart for seveirty and freeze
    # freeze_df, hotter_df = df.loc[(pd.to_numeric(df['Temperature(F)'],errors='coerce')) < 38], df.loc[(pd.to_numeric(df['Temperature(F)'],errors='coerce')) >= 38]
    # y_values_freeze = plot__relative_feature_histogram(freeze_df, 'Severity')
    # y_values_hot =  plot__relative_feature_histogram(hotter_df, 'Severity') 
    # x = np.arange(len(["2","3","4"]))
    # width = 0.3
    # fig, ax = plt.subplots()
    # bar1 = ax.bar(x - width/2, y_values_freeze, label="Below", width=0.3)
    # bar2 = ax.bar(x + width/2, y_values_hot, label="Above", width=0.3)
    # ax.set_xticks(x)
    # ax.set_xticklabels(["2", "3", "4"])
    # ax.legend()
    # ax.bar_label(bar1, padding=2)
    # ax.bar_label(bar2, padding=2)
    # plt.show()

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

    # Graph 3 v2:
    # nr_of_weather = df["Weather_Condition"].value_counts()
    # grouped_by_severity = df[["Weather_Condition", "Severity"]].groupby("Severity").value_counts()
    # keyList = ["No Rain", "Overcast", "Rain", "Light rain", "Heavy Rain", "Light Freezing Drizzle", "Light Drizzle", "Heavy Drizzle", "Drizzle"]
    # result_values = []
    # for key in keyList:
    #     try:
    #         new_value = round(grouped_by_severity[(4, key)] / nr_of_weather[key]* 100, 2)
    #         result_values.append(new_value)
    #     except:
    #         result_values.append(0)
    # x = np.arange(len(keyList))
    # width = 0.3
    # fig, ax = plt.subplots()
    # bar1 = ax.bar(x, result_values, label="Severity 4 percentage", width=0.3)
    # ax.set_xticks(x)
    # ax.set_xticklabels(keyList)
    # ax.legend()
    # plt.xticks(rotation='vertical')
    # ax.bar_label(bar1, padding=2)
    # plt.show()

    # Graph 3 v3:
    # nr_of_weather = df["Weather_Condition"].value_counts()
    # grouped_by_severity = df[["Weather_Condition", "Severity"]].groupby("Severity").value_counts()
    # keyList = ["No Rain", "Overcast", "Rain", "Light rain", "Drizzle","Light Freezing Drizzle", "Light Drizzle", "Heavy Drizzle", "Heavy Rain"]
    # result_values = []
    # for key in keyList:
    #     try:
    #         new_value = round(grouped_by_severity[(4, key)] / nr_of_weather[key]* 100, 2) + round(grouped_by_severity[(3, key)] / nr_of_weather[key]* 100, 2)
    #         result_values.append(new_value)
    #     except:
    #         result_values.append(0)
    # new_keyList = ["No Rain", "Some Rain", "Heavy Rain"]
    # new_results = [
    #     (result_values[0] + result_values[1]) / 2,
    #     (result_values[2] + result_values[3] + result_values[4] + result_values[5] + result_values[6]) / 5,
    #     (result_values[7] + result_values[8]) / 2
    # ]
    # x = np.arange(len(new_keyList))
    # width = 0.3
    # fig, ax = plt.subplots()
    # bar1 = ax.bar(x, new_results, label="% High severity", width=0.3)
    # ax.set_xticks(x)
    # ax.set_xticklabels(new_keyList)
    # ax.legend()
    # plt.xticks(rotation='vertical')
    # ax.bar_label(bar1, padding=2)
    # plt.show()


    # Graph nr 4: 
    # features = ["Bump", "Crossing", "Give_Way", "Junction", "No_Exit", "Railway", "Roundabout", "Stop",  "Traffic_Signal"]
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

    # Graph 4 v2:
    # result_values = []
    # keyList = ["Bump", "Crossing", "Give_Way", "Junction", "No_Exit", "Railway", "Roundabout", "Stop",  "Traffic_Signal"]
    # for feature in keyList:
    #     rslt_df = df[df[feature] == True]
    #     feature_result = rslt_df[[feature, "Severity"]].groupby("Severity").value_counts()
    #     try:
    #         new_value = round(feature_result[(4, True)] / len(rslt_df)* 100, 2)
    #         result_values.append(new_value)
    #     except:
    #         # print('New line')
    #         # print(feature_result[Severity == 4])
    #         result_values.append(0)
    # x = np.arange(len(keyList))
    # width = 0.3
    # fig, ax = plt.subplots()
    # bar1 = ax.bar(x, result_values, label="Severity 4 percentage", width=0.3)
    # ax.set_xticks(x)
    # ax.set_xticklabels(keyList)
    # ax.legend()
    # plt.xticks(rotation='vertical')
    # ax.bar_label(bar1, padding=2)
    # plt.show()

    # Graph 5:
    street_df = pd.DataFrame(df['Street'].value_counts()).reset_index().rename(columns={'index':'Street No.', 'Street': 'Cases'})
    top_ten_streets_df = pd.DataFrame(street_df.head(10))
    print(top_ten_streets_df)
    top_ten_streets_df.plot(kind = 'bar',
        x = 'Street No.',
        y = 'Cases', ax = plt.gca())
    plt.show()

    # Find states
    # print(df["State"].unique())

if __name__ == "__main__":
    main()


