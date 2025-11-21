import unittest
from student_manager.core import StudentManager
import os

class TestStudentManager(unittest.TestCase):
    def setUp(self):
        self.test_file = 'test_students.csv'
        if os.path.exists(self.test_file):
            os.remove(self.test_file)
        self.sm = StudentManager(self.test_file)

    def tearDown(self):
        if os.path.exists(self.test_file):
            os.remove(self.test_file)

    def test_add_and_get(self):
        sid = self.sm.add_student("Alice", [80,90,70,60,50])
        student = self.sm.get_student_by_id(sid)
        self.assertIsNotNone(student)
        self.assertEqual(student['name'], "Alice")
        self.assertEqual(student['total'], 350)

    def test_update(self):
        sid = self.sm.add_student("Bob", [50,50,50,50,50])
        ok = self.sm.update_student(sid, [60,60,60,60,60])
        self.assertTrue(ok)
        st = self.sm.get_student_by_id(sid)
        self.assertEqual(st['total'], 300)

    def test_delete(self):
        sid = self.sm.add_student("Carl", [40,40,40,40,40])
        ok = self.sm.delete_student(sid)
        self.assertTrue(ok)
        self.assertIsNone(self.sm.get_student_by_id(sid))

if __name__ == "__main__":
    unittest.main()