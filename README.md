# The Rossmann Sales Forecast

![Sales Forescast](img/800px-Dirk_Rossmann_GmbH.jpg)

# Business Problem

Dirk Rossmann GmbH is one of the largest drug store chains in Europe with around 56,200 employees and more than 4000 stores across Europe. Currently, Rossmann store managers are tasked with predicting their daily sales for up to six weeks in advance. Store sales are influenced by many factors, including promotions, competition, school and state holidays, seasonality, and locality. With thousands of individual managers predicting sales based on their own experiences, the accuracy of results can be quite varied.

# The Solution Strategy

Data Science team develop a Machine Learning Model that predict with a good accuracy in sales forecast and be easier to consult (on the telegram or on the web application).

**Step 01. Data Description** : Using statics metrics to describe our data.

**Step 02. Feature Engieneering** : based on step 01 create new features on the original that better describe the sales.

**Step 03. Exploratory Data Analysis** : Explore data to find insights and the features that better describe the stores sales.

**Step 04. Feature Selection** : Select the most importante feature to train the machine learning model.

**Step 05. Machine Learning Models** : Creating some Machine Learning models to search the best model for the project

**Step 06. Tunning Hyper Parameters** : Find the best values of each parameter of the selected Model.

**Step 07. Convert Model Performance to Business Values** : Convert the performance of the Machine Learning model into a business result.


# The Dataset

The dataset is available on kaggle plataform(https://www.kaggle.com/c/rossmann-store-sales/data).


# Top Data Insights 


Sales grow more the shorter the distance to a competitor. 

![salesByCompetitionDistance](img/sales_by_competition_distance.PNG)

Sales grow more to store types "A" and "D". 
Sales grow more in public Holidays.
Sales grow more to smaller assortment.

![sales](img/sales_by_store_type_hollidays.PNG)


## Machine Learning Models

I used in this step the models:
* Average - Baseline
* Linear Regression
* Lasso Regression
* Random Forest Regressor
* XGBoost Regressor

The perfromance result indicate that i continue with XGBoost and Random Forest Models.


## Models Performance

XGBoost presents the best performance and time of execution, with a accuracity of **98.1%**.

![xgboostFinalPerformance](img/xgboostFinalPerformance.PNG)


## Convert Model Performance to Business Values

In test data, I calcuted the prediction and comparision with the worst and better cenaries. The model brings a safety data to the CEO decision to sales reform investiment.

![businessPerformance](img/businessPerformance.PNG)

# Next Steps
* Workshop for the Bussiness Users.
* collect feedback about the Model's useability.
* Improve in 10% the Model's accuracy.


# Contact

Email: danilofelipeneto@gmail.com

Linkedin: https://www.linkedin.com/in/danilo-felipe-neto-972b45120/
