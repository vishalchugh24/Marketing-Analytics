''' Case Study: Customer Persona for "TrendMart"
Background
TrendMart is a retail & e-commerce lifestyle brand aiming to personalize marketing strategies.
They have collected both quantitative (demographics, shopping behavior) and qualitative (goals, challenges, lifestyle) customer data.

The marketing team wants to group customers into distinct personas to:

Target promotions effectively

Choose the right communication channels

Improve customer retention

Your Task
You are a Marketing Analyst at TrendMart.
Using the provided datasets:

customer_persona_dataset-Quantitative.xlsx

customer_persona_details_qualitative.xlsx

You need to answer the following beginner-friendly Python coding questions.

Questions
Part 1: Data Preparation
Import both datasets in Python and merge them using Customer_ID as the key.

Display the first 5 rows of the merged dataset.

Part 2: Persona Grouping by Demographics
Group customers by Location (Urban/Rural) and find the average Annual Income.

Find the most common Communication Preference for Urban customers.

Group customers by Technology Usage and calculate the average Online Purchase Frequency.

Part 3: Persona Grouping by Qualitative Data
Find the number of customers whose Goals and Aspirations is "Career growth".

Group customers by Lifestyle and values and find the average Annual Income.

Find the most common Decision-Making trigger for customers with High Technology Usage.

Part 4: Combined Segmentation
Create a segment of customers who are:

Urban

Annual Income > ₹1,000,000

Technology Usage = "High"
Display their Name, Age, Occupation, and Goals.

Count how many customers have "Discounts and offers" as their Decision-Making trigger and shop online more than 5 times '''

# Import Library
import pandas as pd

# 1. Import datasets
df_quant = pd.read_excel("customer_persona_dataset-Quantitative.xlsx")
df_qual = pd.read_excel("customer_persona_details_qualitative.xlsx")

# 2. Merge datasets
df = pd.merge(df_quant, df_qual, on="Customer_ID")

# 3. Group by Location and find avg income
df.groupby("Location")["Annual_Income"].mean()

# 4. Most common communication preference for Urban
df[df["Location"] == "Urban"]["Communication Preference"].mode()

# 5. Avg online purchases by tech usage
df.groupby("Technology Usage")["Online Purchase Frequency"].mean()

# 6. Count customers with Career growth goal
df[df["Goals and Aspirations"] == "Career growth"].shape[0]

# 7. Avg income by lifestyle
df.groupby("Lifestyle and values")["Annual_Income"].mean()

# 8. Most common trigger for high tech usage
df[df["Technology Usage"] == "High"]["Decision-Making triggers"].mode()

# 9. Filter Urban, High income, High tech usage
df[(df["Location"] == "Urban") &
   (df["Annual_Income"] > 1000000) &
   (df["Technology Usage"] == "High")][["Name", "Age", "Occupation", "Goals and Aspirations"]]

# 10. Count specific trigger and high online frequency
df[(df["Decision-Making triggers"] == "Discounts and offers") &
   (df["Online Purchase Frequency"] > 5)].shape[0]
