import streamlit as st
from expense_analyzer import analyze_expenses

st.title("💰 Personal Expense Analyzer")

uploaded_file = st.file_uploader("Upload Expenses CSV", type="csv")
if uploaded_file:
    category_spending, monthly_spending, recommendations = analyze_expenses(uploaded_file)
    
    st.subheader("📊 Spending by Category")
    st.bar_chart(category_spending)  # Uses Streamlit's native chart (no matplotlib needed)
    
    st.subheader("📅 Monthly Spending Trend")
    st.line_chart(monthly_spending)
    
    st.subheader("💡 Smart Savings Tips")
    if recommendations:
        for tip in recommendations:
            st.success(tip)
    else:
        st.info("No savings recommendations yet. Keep tracking expenses!")