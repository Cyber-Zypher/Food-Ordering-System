
# Food Ordering System with Python and MySQL
A Simple Food Ordering system made with Python and MySQL Database.
The Code uses PyMySQL Python Library to function. This code has a very simple syntax which makes it easy to understand and beginner friendly.


## Install the required Libraries.

Clone the project

```
pip install pymysql
```
or
```
python -m pip install pymysql
```
## Initialize the Database
```
-- Create the database
CREATE DATABASE food_ordering;

-- Use the database
USE food_ordering;

-- Create the tables
CREATE TABLE menu (
    id INT PRIMARY KEY,
    item_name VARCHAR(100),
    price DECIMAL(10, 2)
);

CREATE TABLE orders (
    id INT PRIMARY KEY AUTO_INCREMENT,
    item_id INT,
    quantity INT,
    total_price DECIMAL(10, 2),
    FOREIGN KEY (item_id) REFERENCES menu(id)
);
```

## Instructions

- After installing the needed libraries. Edit the `menu.csv` file to load the questions and its answers.

- Then, run the `load_food.py` script to load the questions and answers to the SQL database.

- Don't run the `load_food.py` more than once, It will cause duplicate questions and cause clutter on your database.

- Then Finally, run the `app.py` to play the quiz.

## Authors

- [@sidharth_everett](https://github.com/Cyber-Zypher)
- [@sindhu_vaibhav_KL](https://www.instagram.com/sindhuvaibhav2007/)
- [And our friends @Medusa Infosystems International](https://www.instagram.com/themedusaclan_official/)
