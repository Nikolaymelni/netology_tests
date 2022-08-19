from YA_API import create_folder, delete_folder
import unittest


class TestCreateFolderUnitTest(unittest.TestCase):

    def test_creating_new_folder_yandex_disk(self):
        self.assertEqual(create_folder("test"), 201)

    def test_delete_folder_yandex_disk(self):
        self.assertEqual(delete_folder('test'), 204)
