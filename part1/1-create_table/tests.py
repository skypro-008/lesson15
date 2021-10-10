import unittest
import main
import solution
import sqlite3
from tools import SkyproTestCase
import os


class DirectorsTestCase(SkyproTestCase):
    @classmethod
    def setUpClass(cls):
        cls.student_test_db = "./student_test.db"
        cls.author_test_db = "./author_test.db"
        cls.student_con = sqlite3.connect(cls.student_test_db)
        cls.author_con = sqlite3.connect(cls.author_test_db)
        cls.student_cur = cls.student_con.cursor()
        cls.author_cur = cls.author_con.cursor()
        cls.student_cur.execute(main.sqlite_query)
        cls.author_cur.execute(solution.sqlite_query)
        cls.student_table_names = cls.student_cur.execute(
            "SELECT tbl_name FROM sqlite_master WHERE type='table'").fetchall()
        cls.author_table_names = cls.author_cur.execute(
            "SELECT tbl_name FROM sqlite_master WHERE type='table'").fetchall()

    def test_table_name_is_correct(self):
        student_name = self.student_table_names[0][0]
        author_name = self.author_table_names[0][0]
        self.assertEqual(student_name, author_name,
                         r'%@Проверьте, правильно ли вы назвали таблицу.'
                         f'Таблица должна называться {author_name}, '
                         f'тогда как у вас в запросе {student_name}')

    def test_autoincrement_option_exists(self):
        student_tables = self.student_table_names
        self.assertTrue(
            ('sqlite_sequence',) in student_tables,
            r'%@Проверьте, что воспользовались оператором'
            ' AUTOINCREMENT при создании таблицы')

    def test_table_structure_is_correct(self):
        query = "SELECT * FROM animals"
        student_table = self.student_cur.execute(query).description
        author_table = self.author_cur.execute(query).description
        student_columns = [x[0] for x in student_table]
        author_columns = [x[0] for x in author_table]
        self.assertEqual(
            student_columns, author_columns,
            (r'%@ Проверьте, правильно ли определены поля в таблице.'
             f'Должны быть следующие поля {author_columns}, тогда как'
             f'у вас указаны {student_columns}'))

    def test_table_columns_type_is_correct(self):
        fields = {
            'id': 'integer',
            'animaltype': 'varchar',
            'name': 'varchar',
            'sex': 'varchar',
            'dateofbirth': 'date',
            'age': 'integer',
            'weight': 'decimal'
        }
        student_query = main.sqlite_query.lower()
        for key in fields.keys():
            x = student_query.find(key)
            string = student_query[x:].split(' ')
            value = fields[key]
            self.assertIn(
                str(value), string[1],
                f'Проверьте, правильно ли указан тип для поля {key}'
            )

    @classmethod
    def tearDownClass(cls):
        os.remove(cls.student_test_db)
        os.remove(cls.author_test_db)


if __name__ == "__main__":
    unittest.main()
