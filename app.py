import streamlit as st
from sqlalchemy import text
import plotly.express as px

# Fungsi untuk mengambil data dari database
def fetch_data():
    return conn.query('SELECT * FROM PARTICIPANT ORDER By id;', ttl="0")

# Fungsi untuk membuat dashboard visualisasi
def create_visualization(data):
    st.subheader('Visualisasi Data')

    # Visualisasi sederhana menggunakan Plotly Express
    fig = px.scatter(data, x='ages', y='price', color='job', size='price', title='Scatter Plot Ages vs Price')
    st.plotly_chart(fig, use_container_width=True)

    # Diagram batang untuk menunjukkan jumlah peserta berdasarkan jenis program
    fig_bar = px.bar(data, x='programs', title='Jumlah Peserta Berdasarkan Jenis Program')
    st.plotly_chart(fig_bar, use_container_width=True)

    # ... Tambahkan visualisasi lainnya sesuai kebutuhan

# Fungsi utama aplikasi
def main():
    css_link = '<link rel="stylesheet" href="style.css">'
    st.markdown(css_link, unsafe_allow_html=True)

    st.header('DATABASE PARTICIPANT DATA MANAGEMENT KAMPUNG INGGRIS')
    page = st.sidebar.selectbox("Pilih Menu", ["View Data", "Edit Data", "Visualisasi Data"])

    with conn.session as session:
        query = text('CREATE TABLE IF NOT EXISTS PARTICIPANT (id serial, full_name varchar, gender varchar, birth date, \
                                                           ages int, city varchar, job varchar, institution varchar, \
                                                           email varchar, handphone varchar, programs varchar, \
                                                           duration varchar, price int, starting_date date, ending_date date);')
        session.execute(query)

    if page == "View Data":
        data = fetch_data()
        st.dataframe(data)
    elif page == "Edit Data":
        if st.button('Tambah Data'):
            with conn.session as session:
                query = text('INSERT INTO PARTICIPANT (full_name, gender, birth, ages, city, job, institution, email, handphone, \
                                                        programs, duration, price, starting_date, ending_date) \
                              VALUES (:1, :2, :3, :4, :5, :6, :7, :8, :9, :10, :11, :12, :13, :14);')
                session.execute(query, {'1': '', '2': '', '3': None, '4': 0, '5': '', '6': '', '7': '', '8': '', '9': '',
                                        '10': '', '11': '', '12': 0, '13': None, '14': None})
                session.commit()

        data = fetch_data()
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
                    # ... (kode sebelumnya)

    elif page == "Visualisasi Data":
        data = fetch_data()
        create_visualization(data)

# Panggil fungsi utama
if __name__ == '__main__':
    main()
