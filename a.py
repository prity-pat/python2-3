import streamlit as st
import mysql.connector

st.write('hello')
conn = mysql.connector.connect(host = 'localhost' , user = 'root' , password = 'abcd')
cur = conn.cursor()
cur.execute('show databases')


st.write(cur.fetchall())