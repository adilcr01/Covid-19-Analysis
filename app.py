import pandas as pd
import streamlit as st
import plotly.express as px



states=pd.read_csv('only_states_covid_data.csv')


st.title('Covid-19')
st.header('Track Covid-19 Cases')
st.subheader('Date: 20 Nov 2021')

selected_state = st.selectbox(
'Select a State',
[i for i in states['Name of State / UT']])


fig2=px.pie(states,values=[states[states['Name of State / UT'].isin([selected_state])]['Active Cases* Total'].values[0],
                                 states[states['Name of State / UT'].isin([selected_state])]['Cured/Discharged/Migrated* Cumulative'].values[0],
                                 states[states['Name of State / UT'].isin([selected_state])]['Deaths** Cumulative'].values[0]],
            names=['Total Active Cases','Total Recovered','Total Deaths'],
            hole=0.5)
fig2.update_layout(

title_text=str(selected_state)+" Covid Cases",

annotations=[dict(text='20 Nov 2021', x=0.24, y=0.5, font_size=18, showarrow=False)])





col1,  col2 = st.columns([2,1])

with col1:
   st.plotly_chart(fig2,use_container_width=True)
   col1.subheader("Pie-Chart")


with col2:
    st.subheader("Total Confirmed Cases")
    st.subheader(str(states[states['Name of State / UT'].isin([selected_state])]['Active Cases* Total'].values[0]+
                                 states[states['Name of State / UT'].isin([selected_state])]['Cured/Discharged/Migrated* Cumulative'].values[0]+
                                 states[states['Name of State / UT'].isin([selected_state])]['Deaths** Cumulative'].values[0]))
    st.subheader("New Covid Cases")
    st.subheader(str(states[states['Name of State / UT'].isin([selected_state])]['Active Cases* Change Since Yesterday'].values[0]))
    st.subheader("New Recovered Cases")
    st.subheader(str(states[states['Name of State / UT'].isin([selected_state])]['Cured/Discharged/Migrated* Change since yesterday'].values[0]))
    st.subheader("New Deaths")
    st.subheader(str(states[states['Name of State / UT'].isin([selected_state])]['Deaths** Change since yesterday'].values[0]))



selected_criteria = st.selectbox(
'Select a Criteria',
['Total Active Cases vs State','Total Recovered vs State','Total Covid Deaths vs State'])
def criteria():
    criteria=selected_criteria
    if criteria=='Total Covid Deaths vs State':
        X='Deaths** Cumulative'
        title_x_axis='Total Covid Deaths'
        COLOR='Deaths** Cumulative by %'

    elif criteria=='Total Recovered vs State':
        X='Cured/Discharged/Migrated* Cumulative'
        title_x_axis='Total Recovered Cases'
        COLOR='Cured/Discharged/Migrated* Cumulative by %'

    elif criteria == 'Total Active Cases vs State':
        X='Active Cases* Total'
        title_x_axis='Total Active Cases'
        COLOR='Active Cases* Total by %'
    return X,title_x_axis,COLOR

X,T,C=criteria()

fig5 = px.bar(states,title='States vs Covid Cases', x=X, y='Name of State / UT', orientation='h',color=C)
fig5.update_layout(xaxis_title=T,yaxis_title="States/UT",autosize=False,
            width=1000,
            height=700)


st.container()
st.plotly_chart(fig5,use_container_width=True)


select_criteria = st.selectbox(
'Select a Criteria',
['Daily Active Cases vs State','Daily Recovered vs State','Daily Covid Deaths vs State'])
def criterias():
    criteria=select_criteria
    if criteria=='Daily Covid Deaths vs State':
        X='Deaths** Change since yesterday'
        title_x_axis='Daily Covid Deaths'
        COLOR='Deaths** Change since yesterday by %'

    elif criteria=='Daily Recovered vs State':
        X='Cured/Discharged/Migrated* Change since yesterday'
        title_x_axis='Daily Recovered Cases'
        COLOR='Cured/Discharged/Migrated* Change since yesterday by %'

    elif criteria == 'Daily Active Cases vs State':
        X='Active Cases* Change Since Yesterday'
        title_x_axis='Daily Active Cases'
        COLOR='Active Cases* Change Since Yesterday by %'
    return X,title_x_axis,COLOR

X1,T1,C1=criterias()

fig6 = px.bar(states,title='States vs Covid Cases', x=X1, y='Name of State / UT', orientation='h',color=C1)
fig6.update_layout(xaxis_title=T1,yaxis_title="States/UT",autosize=False,
            width=1000,
            height=700)


st.container()
st.plotly_chart(fig6,use_container_width=True)
