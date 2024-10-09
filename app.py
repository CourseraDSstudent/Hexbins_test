# app.py
from flask import Flask, send_file
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
import io

app = Flask(__name__)

@app.route('/')
def hexbin_plot():
    # Load the Iris dataset
    iris = sns.load_dataset('iris')

    # Create a hexbin plot
    plt.figure(figsize=(8, 6))
    plt.hexbin(iris['sepal_length'], iris['sepal_width'], gridsize=30, cmap='Blues')
    plt.colorbar(label='count')
    plt.xlabel('Sepal Length')
    plt.ylabel('Sepal Width')
    plt.title('Hexbin Plot of Sepal Dimensions')

    # Save the plot to a BytesIO object
    img = io.BytesIO()
    plt.savefig(img, format='png')
    img.seek(0)
    plt.close()

    # Send the image as a response
    return send_file(img, mimetype='image/png')

if __name__ == '__main__':
    app.run(debug=True)
