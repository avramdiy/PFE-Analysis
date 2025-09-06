from flask import Flask, render_template_string
import pandas as pd

app = Flask(__name__)

@app.route('/')
def show_dataframe():
	# Load the data from the specified path
	file_path = r'C:\Users\avram\OneDrive\Desktop\Bloomtech TRG\TRG Week 40\pfe.us.txt'
	df = pd.read_csv(file_path, sep=None, engine='python')
	# Render as HTML table
	return render_template_string('''
		<html>
		<head><title>PFE Data</title></head>
		<body>
			<h1>PFE DataFrame</h1>
			{{ table|safe }}
		</body>
		</html>
	''', table=df.to_html(index=False))

if __name__ == '__main__':
	app.run(debug=True)
