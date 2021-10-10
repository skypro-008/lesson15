import unittest
import main
import solution
import sqlite3
from tools import SkyproTestCase
import os
from tools import create_table


class DirectorsTestCase(SkyproTestCase):
    @classmethod
    def setUpClass(cls):
        cls.student_test_db = "./student_test.db"
        cls.author_test_db = "./author_test.db"
        cls.student_con = sqlite3.connect(cls.student_test_db)
        cls.author_con = sqlite3.connect(cls.author_test_db)
        cls.student_con = create_table(cls.student_con)
        cls.author_con = create_table(cls.author_con)
        cls.student_cur = cls.student_con.cursor()
        cls.author_cur = cls.author_con.cursor()
        cls.student_cur.execute(main.sqlite_query_first)
        cls.student_cur.execute(main.sqlite_query_second)
        cls.author_cur.executescript(solution.sqlite_query)

    def test_first_row_is_added(self):
        query = (
            "SELECT * FROM animals where "
            "`AnimalType`='Кошка' "
            "AND `Age`=7 "
            "AND `Weight`=2.15 "
            "AND `Sex`='Ж' "
            "AND `DateOfBirth`='2013-12-02' "
            "AND `Name`='Соня'"
        )
        student_value = self.student_cur.execute(query).fetchall()
        author_value = self.author_cur.execute(query).fetchall()
        self.assertEqual(student_value, author_value,
                         (r'%@Проверьте, остались ли '
                          'в таблице данные про кошку Соню'))

    def test_second_row_is_added(self):
        query = (
            "SELECT * FROM animals where "
            "`AnimalType`='Кот' "
            "AND `Age`=4 "
            "AND `Weight`=4.5 "
            "AND `Sex`='М' "
            "AND `DateOfBirth`='2017-05-03' "
            "AND `Name`='Семен'"
        )
        student_value = self.student_cur.execute(query).fetchall()
        author_value = self.author_cur.execute(query).fetchall()
        self.assertEqual(student_value, author_value,
                         (r'%@Проверьте, остались ли '
                          'в таблице данные про кота Семена'))

    def test_third_row_is_added(self):
        query = (
            "SELECT * FROM animals where "
            "`AnimalType`='Собака' "
            "AND `Age`=2 "
            "AND `Weight`=20.8 "
            "AND `Sex`='Ж' "
            "AND `DateOfBirth`='2018-11-12' "
            "AND `Name`='Алина'"
        )
        student_value = self.student_cur.execute(query).fetchall()
        author_value = self.author_cur.execute(query).fetchall()
        self.assertEqual(student_value, author_value,
                         (r'%@Проверьте, удалены ли '
                          'из таблицы данные про собаку Алину'))

    def test_fourth_row_is_added(self):
        query = (
            "SELECT * FROM animals where "
            "`AnimalType`='Пес' "
            "AND `Age`=6 "
            "AND `Weight`=5.75 "
            "AND `Sex`='М'"
            "AND `DateOfBirth`='2015-08-25'"
            "AND `Name`='Бобик'"
        )
        student_value = self.student_cur.execute(query).fetchall()
        author_value = self.author_cur.execute(query).fetchall()
        self.assertEqual(student_value, author_value,
                         (r'%@Проверьте, остались ли '
                          'в таблице данные про пса Бобика'))

    @classmethod
    def tearDownClass(cls):
        os.remove(cls.student_test_db)
        os.remove(cls.author_test_db)


if __name__ == "__main__":
    unittest.main()
