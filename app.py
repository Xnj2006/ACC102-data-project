import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import plotly.express as px

st.set_page_config(page_title="Fortune 500 Mini Analyzer", layout="wide")
st.title("Fortune 500 Dataset Analyzer")
st.subheader("the Top 30 in the World's Top 500 List")

df = pd.read_csv("fortune_500_small.csv")

with st.expander("View Raw Dataset"):
    st.dataframe(df)

st.sidebar.header("Filters")
industry_list = sorted(df["Industry"].unique())
selected_industry = st.sidebar.multiselect("Select Industry", industry_list, default=industry_list)
country_list = sorted(df["Country"].unique())
selected_country = st.sidebar.multiselect("Select Country", country_list, default=country_list)

df_filtered = df[(df["Industry"].isin(selected_industry)) & (df["Country"].isin(selected_country))]

st.subheader("Filtered Results")
st.dataframe(df_filtered)

st.subheader("Key Statistics")
col1, col2, col3 = st.columns(3)
with col1:
    st.metric("Total Companies", len(df_filtered))
with col2:
    st.metric("Avg Revenue (m)", round(df_filtered["Revenue_m"].mean(), 2))
with col3:
    st.metric("Avg Profit (m)", round(df_filtered["Profit_m"].mean(), 2))

st.subheader("Revenue vs Profit Scatter Plot")
fig1, ax1 = plt.subplots(figsize=(10, 5))
ax1.scatter(df_filtered["Revenue_m"], df_filtered["Profit_m"], alpha=0.7)
ax1.set_xlabel("Revenue (million USD)")
ax1.set_ylabel("Profit (million USD)")
ax1.set_title("Revenue vs Profit")
st.pyplot(fig1)

st.subheader("Average Profit by Industry")
industry_profit = df_filtered.groupby("Industry")["Profit_m"].mean().sort_values(ascending=False)
fig2, ax2 = plt.subplots(figsize=(10, 5))
industry_profit.plot(kind="bar", ax=ax2, color="skyblue")
ax2.set_ylabel("Avg Profit (million USD)")
ax2.set_title("Average Profit per Industry")
plt.xticks(rotation=45, ha="right")
st.pyplot(fig2)

st.markdown("---")
st.subheader("🌍 National Distribution Analysis")
col1, col2 = st.columns(2)
with col1:
    country_counts = df_filtered['Country'].value_counts()
    fig_country_pie = px.pie(
        values=country_counts.values,
        names=country_counts.index,
        title="Company Distribution by Country",
        hole=0.3,
        color_discrete_sequence=px.colors.sequential.RdBu)
    st.plotly_chart(fig_country_pie, use_container_width=True)
   
with col2:
    country_industry = df_filtered.groupby(['Country', 'Industry'])['Revenue_m'].sum().reset_index()
    fig_country_bar = px.bar(
        country_industry,
        x='Country',
        y='Revenue_m',
        color='Industry',
        title="Income Distribution – By Country & Industry",
        labels={'Revenue_m': 'Total Revenue (million US dollars)', 'Country': 'country'},
        barmode='stack'
    )
    st.plotly_chart(fig_country_bar, use_container_width=True)

st.markdown("---")
st.subheader("🌐 Country Comparison")

country_stats = df.groupby("Country").agg(
    Number_of_Companies=("Company", "count"),
    Average_Profit=("Profit_m", "mean")
).sort_values(by="Average_Profit", ascending=False)

with st.expander("📋 Country Statistics"):
    st.dataframe(country_stats)

st.write("**Average Profit Comparison by Country**")
fig3, ax3 = plt.subplots(figsize=(12, 5))
country_stats["Average_Profit"].plot(kind="bar", ax=ax3, color="lightgreen")
ax3.set_title("Average Profit by Country")
ax3.set_ylabel("Average Profit (million USD)")
plt.xticks(rotation=45, ha="right")
plt.tight_layout()
st.pyplot(fig3)

st.markdown("---")
st.subheader("📊 Profit Margin Analysis")

df["Profit_Margin"] = df["Profit_m"] / df["Revenue_m"] * 100
top_margin = df[["Company", "Profit_Margin"]].sort_values(by="Profit_Margin", ascending=False).head(10)

with st.expander("📋 Top 10 Companies by Profit Margin"):
    st.dataframe(top_margin)

st.write("**Top 10 Companies by Profit Margin**")
fig4, ax4 = plt.subplots(figsize=(12, 5))
ax4.bar(top_margin["Company"], top_margin["Profit_Margin"], color='orange')
ax4.set_title("Top 10 Companies by Profit Margin (%)")
ax4.set_ylabel("Profit Margin (%)")
plt.xticks(rotation=45, ha="right")
plt.tight_layout()
st.pyplot(fig4)


st.markdown("---")
st.subheader("🏭 Industry Revenue Analysis")

st.write("**Top 5 Companies by Revenue in Each Industry**")

selected_industry_for_top5 = st.selectbox(
    "Select the Industry You Want to View",
    sorted(df["Industry"].unique())
)

if selected_industry_for_top5:
    industry_data = df[df["Industry"] == selected_industry_for_top5]
    top5_companies = industry_data.nlargest(5, "Revenue_m")[["Company", "Revenue_m", "Profit_m"]]

    st.write(f"**{selected_industry_for_top5} Top 5 Companies by Revenue in Each Industry**")
    st.dataframe(top5_companies)
    
    fig5, ax5 = plt.subplots(figsize=(10, 5))
    ax5.bar(top5_companies["Company"], top5_companies["Revenue_m"], color='steelblue', alpha=0.7)
    ax5.set_title(f"Top 5 Companies in {selected_industry_for_top5} by Revenue")
    ax5.set_ylabel("Revenue (million USD)")
    plt.xticks(rotation=45, ha="right")
    plt.tight_layout()
    st.pyplot(fig5)
    
    fig6, (ax6_1, ax6_2) = plt.subplots(1, 2, figsize=(14, 5))
    
    ax6_1.bar(top5_companies["Company"], top5_companies["Revenue_m"], color='steelblue', alpha=0.7)
    ax6_1.set_title("Revenue Comparison")
    ax6_1.set_ylabel("Revenue (million USD)")
    ax6_1.tick_params(axis='x', rotation=45)
    
    ax6_2.bar(top5_companies["Company"], top5_companies["Profit_m"], color='coral', alpha=0.7)
    ax6_2.set_title("Profit Comparison")
    ax6_2.set_ylabel("Profit (million USD)")
    ax6_2.tick_params(axis='x', rotation=45)
    
    plt.tight_layout()
    st.pyplot(fig6)

st.markdown("---")
st.subheader("📈 Data Summary")

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric("Overall Profit Margin Range", f"{df['Profit_Margin'].min():.1f}% - {df['Profit_Margin'].max():.1f}%")

with col2:
    avg_margin = df['Profit_Margin'].mean()
    st.metric("Average Profit Margin", f"{avg_margin:.1f}%")

with col3:
    top_country = country_stats.index[0]
    top_country_profit = country_stats.iloc[0]["Average_Profit"]
    st.metric("Top Countries by Average Profit", f"{top_country} (${top_country_profit:.1f}M)")

with col4:
    top_industry_by_count = df['Industry'].value_counts().index[0]
    st.metric("Industry with Most Companies", top_industry_by_count)

st.markdown("---")
st.subheader("🔍 Advanced Filter")

margin_min, margin_max = st.slider(
    "Choose Profit Margin Range (%)",
    min_value=float(df['Profit_Margin'].min()),
    max_value=float(df['Profit_Margin'].max()),
    value=(0.0, float(df['Profit_Margin'].max())),
    step=0.1
)

revenue_min, revenue_max = st.slider(
    "Select Revenue Range (in millions of USD)",
    min_value=float(df['Revenue_m'].min()),
    max_value=float(df['Revenue_m'].max()),
    value=(float(df['Revenue_m'].min()), float(df['Revenue_m'].max())),
    step=10.0
)

filtered_df = df[
    (df['Profit_Margin'] >= margin_min) & 
    (df['Profit_Margin'] <= margin_max) &
    (df['Revenue_m'] >= revenue_min) & 
    (df['Revenue_m'] <= revenue_max)
]

st.write(f"Filter Results: {len(filtered_df)} country/countries")
st.dataframe(filtered_df.head(10))

if len(filtered_df) > 0:
    st.write("**Filter Results Summary:**")
    col1, col2, col3 = st.columns(3)
    with col1:
        st.metric("Average Revenue", f"${filtered_df['Revenue_m'].mean():,.1f}M")
    with col2:
        st.metric("Average Profit", f"${filtered_df['Profit_m'].mean():,.1f}M")
    with col3:
        st.metric("Average Profit Margin", f"{filtered_df['Profit_Margin'].mean():.1f}%")