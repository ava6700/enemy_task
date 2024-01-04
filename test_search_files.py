import unittest
from main import search_files

class TestSearchFiles(unittest.TestCase):

    def test_no_results(self):
        index = {'file1.txt': {'hello', 'world'}}
        results = search_files(index, ['python'])
        self.assertEqual(results, [])

    def test_multiple_results(self):
        index = {'file1.txt': {'hello', 'world'}, 'file2.txt': {'hello', 'python'}}
        results = search_files(index, ['hello'])
        self.assertEqual(results, [('file2.txt', 100), ('file1.txt', 50)])

