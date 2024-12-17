from flask import Flask, render_template
import os
import random

app = Flask(__name__)

# Directory where images are stored
image_folder = 'static/images'

# Function to get shuffled images
def get_shuffled_images():
    images = [f for f in os.listdir(image_folder) if os.path.isfile(os.path.join(image_folder, f))]
    random.shuffle(images)
    return images

@app.route('/')
def slideshow():
    images = get_shuffled_images()
    return render_template('slideshow.html', images=images)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
