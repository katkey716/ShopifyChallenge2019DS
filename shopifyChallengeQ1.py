#import the libraries needed 
import pandas as pd
import numpy as np

#loading the dataset into the dataframe from my github where I saved and renamed the csv
path_name = 'https://raw.githubusercontent.com/katkey716/ShopifyChallenge2019DS/main/Q1_dataset.csv'
shopifydf = pd.read_csv(path_name)
shopifydf.head()
print(f'Previously calculated AOV: $',shopifydf['order_amount'].mean(), sep='')#this was just to make sure I was on the right track how the previous number was gotten

#defining and removing the outliers that may skew the data
def defining_outliers():
    Q1 = np.percentile(shopifydf['order_amount'], 25, method='midpoint')
    Q3 = np.percentile(shopifydf['order_amount'], 75, method='midpoint')
    IQR = Q3 - Q1 #innerquartile range is what we want to stay between
    upper_limit = Q3+1.5*IQR
    lower_limit = Q1-1.5*IQR
    upper_bound = np.where(shopifydf['order_amount'] >= upper_limit)#this is the upper limit so the highest i want the data number to go
    lower_bound = np.where(shopifydf['order_amount'] <= lower_limit)#this is the lowest i want the data numbers to go
    shopifydf.drop(upper_bound[0], inplace=True)#i want to drop all the data above the IQR range
    shopifydf.drop(lower_bound[0], inplace=True)#i want to drop all the data below the IQR range
    return shopifydf#i want to return the new dataframe after dropping the outliers

#calculate AOV with cleaned data minus outliers
def calculate_AOV():
    defining_outliers()#calling the function that cleans up my dataframe a bit
    AOV_exact = shopifydf['order_amount'].mean()#take the mean again minus the outliers
    AOV_rounded = "{:.2f}".format(AOV_exact)#format the number so that it is only rounded to two decimal points just like true cents
    return AOV_rounded

print("Corrected AOV: $",calculate_AOV(), sep='')#give the corrected AOV


