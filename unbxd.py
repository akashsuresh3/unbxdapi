from flask import Flask,render_template,jsonify,request,abort
import sqlite3
from sqlite3 import Error
from flask_sqlalchemy import SQLAlchemy
import datetime
import os
import sys
import hashlib
import requests
import json
import csv

app=Flask(__name__)

basedir=os.path.abspath(os.path.dirname(__file__))


@app.route('https://search.unbxd.io/fb853e3332f2645fac9d71dc63e09ec1/demo-unbxd700181503576558/search?&q=*&rows=<count_of_products>&start=<result_number>',methods=["POST"])
def modify_product(count_of_products,result_number):
	if(request.method!="POST"):
        return jsonify({}),405


    response = request.get_json()["response"]

    products = response["products"]

    n = len(products)

    for i in range(n):
    	for obj in products[i]:
    		for attribute,value in obj.items():
    			if isinstance(value, list):
    				combinedstring = ""

    				if attribute ==  "unbxd_color_for_category":
    					new_value = []
	    				for l in value: 
	    					if l not in new_value: 
	        					new_value.append(l)

	        			for j in new_value:
	        				to_find = "::"
	        				start = j.find(to_find)
	        				end = j.find(to_find,start+2)

	        				add_string = j[start+2:end]

	        				combinedstring = combinedstring + add_string

    				
    				else:
	    				new_value = []
	    				for l in value: 
	    					if l not in new_value: 
	        					new_value.append(l)
	    				for j in new_value:
	    					combinedstring = combinedstring + j

	    				if combinedstring == "false":
	    					combinedstring = "NO"

	    				elif combinedstring == "true":
	    					combinedstring = "YES"

    				obj[attribute] = combinedstring


if __name__=='__main__':
    app.debug=True
    app.run()




