import unittest
import app


class TestSecretaryProgram(unittest.TestCase):

    def setUp(self):
        print('method setUp')

    def tearDown(self):
        print('method tearDown')

    def test_get_doc_owner_name(self):
        self.assertEqual(app.get_doc_owner_name('2207 876234'), 'Василий Гупкин')

    def test_add_new_doc(self):
        self.assertEqual(app.add_new_doc('11 22 334455', 'Айди кард', 'Иванов Иван', 2), 2)

    def test_delete_doc(self):
        self.assertTrue(app.delete_doc('10006'))

    def test_get_all_doc_owners_names(self):
        self.assertIsInstance(app.get_all_doc_owners_names(), set)


if __name__ == '__main__':
    unittest.main()