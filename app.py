from flask import Flask, render_template, request, redirect, url_for, session
from flask_mysqldb import MySQL
import MySQLdb.cursors
import re
import openai

app = Flask(__name__)

openai.api_key = "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" #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

app.secret_key = 'your secret key'

app.config['MYSQL_HOST'] = '146.190.218.21'
app.config['MYSQL_USER'] = 'agustin'
app.config['MYSQL_PASSWORD'] = 'dalkoeslaonda'
app.config['MYSQL_DB'] = 'foodwise_sql'

mysql = MySQL(app)

@app.route('/')
def inicio():
	return redirect(url_for('content'))

@app.route('/content', methods =['GET', 'POST'])
def content():
	msg = 'Hola! Soy elotin el elote. Soy muy sabroso!'
	searched = ''
	image_url = 'https://static.vecteezy.com/system/resources/previews/024/488/216/non_2x/happy-smiling-yellow-corn-face-cartoon-character-funny-cute-vegetable-sticker-color-personage-icon-isolated-on-transparent-background-healthy-organic-vegan-diet-food-generative-ai-free-png.png'
	if request.method == 'POST' and 'search' in request.form:
		search = request.form['search']
		cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
		cursor.execute('SELECT * FROM alimentos WHERE Alimento = %s', (search, ))
		searched = cursor.fetchall()
		if searched:
			msg = "Resultados obtenidos"
			prompt = str(search)
			response = openai.images.generate(prompt=prompt, n=1, size="256x256",)
			image_url = response.data[0].url
		else:
			msg = "Hijoles!. Por el momento no tenemos registro de ese alimento. Por favor, intenta con otro"
			image_url = "https://th.bing.com/th/id/OIG.qxwjaY3G5Etp_Dlski5w?pid=ImgGn&w=1024&h=1024&rs=1"
		return render_template('index.html', msg = msg, resultados = searched, url=image_url)
	return render_template('index.html', msg=msg, url=image_url)

#if __name__ == '__main__':
#    app.run(debug=True)
