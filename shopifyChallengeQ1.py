import pandas as pd
import numpy as np

#loading the dataset into the dataframe
path_name = 'https://raw.githubusercontent.com/katkey716/ShopifyChallenge2019DS/main/Q1_dataset.csv'
shopifydf = pd.read_csv(path_name)
shopifydf.head()
print(f'Previously calculated AOV: $',shopifydf['order_amount'].mean(), sep='')

#defining and removing the outliers that may skew the data
def defining_outliers():
    Q1 = np.percentile(shopifydf['order_amount'], 25, method='midpoint')
    Q3 = np.percentile(shopifydf['order_amount'], 75, method='midpoint')
    IQR = Q3 - Q1 #innerquartile range is what we want to stay between
    upper_limit = Q3+1.5*IQR
    lower_limit = Q1-1.5*IQR
    upper_bound = np.where(shopifydf['order_amount'] >= upper_limit)
    lower_bound = np.where(shopifydf['order_amount'] <= lower_limit)
    shopifydf.drop(upper_bound[0], inplace=True)
    shopifydf.drop(lower_bound[0], inplace=True)
    return shopifydf

#calculate AOV with cleaned data minus outliers
def calculate_AOV():
    defining_outliers()
    AOV_exact = shopifydf['order_amount'].mean()
    AOV_rounded = "{:.2f}".format(AOV_exact)
    return AOV_rounded

print("Corrected AOV: $",calculate_AOV(), sep='')


