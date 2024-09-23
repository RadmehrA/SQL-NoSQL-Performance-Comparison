{\rtf1\ansi\ansicpg1252\cocoartf2761
\cocoatextscaling0\cocoaplatform0{\fonttbl\f0\fswiss\fcharset0 Helvetica;}
{\colortbl;\red255\green255\blue255;}
{\*\expandedcolortbl;;}
\paperw11900\paperh16840\margl1440\margr1440\vieww11520\viewh8400\viewkind0
\pard\tx720\tx1440\tx2160\tx2880\tx3600\tx4320\tx5040\tx5760\tx6480\tx7200\tx7920\tx8640\pardirnatural\partightenfactor0

\f0\fs24 \cf0 # MongoDB Connection\
from pymongo import MongoClient\
import time\
\
# MySQL Connection\
import mysql.connector\
import pandas as pd\
\
# Load Synthetic User Data\
data = pd.read_csv('synthetic_user_data.csv')  # Use the downloaded synthetic dataset\
\
# MongoDB Performance Test\
def mongodb_test():\
    client = MongoClient('localhost', 27017)\
    db = client.testdb\
    collection = db.users\
    start_time = time.time()\
    \
    # Insert data\
    collection.insert_many(data.to_dict('records'))\
    \
    # Query Performance\
    collection.find_one(\{'name': 'User50000'\})\
    \
    duration = time.time() - start_time\
    print(f"MongoDB operation took: \{duration:.4f\} seconds")\
\
# MySQL Performance Test\
def mysql_test():\
    cnx = mysql.connector.connect(user='root', password='password', host='localhost', database='testdb')\
    cursor = cnx.cursor()\
    \
    # Insert data\
    start_time = time.time()\
    add_user = ("INSERT INTO users (id, name, age) VALUES (%s, %s, %s)")\
    for _, user in data.iterrows():\
        cursor.execute(add_user, (user['id'], user['name'], user['age']))\
    \
    # Query Performance\
    cursor.execute("SELECT * FROM users WHERE name = 'User50000'")\
    \
    duration = time.time() - start_time\
    print(f"MySQL operation took: \{duration:.4f\} seconds")\
\
mongodb_test()\
mysql_test()\
}