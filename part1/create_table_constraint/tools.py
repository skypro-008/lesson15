import unittest
import sqlite3
import os

class StatMixin:
    def send_stat(self, result):
        if result.wasSuccessful():
            print(f"Тест {result.testsRun} пройден успешно!")


class SkyproTestCase(StatMixin, unittest.TestCase):
    def run(self, *args, **kwargs):
        result = super().run(*args, **kwargs)
        x = len(result.failures) - 1
        if len(result.failures) == 0:
            pass
        else:
            error_ind = result.failures[x][-1].find('%@')
            if error_ind != -1:
                error_text = result.failures[x][-1][error_ind+2:]
                testcase = result.failures[x][0]
                new_error_output = (testcase, error_text)
                result.failures[x] = new_error_output
        self.send_stat(result)

    def get_query_info(self, query):
        from_sql_checker = self._sql_checker(query)
        from_cursor = self.get_cursor_info(query)
        return {"query_info": from_sql_checker,
                "cursor_info": from_cursor}

    def _get_db_cursor(self, query):
        con = sqlite3.connect("../netflix.db")
        cur = con.cursor()
        cur.execute(query)
        return cur

    def get_cursor_info(self, query):
        cur = self._get_db_cursor(query)
        columns = cur.description
        columns_len = len(columns)
        names_of_columns = []
        query_result = cur.fetchall()
        rows_count = len(query_result)
        for name in columns:
            names_of_columns.append(name[0])
        return {"columns": names_of_columns,
                "columns_count": columns_len,
                "query_result": query_result,
                "rows_count": rows_count}

    def _sql_checker(self, query: str):
        query = query.lower()
        keywords = self._get_key_words(query)
        select_ind = query.find('select ')
        from_ind = query.find('from ')
        where_ind = query.find('where ')
        and_ind = query.find(' and ')
        select_block = query[select_ind:from_ind]
        from_block = query[from_ind:where_ind]
        where_block = query[where_ind:]
        and_block = None
        if and_ind:
            where_block = query[where_ind:and_ind]
            and_block = query[and_ind:]
        blocks = {'колонка': select_block,
                  'таблица': from_block,
                  'условие': where_block,
                  'доп условие': and_block}
        for key, value in blocks.items():
            blocks[key] = self._cleaner(blocks[key])
        blocks['keywords'] = keywords
        return blocks

    def _cleaner(self, lst):
        lst = lst.split(' ')
        key_words = ['select', 'from', 'where', 'like', 'distinct', 'and', '']
        for value in key_words:
            if value in lst:
                lst.remove(value)
        for value in lst:
            if ',' in value:
                devided_value = value.split(',')
                try:
                    devided_value.remove('')
                except:
                    pass
                lst.remove(value)
                lst += devided_value
        return lst

    def _get_key_words(self, query):
        keywords = ['select', 'from', 'where', 'like', 'group by', 'distinct', 'limit', 'order by']
        lst = []
        for keyword in keywords:
            if keyword in query:
                lst.append(keyword)
        return lst

def clean_base(*args):
    try:
        for arg in args:
            os.remove(arg)
    except:
        pass