from flask import Flask, render_template, url_for, request, redirect, flash
from flask_sqlalchemy import SQLAlchemy
import pymysql
import pandas as pd


app = Flask(__name__)
app.secret_key = "Secret Key"

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:root@localhost/application'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)


class Record(db.Model):
	id = db.Column(db.Integer, primary_key = True)
	year = db.Column(db.String(100))
	quarter = db.Column(db.String(100))
	product_1_items = db.Column(db.Integer)
	product_1_amount = db.Column(db.Float)
	product_2_items = db.Column(db.Integer)
	product_2_amount = db.Column(db.Float)
	product_3_items = db.Column(db.Integer)
	product_3_amount = db.Column(db.Float)
	

	def __init__(self, year, quarter, product_1_items, product_1_amount,product_2_items, product_2_amount,product_3_items, product_3_amount):
		self.year = year
		self.quarter = quarter
		self.product_1_items = product_1_items
		self.product_1_amount = product_1_amount
		self.product_2_items = product_2_items
		self.product_2_amount = product_2_amount
		self.product_3_items = product_3_items
		self.product_3_amount = product_3_amount


class yearwise_record(db.Model):
	id = db.Column(db.Integer, primary_key = True)
	year = db.Column(db.Integer)
	total_amount = db.Column(db.Float)

	def __init__(self, year, total_amount):
		self.year = year
		self.total_amount = total_amount


@app.route('/')
def Index():
	all_data = Record.query.all()
	quarters = ['Q1', 'Q2','Q3', 'Q4']
	years = ['2000', '2001', '2002']
	return render_template('index.html', records = all_data, quarters = quarters, years = years)


@app.route('/add', methods = ['POST'])
def add():
	if request.method == 'POST':
		year = request.form['year']
		quarter = request.form['quarter']
		product_1_items = request.form['product_1_items']
		product_1_amount = request.form['product_1_amount']
		product_2_items = request.form['product_2_items']
		product_2_amount = request.form['product_2_amount']
		product_3_items = request.form['product_3_items']
		product_3_amount = request.form['product_3_amount']

		product_data = Record(year, quarter, product_1_items, product_1_amount, product_2_items, product_2_amount, product_3_items, product_3_amount)
		db.session.add(product_data)
		db.session.commit()

		flash("Record Added Successfully!")
		return redirect(url_for('Index'))


@app.route('/update', methods = ['GET', 'POST'])
def update():
	if request.method == 'POST':
		record_data = Record.query.get(request.form.get('id'))
		record_data.year = request.form['year']
		record_data.quarter = request.form['quarter']
		record_data.product_1_items = request.form['product_1_items']
		record_data.product_1_amount = request.form['product_1_amount']
		record_data.product_2_items = request.form['product_2_items']
		record_data.product_2_amount = request.form['product_2_amount']
		record_data.product_3_items = request.form['product_3_items']
		record_data.product_3_amount = request.form['product_3_amount']

		db.session.commit()
		flash("Record Updated Successfully!")

		return redirect(url_for('Index'))

@app.route('/delete/<id>/', methods = ['GET', 'POST'])
def delete(id):
	record_data = Record.query.get(id)
	db.session.delete(record_data)
	db.session.commit()
	flash("Record Deleted Successfully!")

	return redirect(url_for('Index'))



@app.route('/visualization')
def visualization():
	all_data = Record.query.all()
	categories, series_data = graph_data(all_data)
	return render_template('visualization.html', categories=categories, series_data=series_data)


def graph_data(all_data):
	connection = pymysql.connect(host='localhost',
                         user='root',
                         password='root',
                         db='application')

	cursor=connection.cursor()

	df = pd.read_sql('SELECT * FROM record', con=connection)
	categories = list(sorted(set(df['year'])))

	

	series_data = []
	grouped_by_quarter = df.groupby('quarter')

	for quarter,quarter_data in grouped_by_quarter:
		item={}
		item['name']=quarter
		item['data']=list(quarter_data['product_1_amount'])
		item['stack']='product1'
		series_data.append(item)

		item={}
		item['name']=quarter
		item['data']=list(quarter_data['product_2_amount'])
		item['stack']='product2'
		series_data.append(item)

		item={}
		item['name']=quarter
		item['data']=list(quarter_data['product_3_amount'])
		item['stack']='product3'
		series_data.append(item)

	return categories, series_data


if __name__ == "__main__":
	app.run(debug = True)