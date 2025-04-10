import pandas as pd
import matplotlib.pyplot as plt

def analyze_expenses(csv_file):
    df = pd.read_csv(csv_file)
    df['Date'] = pd.to_datetime(df['Date'])
    df['Month'] = df['Date'].dt.month_name()
    
    # Total spending per category
    category_spending = df.groupby('Category')['Amount'].sum().sort_values(ascending=False)
    
    # Monthly trends
    monthly_spending = df.groupby('Month')['Amount'].sum()
    
    # Savings recommendations (rule-based)
    recommendations = []
    if 'Dining' in category_spending.index and category_spending['Dining'] > 200:
        savings = category_spending['Dining'] * 0.1
        recommendations.append(f"💡 Reduce dining out by 10% to save **${savings:.2f}** this month.")
    
    if 'Entertainment' in category_spending.index and category_spending['Entertainment'] > 100:
        savings = category_spending['Entertainment'] * 0.15
        recommendations.append(f"🎬 Cut entertainment spending by 15% to save **${savings:.2f}** this month.")
    
    return category_spending, monthly_spending, recommendations