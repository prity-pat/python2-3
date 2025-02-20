import mysql.connector

import streamlit as st

conn= mysql.connector.connect(
    host= "localhost", user= "root",password= 'abcd', database = "jupyter"
)
#print(mydb)
#st.write(mydb)

cur= conn.cursor()
#cur.execute("create table emp(id int not null auto_increment primary key,name text , age int)")
#cur.execute("show tables")
#st.write("created successfully")

#for i in cur:

    # print(i)
    #st.write(i)

#a = st.text_input("enter name")
#b = st.text_input("enter age")
#print(a)
#st.write(a)

with st.form("insert data"):
    name = st.text_input("name")
    age = st.text_input("age")
    submit_button = st.form_submit_button("insert data")

    display_button = st.form_submit_button("display data")
    update_data = st.form_submit_button("update data")


if submit_button:
    query = "INSERT INTO students (name ,age) values (%s,%s)"
    cur.execute(query,(name ,age))
    conn.commit()
    st.success('data written successfully')
    st.balloons()

if display_button:
    cur.execute("select * from students")
    for i in cur:
        st.write(i)  




user_id = st.text_input("enter id")
new_name = st.text_input("enter name") 
new_age= st.text_input("enter age")
if st.button('update'):    
    query = "update emp set name = %s,age =%s where id = %s"
    cur.execute(query,(new_name , new_age , user_id))
    conn.commit()
    st.success("data updated successfully") 
    st.balloons()   

delete_user_id = st.text_input('enter user id')
if st.button('delete'):
    query = "delete from students where s_id = %s"
    cur.execute(query,(delete_user_id,))
    conn.commit() 
    st.success('data deleted successfully')
    st.balloons()       