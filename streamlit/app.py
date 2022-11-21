import streamlit as st
import numpy as np
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import os

st.set_page_config(layout="wide")
st.title('Employee Attrition Analysis')

st.markdown("""If you’re wondering why employees tend to leave organizations, you’ll mostly get answers related to “low paycheck“ but is that really the case? 
By using a dataset created by IBM data scientists, you’ll understand the real reasons of why employees leave the org! 
The data consists of nearly 1,500 current and former employees with information related to their monthly income, work life balance, experience, job role etc., 
with about 18% of the dataset covering attrition cases, of which half is coming from employees in R&D followed by sales.""")


st.markdown("""Based on the visualizations, we noticed that employees early in their career tend to leave the company after less than 4 years. 
Employees with experience ≤4 years have a 32% attrition rate compared to people with more experience. 
By analyzing the age factor, we’ve also found that younger aged employees are more likely to leave the organization than older people, 
ages between 25 & 35 with 47% attrition rate, indicates that older people choose to stay.""")



# uploaded_file = st.file_uploader("Choose a file")
# if uploaded_file is not None:
#   df = pd.read_csv(uploaded_file)
#   st.write(df)

df = pd.read_csv("HREmployeeAttrition.csv")

fig = px.histogram(df, x="JobRole", height= 500, text_auto='.2s', color = 'Department', color_discrete_sequence=px.colors.qualitative.Set2,
  title = 'Count distributions of the Job Roles and Departments')
st.plotly_chart(fig)
st.caption("""most employees work as sales executives, research scientists and lab technicians
at the Research & Development department""", unsafe_allow_html=False)


fig3 = px.histogram(df, x="Gender", height= 500, text_auto='.2s', color = 'Attrition', color_discrete_sequence=px.colors.qualitative.Set2,
                   title = 'Count distribution of the gender vs attrition')
st.plotly_chart(fig3)
st.caption("""Males are more likely to leave the company = hire more females""", unsafe_allow_html=False)


fig2 = px.histogram(df, x="Age",nbins=20, color='Attrition',
title ="A distribution of employees age range based on the attrition")
st.plotly_chart(fig2)
st.caption("""Most employees who attrite are in age range between 25-35 while most employees > 35""", unsafe_allow_html=False)


fig4 = px.histogram(df, x="TotalWorkingYears",nbins=20, color='Attrition', 
title ="A distribution of employees' total working years based on the attrition")
st.plotly_chart(fig4)
st.caption("""Employees working 5-10 years have a higher attrition rate than employees working > 10 years""", unsafe_allow_html=False)


ncwrd_att=df.groupby(['TotalWorkingYears','Attrition']).apply(lambda x:x['DailyRate'].count()).reset_index(name='Counts')
fig5 = px.area(ncwrd_att,x='TotalWorkingYears',y='Counts',color='Attrition',title='Working experience vs Attrition')
st.plotly_chart(fig5)
st.caption("""Employees who started their career with the company have a higher chance of leaving the organization
 to a different company while people who have gained experience working in multiple companies stay.""", unsafe_allow_html=False)

man_att=df.groupby(['YearsWithCurrManager','Attrition']).apply(lambda x:x['DailyRate'].count()).reset_index(name='Counts')
fig6 = px.line(man_att,x='YearsWithCurrManager',y='Counts',color='Attrition',title='Count of spent years in a company with a manager vs attrition')
st.plotly_chart(fig6)
st.caption("""The count of employees resigning at their first years is higher than when the relative time spend with a manager is very high,
 people are satisfied with their work. Therefore the chances of an employee resigning is significantly low.""", unsafe_allow_html=False)

sats_att=df.groupby(['JobSatisfaction','Attrition']).apply(lambda x:x['DailyRate'].count()).reset_index(name='Counts')
fig7 = px.area(sats_att,x='JobSatisfaction',y='Counts',color='Attrition',title='Count of the job satisfaction level in an organization')
st.plotly_chart(fig7)
st.caption("""The satisfaction ratings slightly decreases with the chances of people leaving the organization. However, as we move from 2-3,
people tend to move on to get better opportunities and experiences.
The attrition rate is almost stagnant for the higher satisfaction levels.""", unsafe_allow_html=False)








