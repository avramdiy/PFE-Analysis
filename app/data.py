from flask import Flask, render_template_string
import pandas as pd

app = Flask(__name__)


@app.route('/')
def show_dataframe():
	# Load the data from the specified path
	file_path = r'C:\Users\avram\OneDrive\Desktop\Bloomtech TRG\TRG Week 40\pfe.us.txt'
	df = pd.read_csv(file_path, sep=None, engine='python')
	# Drop the 'OpenInt' column if it exists
	if 'OpenInt' in df.columns:
		df = df.drop(columns=['OpenInt'])
	# Split the DataFrame into 3 objects for further analysis
	# Assuming equal splits by row count
	n = len(df)
	split1 = df.iloc[:n//3]
	split2 = df.iloc[n//3:2*n//3]
	split3 = df.iloc[2*n//3:]
	# Render as HTML table (showing the first split for demonstration)
	return render_template_string('''
		<html>
		<head><title>PFE Data</title></head>
		<body>
			<h1>PFE DataFrame (First Split)</h1>
			{{ table|safe }}
		</body>
		</html>
	''', table=split1.to_html(index=False))

if __name__ == '__main__':
	app.run(debug=True)
