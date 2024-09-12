from flask import Flask, render_template, request, send_from_directory

app = Flask(__name__)

@app.route('/', methods=['GET','POST'])
def index():
    if request.method == 'POST':
        # Seçilen resmi almak
        selected_image = request.form.get('image-selector')

        # Metni almak
        text_top = request.form.get('textTop')
        text_bottom = request.form.get('textBottom')

        # Metnin rengini almak
        selected_color = request.form.get('color-selector')

        # Metnin konumunu almak
        text_top_y = request.form.get('textTop_y')
        text_bottom_y = request.form.get('textBottom_y')

        # Metin büyüklüğünü almak
        text_size = request.form.get('text_size')

        return render_template('index.html', 
                               selected_image=selected_image, 
                               text_bottom=text_bottom,
                               text_top=text_top,
                               selected_color=selected_color,
                               text_top_y=text_top_y,
                               text_bottom_y=text_bottom_y,
                               text_size=text_size)
    else:
        return render_template('index.html', selected_image='logo.svg')


@app.route('/static/img/<path:path>')
def serve_images(path):
    return send_from_directory('static/img', path)

app.run(debug=True)
