# app.py
from flask import Flask, send_file
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
import io

app = Flask(__name__)

@app.route('/')
# def hexbin_plot():
#     # Load the Iris dataset
#     iris = sns.load_dataset('iris')

#     # Create a hexbin plot
#     plt.figure(figsize=(8, 6))
#     plt.hexbin(iris['sepal_length'], iris['sepal_width'], gridsize=30, cmap='Blues')
#     plt.colorbar(label='count')
#     plt.xlabel('Sepal Length')
#     plt.ylabel('Sepal Width')
#     plt.title('Hexbin Plot of Sepal Dimensions')

#     # Save the plot to a BytesIO object
#     img = io.BytesIO()
#     plt.savefig(img, format='png')
#     img.seek(0)
#     plt.close()

#     # Send the image as a response
#     return send_file(img, mimetype='image/png')

# if __name__ == '__main__':
#     app.run(debug=True)
# app.py


@app.route('/')
def plots():
    # Load the Iris dataset
    iris = sns.load_dataset('iris')

    # Create a figure with two subplots side by side
    fig, axes = plt.subplots(1, 2, figsize=(16, 6))

    # Create a hexbin plot on the first subplot
    axes[0].hexbin(iris['sepal_length'], iris['sepal_width'], gridsize=30, cmap='Blues')
    axes[0].set_title('Hexbin Plot of Sepal Dimensions')
    axes[0].set_xlabel('Sepal Length')
    axes[0].set_ylabel('Sepal Width')
    fig.colorbar(axes[0].collections[0], ax=axes[0], label='count')

    # Create a scatter plot on the second subplot
    axes[1].scatter(iris['sepal_length'], iris['sepal_width'], alpha=0.7)
    axes[1].set_title('Scatter Plot of Sepal Dimensions')
    axes[1].set_xlabel('Sepal Length')
    axes[1].set_ylabel('Sepal Width')

    # Adjust layout
    plt.tight_layout()

    # Save the plots to a BytesIO object
    img = io.BytesIO()
    plt.savefig(img, format='png')
    img.seek(0)
    plt.close()

    # Send the image as a response
    return send_file(img, mimetype='image/png')

if __name__ == '__main__':
    app.run(debug=True)
