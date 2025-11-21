import csv
from pathlib import Path

class Storage:
    def __init__(self, path='students.csv'):
        self.path = Path(path)
        if not self.path.exists():
            self._create_file()

    def _create_file(self):
        with open(self.path, 'w', newline='', encoding='utf-8') as f:
            writer = csv.writer(f)
            writer.writerow([
                'id','name','subject1','subject2','subject3','subject4','subject5','total','percentage','grade'
            ])

    def read_all(self):
        rows = []
        with open(self.path, 'r', encoding='utf-8') as f:
            reader = csv.DictReader(f)
            for r in reader:
                for k in ['subject1','subject2','subject3','subject4','subject5','total']:
                    r[k] = int(r[k])
                r['percentage'] = float(r['percentage'])
                rows.append(r)
        return rows

    def save_all(self, rows):
        with open(self.path, 'w', newline='', encoding='utf-8') as f:
            fieldnames = [
                'id','name','subject1','subject2','subject3','subject4','subject5','total','percentage','grade'
            ]
            writer = csv.DictWriter(f, fieldnames=fieldnames)
            writer.writeheader()
            for r in rows:
                writer.writerow(r)

    def append(self, row):     # <-- THIS FUNCTION MUST EXIST
        with open(self.path, 'a', newline='', encoding='utf-8') as f:
            writer = csv.writer(f)
            writer.writerow([
                row['id'], row['name'],
                row['subject1'], row['subject2'], row['subject3'],
                row['subject4'], row['subject5'],
                row['total'], f"{row['percentage']:.2f}", row['grade']
            ])