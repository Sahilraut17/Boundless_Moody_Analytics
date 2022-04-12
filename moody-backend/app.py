from flask import Flask, render_template, jsonify
from flask_cors import CORS, cross_origin
from sqlalchemy import create_engine
import pandas as pd
import pymysql

app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'
con = pymysql.connect(user='sahil',password='Sahil172',host='moody.cfgnksw3aykg.us-east-1.rds.amazonaws.com',db='moody',port=3306)

@app.route('/fetch/<query>', methods=['GET'])
@cross_origin()
def fetch_data(query):
    df = pd.read_sql_query(query, con)
    return df.to_json(orient='records')

if __name__ == '__main__':
    app.run()
