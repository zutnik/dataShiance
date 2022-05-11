def answer_one():
    # YOUR CODE HERE
    import pandas as pd
    import numpy as np
    data_excel = pd.ExcelFile('assets/Energy Indicators.xls')
    energy = pd.read_excel(data_excel, 0, skiprows=17, skip_footer=38)
    energy = energy[['Unnamed: 1', 'Petajoules', 'Gigajoules', '%']]

    energy.columns = ['Country', 'Energy Supply', 'Energy Supply per Capita', '% Renewable']
    energy['Energy Supply'].replace('...', np.nan, inplace=True)
    energy['Energy Supply'] = energy['Energy Supply'] * 1000000
    energy['Country'].replace({'Republic of Korea': 'South Korea',
                               'United States of America': 'United States',
                               'United Kingdom of Great Britain and Northern Ireland': 'United Kingdom',
                               'China, Hong Kong Special Administrative Region': 'Hong Kong'}, inplace=True)
    energy['Country'].replace(r' \(.*\)', '', regex=True, inplace=True)

    GDP = pd.read_csv('assets/world_bank.csv', skiprows=4)
    GDP['Country Name'].replace('Korea, Rep.', 'South Korea', inplace=True)
    GDP['Country Name'].replace('Iran, Islamic Rep.', 'Iran', inplace=True)
    GDP['Country Name'].replace('Hong Kong SAR, China', 'Hong Kong', inplace=True)

    GDP = GDP[['Country Name', '2006', '2007', '2008', '2009', '2010', '2011', '2012', '2013', '2014', '2015']]
    GDP.rename(columns={'Country Name': 'Country'}, inplace=True)

    ScimEn = pd.read_excel('assets/scimagojr-3.xlsx')
    ScimEn = ScimEn[:15]

    merge1 = pd.merge(ScimEn, energy, how='inner', left_on='Country', right_on='Country')
    final_df = pd.merge(merge1, GDP, how='inner', left_on='Country', right_on='Country')
    final_df = final_df.set_index('Country')
    return final_df
    raise NotImplementedError()
