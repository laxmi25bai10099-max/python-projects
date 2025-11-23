import unittest
from student_manager.core import StudentManager
import os

class TestStudentManager(unittest.TestCase):
    def setUp(self):
        """
        Runs before each test.
        Creates a fresh test CSV file so every test starts clean.
        """
        self.test_file = 'test_students.csv'

        # Remove the file if it already exists
        if os.path.exists(self.test_file):
            os.remove(self.test_file)

        # Create a StudentManager object using the test file
        self.sm = StudentManager(self.test_file)

    def tearDown(self):
        """
        Runs after each test.
        Cleans up by deleting the temporary test file.
        """
        if os.path.exists(self.test_file):
            os.remove(self.test_file)

    def test_add_and_get(self):
        """
        Test whether a student can be added and retrieved successfully.
        """
        sid = self.sm.add_student("Alice", [80, 90, 70, 60, 50])
        student = self.sm.get_student_by_id(sid)

        self.assertIsNotNone(student)               # student should exist
        self.assertEqual(student['name'], "Alice")  # name must match
        self.assertEqual(student['total'], 350)     # total = sum of marks

    def test_update(self):
        """
        Test updating a student's marks.
        """
        sid = self.sm.add_student("Bob", [50, 50, 50, 50, 50])
        ok = self.sm.update_student(sid, [60, 60, 60, 60, 60])

        self.assertTrue(ok)                         # update should succeed
        st = self.sm.get_student_by_id(sid)
        self.assertEqual(st['total'], 300)          # new total

    def test_delete(self):
        """
        Test deleting a student record.
        """
        sid = self.sm.add_student("Carl", [40, 40, 40, 40, 40])
        ok = self.sm.delete_student(sid)

        self.assertTrue(ok)                        # delete should work
        self.assertIsNone(self.sm.get_student_by_id(sid))  # record removed

if __name__ == "__main__":
    unittest.main()