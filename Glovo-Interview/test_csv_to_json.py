import unittest
import os
import json
from csv_to_json import csv_to_json

class TestCSVToJSON(unittest.TestCase):

    def setUp(self):
        # Create a sample CSV file for testing
        self.test_csv = "test_data.csv"
        self.test_json = "test_data.json"

        with open(self.test_csv, "w", encoding="utf-8") as f:
            f.write("id,name,role\n")
            f.write("1,Alice,Engineer\n")
            f.write("2,Bob,Analyst\n")

    def tearDown(self):
        # Clean up files after test
        if os.path.exists(self.test_csv):
            os.remove(self.test_csv)
        if os.path.exists(self.test_json):
            os.remove(self.test_json)

    def test_csv_to_json_conversion(self):
        result = csv_to_json(self.test_csv, self.test_json)

        expected = [
            {"id": "1", "name": "Alice", "role": "Engineer"},
            {"id": "2", "name": "Bob", "role": "Analyst"}
        ]

        self.assertEqual(result, expected)

        # Verify JSON file contents
        with open(self.test_json, "r", encoding="utf-8") as f:
            json_data = json.load(f)

        self.assertEqual(json_data, expected)


if __name__ == "__main__":
    unittest.main()
