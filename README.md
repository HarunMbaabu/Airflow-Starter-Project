## **Beginner Friend Apache Airflow Project.**

Build a data pipeline using Apache Airflow to perform an Extract, Transform, Load (ETL) process on a dataset, for this challenge we will use the Amazon Top 50 Bestselling Books 2009 - 2019. 

**Problem:**
Design a workflow that extracts the data from a source, applies transformations,(e.g., cleaning, and aggregating), and loads the processed data into a destination Snowflake (Snowflake Trial, which goes for 30-DAY)

Use Airflow's operators and scheduling capabilities to define and orchestrate the tasks in your pipeline.

Dataset Provided: Dataset on Amazon's Top 50 bestselling books from 2009 to 2019. Contains 550 books, data has been categorized into fiction and non-fiction using Goodreads 

[Source](https://www.kaggle.com/datasets/sootersaalu/amazon-top-50-bestselling-books-2009-2019) 


Convert the CSV file into a PostgreSQL Table: 


```sql 
-- SQL script to convert a CSV file into a PostgreSQL table

-- Step 1: Create a table to store the data from the CSV file
CREATE TABLE IF NOT EXISTS books (
  name VARCHAR(255),
  author VARCHAR(255),
  user_rating FLOAT,
  reviews INTEGER,
  price NUMERIC(10,2),
  year INTEGER,
  genre VARCHAR(255)
);


-- Step 2: Copy the data from the CSV file into the table
COPY books(name, author, user_rating, reviews, price, year, genre)
FROM '/path/to/your/data/bestsellers with categories.csv'
DELIMITER ',' CSV HEADER; 

```



psql -U your_username -d your_database -f /path/to/your/src/convert_csv_to_table.sql
