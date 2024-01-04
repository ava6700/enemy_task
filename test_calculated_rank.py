import unittest
from main import calculate_rank

class TestCalculateRank(unittest.TestCase):

    def test_empty_search_words(self):
        self.assertEqual(calculate_rank([], set()), 0)

    def test_no_common_words(self):
        self.assertEqual(calculate_rank(['hello'], {'world'}), 0)

    def test_partial_match(self):
        self.assertEqual(calculate_rank(['hello', 'world'], {'hello', 'python'}), 50)

    def test_full_match(self):
        self.assertEqual(calculate_rank(['hello', 'world'], {'hello', 'world'}), 100)

