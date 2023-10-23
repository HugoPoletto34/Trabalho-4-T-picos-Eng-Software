import os
import unittest
from dataProcessor import read_json_file, avgAgeCountry, qualPaisComMaiorMediaDeIdade, qualPaisComMenorMediaDeIdade


class TestDataProcessor(unittest.TestCase):
    def test_read_json_file_success(self):
        current_directory = os.path.dirname(__file__)
        file_path = os.path.join(current_directory, "users.json")

        data = read_json_file(file_path)

        self.assertEqual(len(data), 1000)  # Ajustar o número esperado de registros
        self.assertEqual(data[0]['name'], 'Pamela Jones')
        self.assertEqual(data[1]['age'], 23)

    def test_read_json_file_file_not_found(self):
        with self.assertRaises(FileNotFoundError):
            read_json_file("non_existent.json")

    def test_read_json_file_invalid_json(self):
        with open("invalid.json", "w") as file:
            file.write("invalid json data")
        with self.assertRaises(ValueError):
            read_json_file("invalid.json")

    def test_avarage_age_function(self):
        current_directory = os.path.dirname(__file__)
        file_path = os.path.join(current_directory, "users.json")

        data = read_json_file(file_path)

        avgAges = avgAgeCountry(data)

        self.assertEqual(avgAges['US'], '41.99')
        self.assertEqual(avgAges['UK'], '39.73')
        self.assertEqual(avgAges['CA'], '39.57')
        self.assertEqual(avgAges['AU'], '38.24')
        self.assertEqual(avgAges['FR'], '38.10')
        self.assertEqual(avgAges['DE'], '38.45')
        self.assertEqual(avgAges['JP'], '37.96')
        self.assertEqual(avgAges['BR'], '41.41')

    def test_data_null_avarage_function(self):
        avgAges = avgAgeCountry({})

        self.assertEqual(avgAges, {})

    def test_zero_ages(self):
        data = [{'name': 'Pamela Jones', 'age': 0, 'country': 'US'}, {'name': 'Pamela Jones', 'age': 0, 'country': 'US'}]
        avgAges = avgAgeCountry(data);

        self.assertEqual(avgAges['US'], '0.00')

    def test_exception_when_none_ages(self):
        data = [{'name': 'Pamela Jones', 'country': 'US'}, {'name': 'Pamela Jones', 'country': 'US'}]

        with self.assertRaises(Exception):
            avgAgeCountry(data)

    def test_exception_when_none_country(self):
        data = [{'name': 'Pamela Jones', 'age': 0}, {'name': 'Pamela Jones', 'age': 0}]

        with self.assertRaises(Exception):
            avgAgeCountry(data)

    def test_exception_when_void_country(self):
        data = [{'name': 'Pamela Jones', 'age': 0, 'country': ''}, {'name': 'Pamela Jones', 'age': 0, 'country': ''}]

        with self.assertRaises(Exception):
            avgAgeCountry(data)

    def test_qualPaisComMaiorMediaDeIdade(self):
        current_directory = os.path.dirname(__file__)
        file_path = os.path.join(current_directory, "users.json")

        data = read_json_file(file_path)

        pais = qualPaisComMaiorMediaDeIdade(data)

        self.assertEqual(pais, 'US')

    def test_qualPaisComMaiorMediaDeIdade_empty(self):
        pais = qualPaisComMaiorMediaDeIdade([])

        self.assertEqual(pais, '')

    def test_qualPaisComMenorMediaDeIdade(self):
        current_directory = os.path.dirname(__file__)
        file_path = os.path.join(current_directory, "users.json")

        data = read_json_file(file_path)

        pais = qualPaisComMenorMediaDeIdade(data)

        self.assertEqual(pais, 'JP')

    def test_qualPaisComMenorMediaDeIdade_empty(self):
        pais = qualPaisComMenorMediaDeIdade([])

        self.assertEqual(pais, '')

    def test_avgAgeCountry_with_transform(self):
        current_directory = os.path.dirname(__file__)
        file_path = os.path.join(current_directory, "users.json")

        data = read_json_file(file_path)

        avgAges = avgAgeCountry(data, lambda x: x * 12)

        self.assertEqual(avgAges['US'], '503.90')
        self.assertEqual(avgAges['UK'], '476.75')
        self.assertEqual(avgAges['CA'], '474.87')
        self.assertEqual(avgAges['AU'], '458.91')
        self.assertEqual(avgAges['FR'], '457.23')
        self.assertEqual(avgAges['DE'], '461.37')
        self.assertEqual(avgAges['JP'], '455.51')
        self.assertEqual(avgAges['BR'], '496.95')

    def test_avgAgeCountry_with_transform_empty(self):
        avgAges = avgAgeCountry({}, lambda x: x * 12)

        self.assertEqual(avgAges, {})



if __name__ == '__main__':
    unittest.main()