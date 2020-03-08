# UAH_Assignment_RecordManagement
This project was developed in a couple of days for a test assignment and needs many improvement to make it perfect. Jupyter Notebook and Pandas were used to extract the data from http://testing-ground.scraping.pro/table. Pandas Data Frame was used to insert the data into MySQL database. Flask was used for writing Rest APIs. Bootstrap, HTML, JavaScript, Jquery was used in front-end. HighChart.Js was used for data visualization.

**Note**: This project is not intended for production deployment. 

# To run this project:
1. Create a database in MySQL named "**application**" with a table named "**records**".Import **database_structure.sql** to generate the database schema OR import **database_structure_with_data.sql** to generate database along with scraped data.
2. If database is created with **database_structure.sql** (a database with no data), run the **testing-ground.scraping.py** OR **testing-ground.scraping.ipynb** in Jupyter Notebook to extract the data and insert it into MySQL database. 
3. Download the code and open it in your sublime. Use **Python3** 
4. Install all the necessary imports using the **pip** tool. (Install Flask, flask_sqlalchemy, pymysql, pandas)
5. Run **App.py** (CTRL + B)

## Screens:
1. Home Page
![Alt text](https://github.com/bijaykush/UAH_Assignment_RecordManagement/blob/master/Home%20Page.JPG?raw=true "Data Visualization Page")

2. Data Visualization Page
![Alt text](https://github.com/bijaykush/UAH_Assignment_RecordManagement/blob/master/Data%20Visualization%20Page.JPG?raw=true "Data Visualization Page")

## CRUD Operation
Create, Update, Get and Delete APIs were implemented to work with the data in the database. Adding OR Updating data may cause discrepancies in some cases since I scurried to finish the job.
