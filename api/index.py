from flask import Flask, request, send_file
import qrcode
from io import BytesIO

app = Flask(__name__)

@app.route('/')
def main():
    return 'https://github.com/D1zest/qr-api/tree/main'

@app.route('/g')
def g():
    data = request.args.get('data')
    size = request.args.get('size', '200*200')

    if not data:
        return 'https://github.com/D1zest/qr-api/tree/main', 400

    try:
        width, height = map(int, size.split('*'))
    except ValueError:
        return 'https://github.com/D1zest/qr-api/tree/main', 400

    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(data)
    qr.make(fit=True)
    img = qr.make_image(fill='black', back_color='white')
    img = img.resize((width, height))

    buffer = BytesIO()
    img.save(buffer, 'PNG')
    buffer.seek(0)

    return send_file(buffer, mimetype='image/png')

if __name__ == '__main__':
    app.run(debug=True)
