import streamlit as st
import pandas as pd
from sqlalchemy import text

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

st.header('DATABASE PARTICIPANT KAMPUNG INGGRIS')
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
        id = result['id']
        full_name_lama = result["full_name"]
        gender_lama = result["gender"]
        birth_lama = result["birth"]
        ages_lama = result["ages"]
        city_lama = result["city"]
        job_lama = result["job"]
        institution_lama = result["institution"]
        email_lama = result["email"]
        handphone_lama = result["handphone"]
        programs_lama = result["programs"]
        duration_lama = result["duration"]
        price_lama = result["price"]
        starting_date_lama = result["starting_date"]
        ending_date_lama = result["ending_date"]

        with st.expander(f'a.n. {full_name_lama}'):
            with st.form(f'data-{id}'):
                full_name_baru = st.text_input("full_name", full_name_lama)
                gender_baru = st.selectbox("gender", list_gender, list_gender.index(gender_lama) if gender_lama in list_gender else 0)
                birth_baru = st.date_input("birth", birth_lama)
                ages_baru = st.number_input("ages", value=ages_lama)
                city_baru = st.text_input("city", city_lama)
                job_baru = st.selectbox("job", list_job, list_job.index(job_lama) if job_lama in list_job else 0)
                institution_baru = st.text_input("institution", institution_lama)
                email_baru = st.text_input("email", email_lama)
                handphone_baru = st.text_input("handphone", handphone_lama)
                programs_baru = st.selectbox("programs", list_programs, list_programs.index(programs_lama) if programs_lama in list_programs else 0)
                duration_baru = st.selectbox("duration", list_duration, list_duration.index(duration_lama) if duration_lama in list_duration else 0)
                price_baru = st.number_input("price", value=price_lama)
                starting_date_baru = st.date_input("starting_date", starting_date_lama)
                ending_date_baru = st.date_input("ending_date", ending_date_lama)

                col1, col2 = st.columns([1, 6])

                with col1:
                    if st.form_submit_button('UPDATE'):
                        with conn.session as session:
                            query = text('UPDATE PARTICIPANT \
                                          SET full_name=:1, gender=:2, birth=:3, ages=:4, city=:5, job=:6, institution=:7, \
                                          email=:8, handphone=:9, programs=:10, duration=:11, price=:12, \
                                          starting_date=:13, ending_date=:14 \
                                          WHERE id=:15;')
                            session.execute(query, {'1': full_name_baru, '2': gender_baru, '3': birth_baru,
                                                    '4': ages_baru, '5': city_baru, '6': job_baru, '7': institution_baru,
                                                    '8': email_baru, '9': handphone_baru, '10': programs_baru,
                                                    '11': duration_baru, '12': price_baru, '13': starting_date_baru,
                                                    '14': ending_date_baru, '15': id})
                            session.commit()
                            st.experimental_rerun()

                with col2:
                    if st.form_submit_button('DELETE'):
                        query = text(f'DELETE FROM PARTICIPANT WHERE id=:1;')
                        session.execute(query, {'1': id})
                        session.commit()
                        st.experimental_rerun()


if page == "Visualisasi Data":
    st.subheader("Visualisasi Programs")
    data = conn.query('SELECT programs, COUNT(*) as count FROM participant GROUP BY programs;')
    st.bar_chart(data.set_index('programs'))
    '\n'
    st.subheader("Visualisasi Duration")
    data = conn.query('SELECT duration, COUNT(*) as count FROM participant GROUP BY duration;')
    st.bar_chart(data.set_index('duration'))
    '\n'
    st.subheader("Visualisasi Price")
    data = conn.query('SELECT price, COUNT(*) as count FROM participant GROUP BY price;')
    st.bar_chart(data.set_index('price'))