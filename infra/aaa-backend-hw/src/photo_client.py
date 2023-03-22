import requests


class PhotoClient:
    def __init__(self, url: str):
        self.url = url

    def get_image_binary(self, image_id) -> str:
        image_binary = requests.get(
            f'{self.url}/images/{image_id}',
            timeout=3,
        )
        return image_binary.content


if __name__ == '__main__':
    photo_client_instance = PhotoClient('http://51.250.83.169:7878')
    print(type(photo_client_instance.get_image_binary(10022)))
