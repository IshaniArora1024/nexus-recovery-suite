import pandas as pd
from textblob import TextBlob

# 1. Load your 20 reviews
df = pd.read_csv("reviews.csv")

def calculate_priority(row):
    # Detect emotion (-1 is very angry, 1 is very happy)
    analysis = TextBlob(str(row['Review_Text']))
    sentiment = analysis.sentiment.polarity
    
    # Consultancy Logic: VIPs with bad experiences get "CRITICAL" status
    if sentiment < 0 and row['Past_Purchases'] > 15:
        return "1 - CRITICAL (VIP Recovery)"
    elif sentiment < -0.2:
        return "2 - High Priority"
    elif sentiment > 0.5:
        return "4 - Low (Happy Customer)"
    else:
        return "3 - Medium Priority"

# 2. Apply the logic to every row
df['Priority_Level'] = df.apply(calculate_priority, axis=1)

# 3. Display the Results
print("\n--- CUSTOMER PRIORITY QUEUE ---")
# This sorts the list so the most urgent cases are at the top
print(df[['Customer_Name', 'Priority_Level', 'Customer_Tier']].sort_values(by="Priority_Level"))