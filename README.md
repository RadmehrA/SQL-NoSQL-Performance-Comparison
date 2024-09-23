# SQL vs NoSQL Performance Comparison

## Description
This project compares the performance of a NoSQL database (MongoDB) and an SQL database (MySQL) in terms of query speed, scalability, and data storage efficiency. The goal is to demonstrate how NoSQL databases handle unstructured data compared to relational databases.

## Problem
With the rise of big data and unstructured datasets, NoSQL databases are increasingly being adopted for their flexibility and scalability. However, relational databases still dominate for structured data with well-defined relationships. This project aims to assess how these two types of databases perform for the same dataset in terms of insertion speed and query execution.

## Methodology
1. Insert a dataset of 1 million records into both a MySQL database and a MongoDB collection.
2. Execute basic queries on each database and measure execution time.

## Requirements
- Python 3.x
- MongoDB
- MySQL
- `pymongo` library for MongoDB
- `mysql-connector` for MySQL

## Code Example
```python
# MongoDB Performance Test
from pymongo import MongoClient

# MySQL Performance Test
import mysql.connector
