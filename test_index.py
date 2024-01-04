import unittest
from main import index_files
import os

class TestIndexFiles(unittest.TestCase):

    def test_empty_directory(self):
        with self.assertRaises(ValueError):
            index_files('empty_dir')

    def test_index_txt_files(self):
        directory = 'test_files'
        os.makedirs(directory, exist_ok=True)
        with open(os.path.join(directory, 'file1.txt'), 'w') as f:
            f.write('hello world')
        with open(os.path.join(directory, 'file2.txt'), 'w') as f:
            f.write('goodbye world')
        index = index_files(directory)
        self.assertEqual(index, {'file1.txt': {'hello', 'world'}, 'file2.txt': {'goodbye', 'world'}})

