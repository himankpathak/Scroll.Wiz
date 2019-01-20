from flask import Flask, redirect, url_for, request,render_template
import requests 
import ast
import base64
import cv2
from io import StringIO
import numpy as np
	
def readb64(base64_string):
    sbuf = StringIO()
    sbuf.write(base64.b64decode(str(base64_string)))
    pimg = Image.open(sbuf)
    return cv2.cvtColor(np.array(pimg), cv2.COLOR_RGB2BGR)

	
	
app = Flask(__name__)

@app.route('/',methods = ['POST', 'GET'])
def start():
	if request.method == 'POST':
		data_url = request.get_data()
		img = readb64(str(data_url))
		cv2.imwrite('img.jpg',img)
		return 'True';
	return 'False'
	  
	
if __name__ == '__main__':
	app.run(debug = True,host='::',port=80)