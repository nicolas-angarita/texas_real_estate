# <div align="center">Predicting Texas's Real Estate Prices</div>


![alt text](https://cosmic-s3.imgix.net/43a6a620-e671-11eb-b45e-251845c7c90f-TEXAS.png?auto=format&w=1920&q=20)

# Project Goals

 - Identify if there are any correlations between the metro areas in price and their features
 - Build a model to best predict the 4 major market prices in the next 6 months
 - Compare the 4 major markets to analyze and determine which markets are overpriced and which seem to still have an investable opportunity 

# Project Description

We are looking to build supervised machine learning models using time series analysis and regression, to best predict prices for Texas's major markets for the next 6 months. The major markets we are taking a look at are San Antonio-New Braunfels, Houston-Woodlands-Sugar Land, Austin-Round Rock, and Dallas-Fort Worth-Arlington. We plan to explore and find if there are any correlations between the features given in the dataset to help us predict price. The time frame we are looking at is from 01/01/1990 to 3/01/2023. After we have explored and made our models we will recommend to use the features provided in the data set or if new data will be needed to help predict the average price. We will also provide any usesful insights on interesting findings relating to investable opportunties.

# Initial Questions

 1. Does the average price of a metro area have a correlation with its features?
 2. Do metro areas have a relationship with other metro areas?
 3. Which metro area looks like the best overall to invest in (underpriced compared to the other major markets)?


# The Plan

 - Create README with project goals, project description, initial hypotheses, planning of project, data dictionary, and come up with recommedations/takeaways

### Acquire Data
 - Acquire data from Yahoo Finance Library and dowload the historical data from BTC, DJI, & Gold. Create a function to later import the data into a juptyer notebook. (acquire.py)

### Prepare Data
 - Clean and prepare the data creating a function that will give me data that is ready to be explored upon. Within this step we will also write a function to split our data into train, validate, and test. (prepare.py) 
 
### Explore Data
- Create visuals on our data 

- Create at least two hypotheses, set an alpha, run the statistical tests needed, reject or fail to reject the Null Hypothesis, document any findings and takeaways that are observed.

### Model Data 
 - Create a baseline model of BTC (Moving Average model)
 
 - Create, Fit, Predict on train subset on 3 time series models.
 
 - Evaluate models on train and validate datasets.
 
 - Evaluate which model performs the best and on that model use the test data subset.
 
### Delivery  
 - Create a Final Report Notebook to document conclusions, takeaways, and next steps in recommadations for predicitng BTC's Price. Also, inlcude visualizations to help explain why the model that was selected is the best to better help the viewer understand. 


## Data Dictionary


| Target Variable |     Definition     |
| --------------- | ------------------ |
|      btc_price    | price of Bitcoin |

| Feature  | Definition |
| ------------- | ------------- |
| open | Opening price of the asset |
| high | The high price point of the asset  |
| low | The low price point of the asset |
| close | The closing price of the asset |
| adj close | The closing price after adjustments  |
| volume | The amount of an asset that changes hands | 
| dji_price | The price of the Dow Jones Industrial Average |
| gold | The price of gold per ounce|



## Steps to Reproduce

 - You will need to have the Yahoo Finance library downloaded to get the historical data of BTC, DJI, and Gold

- Clone my repo including the acquire.py, prepare.py, explore.py, and modeling.py 

- Put the data in a file containing the cloned repo.

- Run notebook.

## Conclusions

**Bitcoin price predictions were used by minimizing RMSE within our models. Both DJI and Gold prove to have mild to strong correlations with BTC's price.**


 
**Best Model's performance:<br>**
**- My best model reduced the root mean squared error by 3,974 dollars compared to the baseline results.**

**- RMSE 9280.0 dollars on in-sample (train), RMSE 9280.0 dollars on out-of-sample data (validate) and RMSE of 27436.26 dollars on the test data.**

## Recommendations
- I would recommend gathering more data from BTC's inception of trading.

- I would also recommend collecting data or finding more correlations to BTC's price, as predicitng price on just BTC historical data is not optimal. This is a good base to better understand the historical price, but a multivariate time series model would have to be made to get better predictions.
## Next Steps

- Find more correlations to better predict BTC price (DXY to BTC price)

- Consider adding different hyperparameters to models for better results
    
- Take this data and build multivariate models
