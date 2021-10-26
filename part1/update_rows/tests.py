import unittest
import main
import solution
import sqlite3
from tools import SkyproTestCase
import os
from tools import create_table, clean_base


class UpdateTestCase(SkyproTestCase):
    @classmethod
    def setUpClass(cls):
        cls.student_test_db = "./student_test.db"
        cls.author_test_db = "./author_test.db"
        test_b = os.path.exists(cls.author_test_db)
        test_author_b = os.path.exists(cls.author_test_db)
        if test_b or test_author_b:
            clean_base(cls.student_test_db, cls.author_test_db)
        cls.student_con = sqlite3.connect(cls.student_test_db)
        cls.author_con = sqlite3.connect(cls.author_test_db)
        cls.student_con = create_table(cls.student_con)
        cls.author_con = create_table(cls.author_con)
        cls.student_cur = cls.student_con.cursor()
        cls.author_cur = cls.author_con.cursor()
        cls.student_cur.execute(main.sqlite_query_first)
        cls.student_cur.execute(main.sqlite_query_second)
        cls.author_cur.execute(solution.sqlite_query_first)
        cls.author_cur.execute(solution.sqlite_query_second)

    def test_first_row_is_added(self):
        query = (
            "SELECT * FROM animals where "
            "`AnimalType`='Кошка' "
            "AND `Age`=4 "
            "AND `Weight`=4.5 "
            "AND `Sex`='М' "
            "AND `DateOfBirth`='2017-05-03' "
            "AND `Name`='Семен'"
        )
        student_value = self.student_cur.execute(query).fetchall()
        author_value = self.author_cur.execute(query).fetchall()
        self.assertEqual(student_value, author_value,
                         (r'%@Проверьте, правильно ли '
                          'вы изменили данные про кота Семена'))

    def test_second_row_is_added(self):
        query = (
            "SELECT * FROM animals where "
            "`AnimalType`='Собака' "
            "AND `Age`=6 "
            "AND `Weight`=5.75 "
            "AND `Sex`='М'"
            "AND `DateOfBirth`='2015-08-25'"
            "AND `Name`='Бобик'"
        )
        student_value = self.student_cur.execute(query).fetchall()
        author_value = self.author_cur.execute(query).fetchall()
        self.assertEqual(student_value, author_value,
                         (r'%@Проверьте, правильно ли '
                          'вы изменили данные про пса Бобика'))

    @classmethod
    def tearDownClass(cls):
        cls.student_con.close()
        cls.author_con.close()
        os.remove(cls.student_test_db)
        os.remove(cls.author_test_db)


if __name__ == "__main__":
    unittest.main()
