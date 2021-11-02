import unittest
from add_folder_yandex import YaUploader, reading_token_y


folder_name = 'test_folder'
my_up_loader = YaUploader(reading_token_y(), folder_name)


class TestYandexFolder(unittest.TestCase):
    def test_add_folder(self):
        """Тест создает папку на Яндекс диске """
        add_folder_new = f'Папка {folder_name} создана!'

        self.assertEqual(my_up_loader.add_folder(), add_folder_new)

    def test_folder_created(self):
        """Тест проверяет на наличие папки на яндекс диске"""
        folder_created = f'Папка с именем {folder_name} уже существует!'

        self.assertIn(folder_created, my_up_loader.add_folder())

    def test_errors(self):
        self.assertEqual(my_up_loader.add_folder(), 'Ошибка!')


if __name__ == '__main__':
    unittest.main()

