import requests


class YaUploader:
    def __init__(self, token: str, folder):
        self.API_BASE_URL = 'https://cloud-api.yandex.net/'
        self.token = token
        self.headers = {'Authorization': token}
        self.folder = folder

    def add_folder(self):
        # Создание папки на Яндекс диске:
        req = requests.put(self.API_BASE_URL + 'v1/disk/resources/', headers=self.headers, params={
            'path': self.folder
        })
        if req.status_code == 201:
            return f'Папка {self.folder} создана!'

        elif req.status_code == 409:
            return f'Папка с именем {self.folder} уже существует!'

        else:
             return 'Ошибка!'


def reading_token_y():
    # Чтение токен из файла Yandex
    with open('token_yandex.txt', 'r') as file_yandex:
        token_y = file_yandex.read().strip()
        return token_y


if __name__ == '__main__':
    up_loader = YaUploader(reading_token_y(), 'folder_test')
    up_loader.add_folder()
