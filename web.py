from flask import Flask, request, render_template_string
import qrcode
import os

app = Flask(__name__)

# Ensure the 'static' directory exists
if not os.path.exists('static'):
    os.makedirs('static')

@app.route('/', methods=['GET', 'POST'])
def home():
    qr_image = None
    character_count = None
    version = None
    if request.method == 'POST':
        url = request.form['url']
        box_size = int(request.form['box_size'])
        border = int(request.form['border'])
        error_correction = request.form['error_correction']
        character_count = len(url)

        # Map the selected error correction level
        error_correction_map = {
            'L': qrcode.constants.ERROR_CORRECT_L,
            'M': qrcode.constants.ERROR_CORRECT_M,
            'Q': qrcode.constants.ERROR_CORRECT_Q,
            'H': qrcode.constants.ERROR_CORRECT_H
        }

        # Determine the appropriate version based on character count
        if request.form['version'] == 'auto':
            if error_correction == 'L':
                if character_count <= 25:
                    version = 1
                elif character_count <= 47:
                    version = 2
                elif character_count <= 77:
                    version = 3
                elif character_count <= 114:
                    version = 4
                elif character_count <= 154:
                    version = 5
                else:
                    version = 6
            elif error_correction == 'M':
                if character_count <= 20:
                    version = 1
                elif character_count <= 38:
                    version = 2
                elif character_count <= 61:
                    version = 3
                elif character_count <= 90:
                    version = 4
                elif character_count <= 122:
                    version = 5
                else:
                    version = 6
            elif error_correction == 'Q':
                if character_count <= 16:
                    version = 1
                elif character_count <= 29:
                    version = 2
                elif character_count <= 47:
                    version = 3
                elif character_count <= 67:
                    version = 4
                elif character_count <= 87:
                    version = 5
                else:
                    version = 6
            elif error_correction == 'H':
                if character_count <= 10:
                    version = 1
                elif character_count <= 20:
                    version = 2
                elif character_count <= 35:
                    version = 3
                elif character_count <= 50:
                    version = 4
                elif character_count <= 64:
                    version = 5
                else:
                    version = 6
        else:
            version = int(request.form['version'])
        elif error_correction == 'M':
            if character_count <= 20:
                version = 1
            elif character_count <= 38:
                version = 2
            elif character_count <= 61:
                version = 3
            elif character_count <= 90:
                version = 4
            elif character_count <= 122:
                version = 5
            else:
                version = 6
        elif error_correction == 'Q':
            if character_count <= 16:
                version = 1
            elif character_count <= 29:
                version = 2
            elif character_count <= 47:
                version = 3
            elif character_count <= 67:
                version = 4
            elif character_count <= 87:
                version = 5
            else:
                version = 6

        # Create the QR code
        qr = qrcode.QRCode(
            version=version,
            error_correction=error_correction_map[error_correction],
            box_size=box_size,
            border=border,
        )
        qr.add_data(url)
        qr.make(fit=True)

        img = qr.make_image(fill_color="black", back_color="white")
        img_path = "static/qr_code.png"
        img.save(img_path)
        qr_image = img_path

    # HTML template to accept URL, box size, border, error correction level, and display QR code
    html_template = '''
    <!doctype html>
    <html lang="en">
      <head>
        <meta charset="utf-8">
        <title>QR Code Generator</title>
      </head>
      <body>
        <h1>QR Code Generator</h1>
        <p>
          <strong>ERROR_CORRECT_L:</strong> About 7% or less errors can be corrected.<br>
          <strong>ERROR_CORRECT_M (default):</strong> About 15% or less errors can be corrected.<br>
          <strong>ERROR_CORRECT_Q:</strong> About 25% or less errors can be corrected.<br>
          <strong>ERROR_CORRECT_H:</strong> About 30% or less errors can be corrected.
        </p><br>
        <form method="post">
          <label for="url">Enter URL:</label>
          <input type="text" id="url" name="url" required><br><br>
          <label for="box_size">Enter Box Size:</label>
          <input type="number" id="box_size" name="box_size" value="2" required><br><br>
          <label for="border">Enter Border Size:</label>
          <input type="number" id="border" name="border" value="1" required><br><br>
          <label for="version">Select QR Code Version:</label>
          <select id="version" name="version" required>
            <option value="auto">Auto</option>
            <option value="1">Version 1</option>
            <option value="2">Version 2</option>
            <option value="3">Version 3</option>
            <option value="4">Version 4</option>
            <option value="5">Version 5</option>
            <option value="6">Version 6</option>
          </select><br><br>
          <button type="submit">Generate QR Code</button>
        </form>
        {% if qr_image %}
        <h2>Your QR Code:</h2>
        <img src="/{{ qr_image }}" alt="QR Code">
        <p>URL Character Count: {{ character_count }}</p>
        <p>QR Code Version: {{ version }}</p>
        {% endif %}
      </body>
    </html>
    '''

    return render_template_string(html_template, qr_image=qr_image, character_count=character_count, version=version)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)            