
#importing modules 

#import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


def bar_chart(df):
    '''
    Plotting the grouped bar chart to analyse and visualise the CO2 Emission 
    rate by countries over years
    '''
    # Plotting the grouped bar chart
    years = co2_df.columns[2:].tolist()
    #declaring bar_width variable for describing the bar width size
    bar_width = 0.15
    fig, ax = plt.subplots()

    for i, country_data in enumerate(df):
        x_pos = range(len(years))
        ax.bar([x + i*bar_width for x in x_pos], country_data, bar_width,
               label=countries[i])

    # plot bar chart, labels are used to produce the legend
    ax.set_xlabel('Year')
    ax.set_ylabel('CO2 Emissions (kt)')
    ax.set_title('CO2 Emissions by Country and Year')
    ax.set_xticks([x + (len(countries)-1)*bar_width / 2 for x in x_pos])
    ax.set_xticklabels(years)
    ax.legend(loc='upper left', bbox_to_anchor=(1, 1))
    plt.tight_layout()
    plt.show()
    return


def line_plot(df,countries):
    '''
    Plotting the grouped line plot to analyse and visualise the Agricultural 
    nitrous oxide emissions rate by countries over years
    
    '''
    # Extract relevant columns for plotting
    years = df.columns[2:]

    # Plotting the line plot
    plt.figure(figsize=(12, 6))
    for country in countries:
        country_data = df[df["Country Name"] == country]
        plt.plot(years, country_data.iloc[0, 2:], label=country)
        
    # plot line plot, labels are used to produce the legend
    plt.xlabel("Year")
    plt.ylabel("Agricultural nitrous oxide emissions (thousand metric tons of CO2 equivalent)")
    plt.title("Agricultural nitrous oxide emissions by countries over the years")
    plt.legend(loc='upper left', bbox_to_anchor=(1, 1))
    plt.show()
    return


def heatmap(df):
    '''
    Plotting the grouped correlation plot to analyse and visualise by 
    countries over years
    
    '''
    # Extract relevant columns for the heatmap
    #countries = df["Country Name"]
    years = df.columns[2:]

    # Create a pivot table for the heatmap
    heatmap_data = df.pivot(index="Country Name", columns="Series Name", 
                             values=years[0])

    # Plotting the heatmap with values and gridlines
    plt.figure(figsize=(14, 8))
    sns.heatmap(heatmap_data.corr(), cmap="YlGnBu", annot=True, fmt=".1f", linecolor="black", linewidth=1)
    plt.title("Correlation Heatmap")
    plt.xlabel("")
    plt.ylabel("")
    plt.show()
    return()

    
#importing data from csv file
df=pd.read_csv("Data.csv")
#Droping the unwanted shells to get the proper data by cleanig the dataset
df.drop(["Country Code", "Series Code", "2021 [YR2021]", "2022 [YR2022]"], axis=1, inplace=True)
df2 = df
df2.drop(["2008 [YR2008]", "2009 [YR2009]", "2010 [YR2010]"], axis=1, inplace=True)

#Renaming the column names for easy readable purpose
df.rename(columns={"2008 [YR2008]":"2008","2009 [YR2009]":"2009", "2010 [YR2010]":"2010", "2011 [YR2011]":"2011", "2012 [YR2012]":"2012", "2013 [YR2013]":"2013", "2014 [YR2014]":"2014", "2015 [YR2015]":"2015", "2016 [YR2016]":"2016", "2017 [YR2017]":"2017", "2018 [YR2018]":"2018", "2019 [YR2019]":"2019", "2020 [YR2020]":"2020"}, inplace=True)


#Using describe function to get mean, median and standard for the dataset
print(df.describe())

# Filtering df2 to get only the CO2 emissions data
co2_df = df2[df2['Series Name'] == 'CO2 emissions (kt)']

# Get the countries and their CO2 emissions data
countries = co2_df['Country Name'].tolist()
co2_emissions_data = co2_df.iloc[:, 2:].values.tolist()

bar_chart(co2_emissions_data)

line_plot(df,countries)

heatmap(df)





