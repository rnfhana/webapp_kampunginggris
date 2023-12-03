import streamlit as st
from sqlalchemy import text
import pandas as pd
import plotly.express as px

css_link = '<link rel="stylesheet" href="style.css">'
st.markdown(css_link, unsafe_allow_html=True)

list_programs = ['', 'General English', 'Intensive IELTS', 'TOEFL Preparation', 'Business English', 'Conversational English']
list_gender = ['', 'male', 'female']
list_duration = ['', '2 months', '3 months']
list_job = ['', 'Student', 'Worker', 'College Student']

conn = st.connection("postgresql", type="sql", 
                     url="postgresql://rezkihanafadhila:rFTzUJkYG4j9@ep-royal-wind-80779842.us-east-2.aws.neon.tech/web")

with conn.session as session:
    query = text('CREATE TABLE IF NOT EXISTS PARTICIPANT (id serial, full_name varchar, gender varchar, birth date, \
                                                       ages int, city varchar, job varchar, institution varchar, \
                                                       email varchar, handphone varchar, programs varchar, \
                                                       duration varchar, price int, starting_date date, ending_date date);')
    session.execute(query)

st.header('DATABASE PARTICIPANT DATA MANAGEMENT KAMPUNG INGGRIS')
page = st.sidebar.selectbox("Pilih Menu", ["View Data", "Edit Data", "Visualisasi Data"])

if page == "View Data":
    data = conn.query('SELECT * FROM PARTICIPANT ORDER By id;', ttl="0").set_index('id')
    st.dataframe(data)

if page == "Edit Data":
    if st.button('Tambah Data'):
        with conn.session as session:
            query = text('INSERT INTO PARTICIPANT (full_name, gender, birth, ages, city, job, institution, email, handphone, \
                                                    programs, duration, price, starting_date, ending_date) \
                          VALUES (:1, :2, :3, :4, :5, :6, :7, :8, :9, :10, :11, :12, :13, :14);')
            session.execute(query, {'1': '', '2': '', '3': None, '4': 0, '5': '', '6': '', '7': '', '8': '', '9': '',
                                    '10': '', '11': '', '12': 0, '13': None, '14': None})
            session.commit()

    data = conn.query('SELECT * FROM PARTICIPANT ORDER By id;', ttl="0")
    for _, result in data.iterrows():
        # Your existing code for editing data

if page == "Visualisasi Data":
    st.subheader("Visualisasi Data")
    
    # Fetch the data
    data = conn.query('SELECT * FROM PARTICIPANT ORDER By id;', ttl="0")

    # Visualization using bar chart
    st.subheader("Bar Chart")
    fig_bar = px.bar(data, x='programs', title='Program Distribution')
    st.plotly_chart(fig_bar)

    # Visualization using pie chart
    st.subheader("Pie Chart")
    fig_pie = px.pie(data, names='gender', title='Gender Distribution')
    st.plotly_chart(fig_pie)
