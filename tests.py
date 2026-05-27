import unittest
from src.core.matching import levenshtein, name_similarity, verify

class TestLevenshtein(unittest.TestCase):
    def test_identical_strings(self):
        self.assertEqual(levenshtein("peter","peter"),0)

    def test_one_replacement(self):
        self.assertEqual(levenshtein("adeola","adaola"),1)

    def test_completely_different(self):
        self.assertGreater(levenshtein("peter","james"),3)

class TestNameSimilarity(unittest.TestCase):
    def test_exact_match(self):
        self.assertEqual(name_similarity("Adeola", "Adeola"), 1.0)

    def test_fuzzy_match(self):
        score = name_similarity("Adeola", "Adaola")
        self.assertGreater(score, 0.7)

    def test_no_match(self):
        score = name_similarity("Peter", "James")
        self.assertLess(score, 0.5)

class TestVerify(unittest.TestCase):
    
    def test_full_match(self):
        req = {"name": "Adeola Bello", "dob": "01/01/1990"}
        rec = {"name": "Adeola Bello", "dob": "01/01/1990"}
        result = verify(req, rec)
        self.assertEqual(result["result"], "MATCH")

    def test_partial_match(self):
        req = {"name": "Adeola Belo", "dob": "01/01/1990"}
        rec = {"name": "Adeola Bello", "dob": "01/01/1990"}
        result = verify(req, rec)
        self.assertEqual(result["result"], "PARTIAL")

    def test_no_match(self):
        req = {"name": "James Okafor", "dob": "01/01/1990"}
        rec = {"name": "Adeola Bello", "dob": "01/01/1990"}
        result = verify(req, rec)
        self.assertEqual(result["result"], "NO_MATCH")

if __name__ == "__main__":
    unittest.main(verbosity=2)

