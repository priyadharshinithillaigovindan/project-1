import pandas as pd
import  mysql.connector
import streamlit as streamlit
from streamlit_option_menu import option_menu
import plotly.express as px
import time

#kerala bus list
list_kerala=[]
df_kerala=pd.read_csv("df_kerala.csv")
for i,r in df_kerala.iterrows():
    list_kerala.append(r["Route_name"])

   #andhra_pradesh bus list
list_andhra_pradesh=[]
df_andhra_pradesh=pd.read_csv("df_andhra_pradesh.csv")
for i,r in df_andhra_pradesh.iterrows():
    list_andhra_pradesh.append(r["Route_name"])

  #assam bus list
list_assam=[]
df_assam=pd.read_csv("df_assam.csv")
for i,r in df_assam.iterrows():
    list_assam.append(r["Route_name"])   

#himachal_pradesh bus list
list_himachal_pradesh =[]
df_himachal_pradesh =pd.read_csv("df_himachal_pradesh.csv")
for i,r in df_himachal_pradesh.iterrows():
    list_himachal_pradesh .append(r["Route_name"]) 


#hyderabad bus list
list_hyderabad =[]
df_hyderabad=pd.read_csv("df_hyderabad.csv")
for i,r in df_hyderabad.iterrows():
    list_hyderabad.append(r["Route_name"])

#GOA BUS LIST
#GOA BUS LIST
list_GOA =[]
df_GOA=pd.read_csv("df_GOA.CSV")
for i,r in df_GOA .iterrows():
    list_GOA.append(r["Route_name"])

#RAJASDHAN BUS LIST
list_RAJASDHAN =[]
df_RAJASDHAN =pd.read_csv("df_RAJASDHAN.CSV")
for i,r in df_RAJASDHAN.iterrows():
    list_RAJASDHAN . append (r["Route_name"])

#SOUTH_BENGAL BUS LIST
list_SOUTH_BENGAL =[]
df_SOUTH_BENGAL =pd.read_csv("df_SOUTH_BENGAL.csv")
for i,r in df_SOUTH_BENGAL.iterrows():
    list_SOUTH_BENGAL . append (r["Route_name"])

# uttar_pradesh BUS LIST
list_uttar_pradesh =[]
df_uttar_pradesh = pd.read_csv("df_uttar_pradesh.csv")
for i,r in df_uttar_pradesh.iterrows():
    list_uttar_pradesh . append (r["Route_name"])

# west_bengal BUS LIST
list_west_bengal =[]
df_west_bengal =pd.read_csv("df_west_bengal.csv")
for i,r in df_west_bengal.iterrows():
    list_west_bengal. append (r["Route_name"])
    
    import streamlit as st
from streamlit_option_menu import option_menu
import os  # Import os to handle file paths

# Set page configuration
st.set_page_config(layout="wide")

# Navigation menu
web = option_menu(
    menu_title="onlinebus",
    options=["Home", "States and Routes"],
    icons=["house", "info-circle"],
    orientation="horizontal"
)

 # Home page settings
if web == "Home":
 # Load image properly
    st.image(r"C:\Users\PRIYA\OneDrive\Desktop\277796888_5590327647663467_6923175881659344174_n.jpg",width=200)
    st.video("https://youtu.be/h3qA8vkFXSs?si=SOc1br_ASh940yHN")
    st.markdown("[REDBUS](https://www.redbus.in/)")
   
    

    st.title("Redbus Data Scraping with Selenium & Dynamic Filtering using Streamlit")
    st.subheader(":blue[Domain:] Transportation")
    st.subheader(":blue[Objective:]")
    st.markdown("The **'Redbus Data Scraping and Filtering with Streamlit Application'** aims to revolutionize the transportation industry by providing a comprehensive solution.")

    st.subheader(":blue[Overview:] ")
    st.markdown("### **Selenium:**")
    st.markdown("Selenium is a tool used for automating web browsers. It is commonly used for web scraping, which involves extracting data from websites.")

    st.markdown("### **Pandas:**")
    st.markdown("Pandas is a powerful library that transforms datasets from CSV format into structured DataFrames. It helps in data manipulation, cleaning, and preprocessing, ensuring that data is ready for analysis.")

    st.markdown("### **MySQL:**")
    st.markdown("With the help of SQL, we establish a connection to a MySQL database, enabling seamless integration of datasets. The data is efficiently inserted into relevant tables for storage and retrieval.")

    st.markdown("### **Streamlit:**")
    st.markdown("We developed an interactive web application using Streamlit, a user-friendly framework for data visualization and analysis.")

    st.subheader(":blue[Skills Gained:]") 
    st.markdown("Selenium, Python, Pandas, MySQL-connector-python, Streamlit.")

    
# Default value for 's'
s = None  

if web == "States and Routes":
    s = st.selectbox("Lists of states",
        ["kerala", "andhra pradesh", "assam", "GOA",
         "himachal_pradesh", "hyderabad", "rajasthan",
         "south_bangal","uttar_pradesh","west_bengal"]
    )
 
# Allow user to select fare range
select_fare = st.radio("Choose bus fare range",
         ("50-1000", "1000-2000", ">=2000"))
     
    

# Kerala bus fare filtering
if s == "kerala":  # <-- Correct indentation
    k = st.selectbox("List of routes", list_kerala)

    conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password="Priya@93",
        database="red_bus_details"
    )
    my_cursor = conn.cursor()
    
    
       
 # Adjusted query
    query = f"SELECT * FROM bus_details WHERE Route_name = '{k}'"


    if select_fare == "50-1000":
          query += "AND price BETWEEN 50 AND 1000"

    elif select_fare == "1000-2000":
         query += "AND price BETWEEN 1000 AND 2000"

    elif select_fare == ">=2000":
        query += "AND price >= 2000"
             
                    
    my_cursor.execute(query)
    out = my_cursor.fetchall()

    # Creating a DataFrame from the query results
    df = pd.DataFrame(out, columns=["ID", "Bus_name", "Bus_type", "Start_time", "End_time",
                                    "Total_duration", "price", "sets_available", "Rating",
                                    "Route_link", "Route_name"])
    st.write(df)
    
    # andhra pradesh bus fare filtering
if s == "andhra pradesh":  # <-- Correct indentation
    a = st.selectbox("List of routes", list_andhra_pradesh)

    conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password="Priya@93",
        database="red_bus_details"
    )
    my_cursor = conn.cursor()
    
    
       
 # Adjusted query
    query = f"SELECT * FROM bus_details WHERE Route_name = '{a}'"


    if select_fare == "50-1000":
          query += "AND price BETWEEN 50 AND 1000"

    elif select_fare == "1000-2000":
         query += "AND price BETWEEN 1000 AND 2000"

    elif select_fare == ">=2000":
        query += "AND price >= 2000"
             
                    
    my_cursor.execute(query)
    out = my_cursor.fetchall()

    # Creating a DataFrame from the query results
    df = pd.DataFrame(out, columns=["ID", "Bus_name", "Bus_type", "Start_time", "End_time",
                                    "Total_duration", "price", "sets_available", "Rating",
                                    "Route_link", "Route_name"])
    st.write(df)
    
    
# Goa bus fare filtering
if s == "GOA":  # <-- Correct indentation
    GOA = st.selectbox("List of routes", list_GOA)

    conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password="Priya@93",
        database="red_bus_details"
    )
    
    my_cursor = conn.cursor()
 # Adjusted query
    query = f"SELECT * FROM bus_details WHERE Route_name = '{GOA}'"
    
    if select_fare == "50-1000":
          query += "AND price BETWEEN 50 AND 1000"

    elif select_fare == "1000-2000":
         query += "AND price BETWEEN 1000 AND 2000"

    elif select_fare == ">=2000":
        query += "AND price >= 2000"
        
    my_cursor.execute(query)
    out = my_cursor.fetchall()

    # Creating a DataFrame from the query results
    df = pd.DataFrame(out, columns=["ID", "Bus_name", "Bus_type", "Start_time", "End_time",
                                    "Total_duration", "price", "sets_available", "Rating",
                                    "Route_link", "Route_name"])
    st.write(df)
    
    # himachal pradesh bus fare filtering
if s == "himachal_pradesh":  # <-- Correct indentation
    h = st.selectbox("List of routes", list_himachal_pradesh)

    conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password="Priya@93",
        database="red_bus_details"
    )
    my_cursor = conn.cursor()
    
    
       
 # Adjusted query
    query = f"SELECT * FROM bus_details WHERE Route_name = '{h}'"


    if select_fare == "50-1000":
          query += "AND price BETWEEN 50 AND 1000"

    elif select_fare == "1000-2000":
         query += "AND price BETWEEN 1000 AND 2000"

    elif select_fare == ">=2000":
        query += "AND price >= 2000"
             
                    
    my_cursor.execute(query)
    out = my_cursor.fetchall()

    # Creating a DataFrame from the query results
    df = pd.DataFrame(out, columns=["ID", "Bus_name", "Bus_type", "Start_time", "End_time",
                                    "Total_duration", "price", "sets_available", "Rating",
                                    "Route_link", "Route_name"])
    st.write(df)
    
# assam bus fare filtering
if s == "assam":  # <-- Correct indentation
    a = st.selectbox("List of routes", list_assam)

    conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password="Priya@93",
        database="red_bus_details"
    )
    my_cursor = conn.cursor()
    
    
       
 # Adjusted query
    query = f"SELECT * FROM bus_details WHERE Route_name = '{a}'"


    if select_fare == "50-1000":
          query += "AND price BETWEEN 50 AND 1000"

    elif select_fare == "1000-2000":
         query += "AND price BETWEEN 1000 AND 2000"

    elif select_fare == ">=2000":
        query += "AND price >= 2000"
             
                    
    my_cursor.execute(query)
    out = my_cursor.fetchall()

    # Creating a DataFrame from the query results
    df = pd.DataFrame(out, columns=["ID", "Bus_name", "Bus_type", "Start_time", "End_time",
                                    "Total_duration", "price", "sets_available", "Rating",
                                    "Route_link", "Route_name"])
    st.write(df)
    
    # hyderabad bus fare filtering
if s == "hyderabad":  # <-- Correct indentation
    h = st.selectbox("List of routes", list_hyderabad)

    conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password="Priya@93",
        database="red_bus_details"
    )
    my_cursor = conn.cursor()
    
    
       
 # Adjusted query
    query = f"SELECT * FROM bus_details WHERE Route_name = '{h}'"


    if select_fare == "50-1000":
          query += "AND price BETWEEN 50 AND 1000"

    elif select_fare == "1000-2000":
         query += "AND price BETWEEN 1000 AND 2000"

    elif select_fare == ">=2000":
        query += "AND price >= 2000"
             
                    
    my_cursor.execute(query)
    out = my_cursor.fetchall()

    # Creating a DataFrame from the query results
    df = pd.DataFrame(out, columns=["ID", "Bus_name", "Bus_type", "Start_time", "End_time",
                                    "Total_duration", "price", "sets_available", "Rating",
                                    "Route_link", "Route_name"])
    st.write(df)
    
    # rajasdhan bus fare filtering
if s == "rajasthan":  # <-- Correct indentation
    r = st.selectbox("List of routes", list_RAJASDHAN)

    conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password="Priya@93",
        database="red_bus_details"
    )
    my_cursor = conn.cursor()
    
    
       
 # Adjusted query
    query = f"SELECT * FROM bus_details WHERE Route_name = '{r}'"


    if select_fare == "50-1000":
          query += "AND price BETWEEN 50 AND 1000"

    elif select_fare == "1000-2000":
         query += "AND price BETWEEN 1000 AND 2000"

    elif select_fare == ">=2000":
        query += "AND price >= 2000"
             
                    
    my_cursor.execute(query)
    out = my_cursor.fetchall()

    # Creating a DataFrame from the query results
    df = pd.DataFrame(out, columns=["ID", "Bus_name", "Bus_type", "Start_time", "End_time",
                                    "Total_duration", "price", "sets_available", "Rating",
                                    "Route_link", "Route_name"])
    st.write(df)
    
    # hyderabad bus fare filtering
if s == "hyderabad":  # <-- Correct indentation
    h = st.selectbox("List of routes", list_hyderabad)

    conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password="Priya@93",
        database="red_bus_details"
    )
    my_cursor = conn.cursor()
    
    
       
 # Adjusted query
    query = f"SELECT * FROM bus_details WHERE Route_name = '{h}'"


    if select_fare == "50-1000":
          query += "AND price BETWEEN 50 AND 1000"

    elif select_fare == "1000-2000":
         query += "AND price BETWEEN 1000 AND 2000"

    elif select_fare == ">=2000":
        query += "AND price >= 2000"
             
                    
    my_cursor.execute(query)
    out = my_cursor.fetchall()

    # Creating a DataFrame from the query results
    df = pd.DataFrame(out, columns=["ID", "Bus_name", "Bus_type", "Start_time", "End_time",
                                    "Total_duration", "price", "sets_available", "Rating",
                                    "Route_link", "Route_name"])
    st.write(df)
    
    # south_bangal bus fare filtering
if s == "south_bangal":  # <-- Correct indentation
    s = st.selectbox("List of routes", list_SOUTH_BENGAL)

    conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password="Priya@93",
        database="red_bus_details"
    )
    my_cursor = conn.cursor()
    
    
       
 # Adjusted query
    query = f"SELECT * FROM bus_details WHERE Route_name = '{s}'"


    if select_fare == "50-1000":
          query += "AND price BETWEEN 50 AND 1000"

    elif select_fare == "1000-2000":
         query += "AND price BETWEEN 1000 AND 2000"

    elif select_fare == ">=2000":
        query += "AND price >= 2000"
             
                    
    my_cursor.execute(query)
    out = my_cursor.fetchall()

    # Creating a DataFrame from the query results
    df = pd.DataFrame(out, columns=["ID", "Bus_name", "Bus_type", "Start_time", "End_time",
                                    "Total_duration", "price", "sets_available", "Rating",
                                    "Route_link", "Route_name"])
    st.write(df)
    
   

# west_bengal fare bus details
if s == "west_bengal":  
    w = st.selectbox("List of routes", list_west_bengal)

    # Database connection
    conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password="Priya@93",
        database="red_bus_details"
    )
    my_cursor = conn.cursor()

    # Query setup
    query = f"SELECT * FROM bus_details WHERE Route_name = '{w}'"

    if select_fare == "50-1000":
        query += " AND price BETWEEN 50 AND 1000"
    elif select_fare == "1000-2000":
        query += " AND price BETWEEN 1000 AND 2000"
    elif select_fare == ">=2000":
        query += " AND price >= 2000"

    my_cursor.execute(query)
    out = my_cursor.fetchall()

    # Creating a DataFrame
    df = pd.DataFrame(out, columns=[
        "ID", "Bus_name", "Bus_type", "Start_time", "End_time",
        "Total_duration", "price", "sets_available", "Rating",
        "Route_link", "Route_name"
    ])
    
    st.write(df)
 
 
 #uttar pradesh fare bus details
 
if s == "uttar_pradesh":  
    u = st.selectbox("List of routes", list_uttar_pradesh)

    # Database connection
    conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password="Priya@93",
        database="red_bus_details"
    )
    my_cursor = conn.cursor()

    # Query setup
    query = f"SELECT * FROM bus_details WHERE Route_name = '{u}'"

    if select_fare == "50-1000":
        query += " AND price BETWEEN 50 AND 1000"
    elif select_fare == "1000-2000":
        query += " AND price BETWEEN 1000 AND 2000"
    elif select_fare == ">=2000":
        query += " AND price >= 2000"

    my_cursor.execute(query)
    out = my_cursor.fetchall()

    # Creating a DataFrame
    df = pd.DataFrame(out, columns=[
        "ID", "Bus_name", "Bus_type", "Start_time", "End_time",
        "Total_duration", "price", "sets_available", "Rating",
        "Route_link", "Route_name"
    ])
    
    st.write(df)
 
 
 
 
 