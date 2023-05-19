import pandas as pd
import numpy as np 
import datetime as dt


def percent_distribution(csv):
    '''
    This function is to acquire and prepare the percent distribution of the real estate data
    '''
    
    pct_distribution = pd.read_csv(csv)
    
    pct_distribution.columns = pct_distribution.iloc[0]
    pct_distribution.columns = pct_distribution.columns.astype('str')
    pct_distribution.rename(columns=lambda x: x.split(".")[0], inplace=True)
    pct_distribution = pct_distribution[1:]
    
    pct_distribution = pct_distribution.rename(columns={pct_distribution.columns[0]: 'price_range'})
    pct_distribution = pct_distribution.set_index('price_range')
    
    new_index = pct_distribution.index.tolist()
    last_index_value = pct_distribution.index[-1].split('$')[1]
    new_index[-1] = last_index_value
    pct_distribution.index = new_index
    
    pct_distribution.rename_axis('price_range', inplace=True)
    
    return pct_distribution


def sales(csv):
    '''
    This function is to acquire and prepare the monthly and annual sales data
    '''
    
    mon_anni_sales = pd.read_csv(csv)
    
    mon_anni_sales =  mon_anni_sales.rename(columns={'Date':'date', 'Sales':'sales',
                                                     'Dollar\nVolume':'dollar_volume', 
                                                     'Average\nPrice':'average_price', 
                                                     'Median\nPrice': 'median_price',
                                                     'Total\nListings':'total_listings',
                                                     'Months\nInventory':'months_inventory'})
    
    
    columns = ['sales', 'dollar_volume', 'average_price', 'median_price', 'total_listings']
    
    for col in columns:
        mon_anni_sales[col] = mon_anni_sales[col].str.replace(',','')
        mon_anni_sales[col] = mon_anni_sales[col].astype('int64')
    
    if mon_anni_sales.dtypes[0] == 'int64':
        
        return mon_anni_sales
    
    else:
        
        mon_anni_sales['date']= pd.to_datetime(mon_anni_sales['date'])
    
    
    return mon_anni_sales



