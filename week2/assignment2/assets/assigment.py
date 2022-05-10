def proportion_of_education():
    import pandas as pd
    df = pd.read_csv('NISPUF17.csv', index_col=0)
    count1 = 0
    count2 = 0
    count3 = 0
    count4 = 0
    for num, values in df['EDUC1'].iteritems():
        if values == 1:
            count1 += 1
        if values == 2:
            count2 += 1
        if values == 3:
            count3 += 1
        if values == 4:
            count4 += 1
    total = len(df['EDUC1'])
    result = {
        "less than high school": count1 / total,
        "high school": count2 / total,
        "more than high school but not college": count3 / total,
        "college": count4 / total
    }
    return result


print(proportion_of_education())


def average_influenza_doses():
    import pandas as pd
    df = pd.read_csv('NISPUF17.csv', index_col=0)
    total1 = len(df[df['CBF_01'] == 1])
    total2 = len(df[df['P_NUMFLU'] == 2])
    x = df[df['CBF_01'] == 1]['P_NUMFLU'].sum()
    y = df[df['CBF_01'] == 2]['P_NUMFLU'].sum()
    result = (x / total1, y / total2)
    return result


print(average_influenza_doses())


def chickenpox_by_sex():
    import pandas as pd
    df = pd.read_csv('NISPUF17.csv', index_col=0)
    df = df[df['P_NUMVRC'] >= 1]
    x = df[df['HAD_CPOX'] == 1]
    y = df[df['HAD_CPOX'] == 2]
    maleinf = len(x[x['SEX'] == 1])
    malenotinf = len(y[y['SEX'] == 1])
    fameinf = len(x[x['SEX'] == 2])
    famenotinf = len(y[y['SEX'] == 2])
    result = {'male': maleinf / malenotinf, 'female': fameinf / famenotinf}
    return result


print(chickenpox_by_sex())


def corr_chickenpox():
    import scipy.stats as stats
    import pandas as pd
    df = pd.read_csv('NISPUF17.csv', index_col=0)
    df = df[['HAD_CPOX', 'P_NUMVRC']]
    df = df[df['HAD_CPOX'] <= 3]
    df = df[df['P_NUMVRC'].notna()]
    corr, pval = stats.pearsonr(df['HAD_CPOX'], df['P_NUMVRC'])
    return corr


print(corr_chickenpox())
