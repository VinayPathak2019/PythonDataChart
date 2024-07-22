import pandas as pd
from sqlalchemy import create_engine
import matplotlib.pyplot as plt
from flask import Flask, render_template

app = Flask(__name__)

# Replace the below connection string with your database details
engine = create_engine('mssql+pyodbc://sa:1234@desktop-001/ServiceInvoices?driver=ODBC+Driver+17+for+SQL+Server')

def create_plot():
    # Load data into a pandas DataFrame
    query = "SELECT * FROM your_table"
    df = pd.read_sql(query, engine)
    
    # Create the plot
    plt.figure(figsize=(10, 6))
    plt.plot(df['x_column'], df['y_column'])
    plt.title('Your Plot Title')
    plt.xlabel('X-axis Label')
    plt.ylabel('Y-axis Label')
    plt.grid(True)
    plt.savefig('static/plot.png')

@app.route('/')
def index():
    create_plot()
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
