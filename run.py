#! /usr/bin/env python3

import os

import pandas as pd

from langchain.agents import create_csv_agent
from langchain.chat_models import ChatOpenAI
import warnings
warnings.filterwarnings("ignore")

# Column name mapping generated using ChatGPT
column_mapping = {
    "AcceptedCmp1": "Accepted_Offer_In_First_Campaign",
    "AcceptedCmp2": "Accepted_Offer_In_Second_Campaign",
    "AcceptedCmp3": "Accepted_Offer_In_Third_Campaign",
    "AcceptedCmp4": "Accepted_Offer_In_Fourth_Campaign",
    "AcceptedCmp5": "Accepted_Offer_In_Fifth_Campaign",
    "Response": "Accepted_Offer_In_Last_Campaign",
    "Complain": "Complained_In_Last_2_Years",
    "DtCustomer": "Enrollment_Date_With_Company",
    "Education": "Customer_Education_Level",
    "Marital": "Customer_Marital_Status",
    "Kidhome": "Number_Of_Small_Children_In_Household",
    "Teenhome": "Number_Of_Teenagers_In_Household",
    "Income": "Yearly_Household_Income",
    "MntFishProducts": "Amount_Spent_On_Fish_Products_Last_2_Years",
    "MntMeatProducts": "Amount_Spent_On_Meat_Products_Last_2_Years",
    "MntFruits": "Amount_Spent_On_Fruits_Last_2_Years",
    "MntSweetProducts": "Amount_Spent_On_Sweet_Products_Last_2_Years",
    "MntWines": "Amount_Spent_On_Wines_Last_2_Years",
    "MntGoldProds": "Amount_Spent_On_Metal_Gold_Products_Last_2_Years",
    "NumDealsPurchases": "Number_Of_Purchases_With_Discount",
    "NumCatalogPurchases": "Number_Of_Purchases_Using_Catalogue",
    "NumStorePurchases": "Number_Of_Purchases_Made_In_Stores",
    "NumWebPurchases": "Number_Of_Purchases_Made_Through_Website",
    "NumWebVisitsMonth": "Number_Of_Website_Visits_In_Last_Month",
    "Recency": "Days_Since_Last_Purchase"
}

def repl():
   while True:
       try:
           user_question = input("user> ")
   
           if not user_question:
               continue
   
           if user_question == 'exit':
               print("agent> Bye!")
               break
   
           answer = agent.run(user_question)
           print("agent> " + answer)
       except KeyboardInterrupt:
           print("agent> Bye!")
           break

def delete_if_exists(path):
    try:
        os.remove(path)
    except:
        pass

def rewrite_columns():
    delete_if_exists('dataset_final.csv')
    df = pd.read_csv('dataset.csv')
    df = df.rename(columns=column_mapping)
    df.to_csv('dataset_final.csv', index=False)

rewrite_columns()
agent = create_csv_agent(ChatOpenAI(temperature=0, model_name="gpt-4"), 'dataset_final.csv', verbose=False, handle_parsing_errors=True)

repl()



    