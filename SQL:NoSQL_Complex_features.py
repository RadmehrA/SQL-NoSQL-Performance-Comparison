{\rtf1\ansi\ansicpg1252\cocoartf2761
\cocoatextscaling0\cocoaplatform0{\fonttbl\f0\fswiss\fcharset0 Helvetica;}
{\colortbl;\red255\green255\blue255;}
{\*\expandedcolortbl;;}
\paperw11900\paperh16840\margl1440\margr1440\vieww11520\viewh8400\viewkind0
\pard\tx720\tx1440\tx2160\tx2880\tx3600\tx4320\tx5040\tx5760\tx6480\tx7200\tx7920\tx8640\pardirnatural\partightenfactor0

\f0\fs24 \cf0 # Enhanced MongoDB and MySQL Performance Comparison\
\
from pymongo import MongoClient\
import mysql.connector\
import time\
import matplotlib.pyplot as plt\
\
# Generate Sample Dataset\
sample_data = [\{'id': i, 'name': f'User\{i\}', 'age': i % 100\} for i in range(1000000)]\
\
def mongodb_test():\
    client = MongoClient('localhost', 27017)\
    db = client.testdb\
    collection = db.users\
    start_time = time.time()\
    \
    # Insert data\
    collection.insert_many(sample_data)\
    insertion_duration = time.time() - start_time\
    \
    # Query Performance\
    query_start = time.time()\
    collection.find_one(\{'name': 'User50000'\})\
    query_duration = time.time() - query_start\
    \
    return insertion_duration, query_duration\
\
def mysql_test():\
    cnx = mysql.connector.connect(user='root', password='password', host='localhost', database='testdb')\
    cursor = cnx.cursor()\
    \
    # Insert data\
    start_time = time.time()\
    add_user = ("INSERT INTO users (id, name, age) VALUES (%s, %s, %s)")\
    for user in sample_data:\
        cursor.execute(add_user, (user['id'], user['name'], user['age']))\
    cnx.commit()\
    insertion_duration = time.time() - start_time\
    \
    # Query Performance\
    query_start = time.time()\
    cursor.execute("SELECT * FROM users WHERE name = 'User50000'")\
    query_duration = time.time() - query_start\
    \
    cursor.close()\
    cnx.close()\
    \
    return insertion_duration, query_duration\
\
# Run tests and collect results\
mongo_insert, mongo_query = mongodb_test()\
mysql_insert, mysql_query = mysql_test()\
\
# Visualize Results\
labels = ['MongoDB Insertion', 'MongoDB Query', 'MySQL Insertion', 'MySQL Query']\
times = [mongo_insert, mongo_query, mysql_insert, mysql_query]\
\
plt.bar(labels, times)\
plt.ylabel('Time (seconds)')\
plt.title('Database Performance Comparison')\
plt.show()\
}