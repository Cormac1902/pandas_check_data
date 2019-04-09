import unittest
import load_csv as load
import check_csv as check
import os


class HeadersTestCase(unittest.TestCase):
    def setUp(self):
        self.csv_dir = 'D:\\Users\\Cormac\\OneDrive\\Family\\Cormac\\College\\NUIG\\Semester 2\\' \
                       'Industrial Development Project\\project_starter'
        self.file = 'upperheaders.csv'
        self.headers = load.get_headers(load.read_csv(os.path.join(self.csv_dir, self.file)))

    def test_headers(self):
        self.assertTrue(check.check_upper(self.headers), 'Not identifying uppercase headers')


if __name__ == '__main__':
    unittest.main()
