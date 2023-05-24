import pandas as pd
import numpy as np 
import seaborn as sns
import matplotlib.pyplot as plt
from datetime import datetime, timedelta 
from scipy.stats import pearsonr



def time_df(df):
    df.set_index('date', inplace = True)
    return df


def comparing_markets(mkt1,mkt2,mkt3,mkt4, keys = ['name1', 'name2', 'name3', 'name4']):
    markets = [mkt1,mkt2,mkt3,mkt4]
    
    concat_markets = []
    for market in markets:
        df = time_df(market)
        concat_markets.append(df['average_price'])  

    df = pd.concat(concat_markets, axis=1, 
    keys = keys)
    
    return df


def create_market_subplots(markets, titles):
    num_markets = len(markets)
    num_rows = (num_markets - 1) // 2 + 1
    num_cols = min(num_markets, 2)
    
    fig, axs = plt.subplots(num_rows, num_cols, figsize=(10, 8))

    for i, market in enumerate(markets):
        row = i // num_cols
        col = i % num_cols
        ax = axs[row, col]
        sns.regplot(data=market, x='sales', y='average_price', line_kws={'color': 'red'}, ax=ax)
        ax.set_title(titles[i])

    plt.tight_layout()
    plt.show()
    
    
def plot_market_home_prices(df, title, x_label, y_label, figsize=(12, 8), palette=None, linestyle='-', dashes=False):
    sns.set_style('whitegrid')
    sns.set_palette(palette)

    plt.figure(figsize=figsize)
    sns.lineplot(data=df, linestyle=linestyle, dashes=dashes)

    plt.title(title, fontsize=20)
    plt.xlabel('')
    plt.ylabel(f'{y_label} ($)', fontsize=17)  # Include currency symbol in y-axis label
    plt.xticks(fontsize=15)
    plt.yticks(fontsize=15)

    plt.legend(df.columns, fontsize=15)

    sns.despine()
    plt.tight_layout()
    
    plt.show()
    
    