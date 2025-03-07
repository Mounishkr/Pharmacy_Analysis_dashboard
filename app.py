import streamlit as st
import pandas as pd
import plotly.express as px

# Streamlit app
def main():
    st.title("Pharma Sales Analysis Dashboard")
    st.sidebar.header("Upload Your Excel File")
    
    uploaded_file = st.sidebar.file_uploader("Upload Excel File", type=["xlsx"])
    
    if uploaded_file:
        df = pd.read_excel(uploaded_file, sheet_name="Sheet1")
        st.success("File uploaded successfully!")
        
        # Display raw data
        st.subheader("Raw Data Preview")
        st.dataframe(df.head())
        
        # Sales Overview (IP & OP)
        st.subheader("IP and OP Sales Overall Profit")
        sales_summary = df.groupby("Type")[["SALEVALUE", "Profit"]].sum().reset_index()
        st.dataframe(sales_summary)
        fig = px.bar(sales_summary, x="Type", y=["SALEVALUE", "Profit"], barmode="group", title="IP vs OP Sales & Profit")
        st.plotly_chart(fig)
        
        # OP Pharma Report
        st.subheader("OP Pharma Report")
        op_df = df[df["Type"] == "OP"]
        op_summary = op_df.groupby("Category")[["SALEVALUE", "Profit"]].sum().reset_index()
        st.dataframe(op_summary)
        fig_op = px.pie(op_summary, names="Category", values="SALEVALUE", title="OP Pharma Sales Distribution")
        st.plotly_chart(fig_op)
        
        # IP Pharma Report
        st.subheader("IP Pharma Report")
        ip_df = df[df["Type"] == "IP"]
        ip_summary = ip_df.groupby("Category")[["SALEVALUE", "Profit"]].sum().reset_index()
        st.dataframe(ip_summary)
        fig_ip = px.pie(ip_summary, names="Category", values="SALEVALUE", title="IP Pharma Sales Distribution")
        st.plotly_chart(fig_ip)
        
        # Specialty-wise Report
        st.subheader("Specialty-wise Sales Report")
        specialty_summary = df.groupby("SEPCIALITY")[["SALEVALUE", "Profit"]].sum().reset_index()
        st.dataframe(specialty_summary)
        fig_specialty = px.bar(specialty_summary, x="SEPCIALITY", y="SALEVALUE", title="Specialty-wise Sales Analysis")
        st.plotly_chart(fig_specialty)
        
        # Month-wise Sales Analysis
        st.subheader("Month-wise Sales Analysis")
        df["CREATEDT"] = pd.to_datetime(df["CREATEDT"])
        df["Month"] = df["CREATEDT"].dt.strftime('%Y-%m')
        month_summary = df.groupby("Month")["SALEVALUE"].sum().reset_index()
        st.dataframe(month_summary)
        fig_month = px.line(month_summary, x="Month", y="SALEVALUE", title="Monthly Sales Trend")
        st.plotly_chart(fig_month)
        
        # Doctor-wise Profit Analysis
        st.subheader("Doctor-wise Net Profit Analysis")
        doctor_summary = df.groupby("DOCTORNAME")["Profit"].sum().reset_index().sort_values(by="Profit", ascending=False)
        st.dataframe(doctor_summary)
        fig_doctor = px.bar(doctor_summary.head(10), x="DOCTORNAME", y="Profit", title="Top 10 Doctors by Net Profit")
        st.plotly_chart(fig_doctor)

if __name__ == "__main__":
    main()
