\ README.md

\ Fortune 500 Mini Analyzer – ACC102 Track4

An interactive financial analytics tool built with Streamlit for analyzing the top 30 Fortune Global 500 companies.



\ 1. Problem \& User

This tool helps business and accounting students explore key financial metrics (revenue, profit, profit margin) across industries and countries, enabling clear and visual comparison of corporate performance. The target user is ACC102 students and beginner business analysts.



\ 2. Data

Data Source: Fortune Global 500 2024, Fortune Media Limited  

Official website: https://fortune.com/global500/  

Accessed: April 16, 2026  

Key Fields:  

\- Company: Name of the company  

\- Industry: Industry category  

\- Revenue\_m: Annual revenue (million USD)  

\- Profit\_m: Annual profit (million USD)  

\- Country: Headquarters location  

\- Rank: Global 500 ranking by revenue  

\- Profit\_Margin: Profit percentage calculated from revenue and profit  



\ 3. Methods

\- Used pandas for data loading, filtering, and profit margin calculation  

\- Built interactive sidebar filters for industry and country  

\- Created visualizations with matplotlib and Plotly (scatter plots, bar charts, pie charts, stacked bar charts)  

\- Added dynamic top-5 company analysis per industry  

\- Built advanced filter by profit margin and revenue range  

\- Displayed key metrics and summary statistics in real time  



\ 4. Key Findings

\- Energy and Technology industries have the highest average profit and profit margin.  

\- Revenue and profit are not perfectly correlated — high revenue does not always mean high profit efficiency.  

\- The USA and China dominate the top 30 Fortune 500 list.  

\- Saudi Aramco, Apple, and Microsoft achieve the strongest profit margins.  

\- Industry structure strongly influences corporate profitability.  



\ 5. How to Run

1\. Install required libraries:

pip install streamlit pandas matplotlib plotly

2\. Run the application:

streamlit run app.py



\ 6. Product Link / Demo

&#x20; 



\ 7. Limitations \& Next Steps

Limitations:  

\- Only 30 companies are included, so results cannot represent the full Global 500.  

\- Only single-year data without historical trend comparison.  

\- No financial ratios like ROE or debt ratios included.  



Next steps:  

\- Add multi-year data for trend analysis.  

\- Include more financial indicators (ROE, profit margin trend).  

\- Enable chart export and PDF report generation.  

\- Support more industries and larger datasets.

