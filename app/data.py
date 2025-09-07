from flask import Flask, render_template_string
import pandas as pd
import matplotlib.pyplot as plt
import io
import base64

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

@app.route('/plot-volume')
def plot_volume():
	file_path = r'C:\Users\avram\OneDrive\Desktop\Bloomtech TRG\TRG Week 40\pfe.us.txt'
	df = pd.read_csv(file_path, sep=None, engine='python')
	if 'OpenInt' in df.columns:
		df = df.drop(columns=['OpenInt'])
	n = len(df)
	split1 = df.iloc[:n//3]
	# Plot the Volume column
	plt.figure(figsize=(10, 4))
	plt.plot(split1['Volume'])
	plt.title('Volume over Time (split1)')
	plt.xlabel('Index')
	plt.ylabel('Volume')
	plt.tight_layout()
	# Save plot to a bytes buffer
	buf = io.BytesIO()
	plt.savefig(buf, format='png')
	plt.close()
	buf.seek(0)
	img_base64 = base64.b64encode(buf.read()).decode('utf-8')
	# Render as HTML with embedded image
	return render_template_string('''
		<html>
		<head><title>Volume Plot</title></head>
		<body>
			<h1>Volume over Time (split1)</h1>
			<img src="data:image/png;base64,{{ img }}"/>
		</body>
		</html>
	''', img=img_base64)

@app.route('/plot-volume-split2')
def plot_volume_split2():
	file_path = r'C:\Users\avram\OneDrive\Desktop\Bloomtech TRG\TRG Week 40\pfe.us.txt'
	df = pd.read_csv(file_path, sep=None, engine='python')
	if 'OpenInt' in df.columns:
		df = df.drop(columns=['OpenInt'])
	n = len(df)
	split2 = df.iloc[n//3:2*n//3]
	# Plot the Volume column for split2
	plt.figure(figsize=(10, 4))
	plt.plot(split2['Volume'])
	plt.title('Volume over Time (split2)')
	plt.xlabel('Index')
	plt.ylabel('Volume')
	plt.tight_layout()
	buf = io.BytesIO()
	plt.savefig(buf, format='png')
	plt.close()
	buf.seek(0)
	img_base64 = base64.b64encode(buf.read()).decode('utf-8')
	return render_template_string('''
		<html>
		<head><title>Volume Plot Split2</title></head>
		<body>
			<h1>Volume over Time (split2)</h1>
			<img src="data:image/png;base64,{{ img }}"/>
		</body>
		</html>
	''', img=img_base64)

if __name__ == '__main__':
	app.run(debug=True)
