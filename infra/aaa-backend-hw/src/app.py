from flask import Flask, request

import logging
import io

from models.plate_reader import PlateReader
from photo_client import PhotoClient

from PIL import UnidentifiedImageError
from requests import exceptions


app = Flask(__name__)

plate_reader = PlateReader.load_from_file('./model_weights/plate_reader_model.pth')
photo_client = PhotoClient('http://51.250.83.169:7878')


# curl 127.0.0.1:8080/readNumbers/10022,9965
@app.route('/readNumbers/<string:image_ids>')
def read_numbers(image_ids):
    dict_images, dict_results = {}, {}

    for id in image_ids.split(','):
        try:
            image_binary = photo_client.get_image_binary(id)
            dict_images[id] = io.BytesIO(image_binary)
        except exceptions.ReadTimeout:
            dict_results[f'result_{id}'] = 'Timeout error'

    for id, im in dict_images.items():
        try:
            dict_results[f'result_{id}'] = plate_reader.read_text(im)
        except UnidentifiedImageError:
            dict_results[f'result_{id}'] = 'Invalid image or its id'

    return dict_results


@app.route('/health')
def health():
    return {'result': True}


if __name__ == '__main__':
    logging.basicConfig(
        format='[%(levelname)s] [%(asctime)s] %(message)s',
        level=logging.INFO,
    )

    app.config['JSON_AS_ASCII'] = False # для русского языка
    app.run(host='0.0.0.0', port=8080, debug=True)
