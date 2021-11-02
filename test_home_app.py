import unittest

from scr.tests_app import show_document_info, add_new_doc, delete_doc


class TestFunctions(unittest.TestCase):
    def test_show_document_info(self):
        documents = [
            {"type": "passport", "number": "2207 876234", "name": "Василий Гупкин"}
        ]

        result = 'passport "2207 876234" "Василий Гупкин"'

        for current_document in documents:
            self.assertEqual(show_document_info(current_document), result)

    def test_add_new_doc(self):
        new_doc_number = '123-456'
        new_doc_type = 'passport'
        new_doc_owner_name = 'Alexey'
        new_doc_shelf_number = '3'

        '''
        add_new_doc функция возвращает всего один параметр new_doc_shelf_number
        В результате мы на выходе получаем только номер полки
        Но как я понимаю, если все параметры введены правильно, то функция работает верно
        Вот тут у меня сомнения возникают, как проверить остальные параметры
        '''

        self.assertEqual(add_new_doc(new_doc_number, new_doc_type,
                                     new_doc_owner_name,
                                     new_doc_shelf_number), new_doc_shelf_number)

    def test_delete_doc(self):
        self.assertEqual(delete_doc('11-2'), ('11-2', True))

        """
        Так же и в delete_doc функции указывается номер документа и возвращаемое значение.
        Форматирование вывода функции происходит в программе уже на стадии ее вызова
        Я вывел, то что функция возвращает в неформатированном виде.
        """


if __name__ == '__main__':
    unittest.main()
