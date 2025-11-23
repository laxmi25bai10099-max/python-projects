import csv
from pathlib import Path

class Storage:
    def __init__(self, path="students.csv"):
        self.path = Path(path)
        if not self.path.exists():
            self._make()

    def _make(self):
        with open(self.path, "w", newline="") as f:
            w = csv.writer(f)
            w.writerow(["id","name","subject1","subject2","subject3","subject4","subject5","total","percentage","grade"])

    def load(self):
        data = []
        with open(self.path, "r") as f:
            r = csv.DictReader(f)
            for x in r:
                for s in ["subject1","subject2","subject3","subject4","subject5","total"]:
                    x[s] = int(x[s])
                x["percentage"] = float(x["percentage"])
                data.append(x)
        return data

    def save(self, rows):
        with open(self.path, "w", newline="") as f:
            head = ["id","name","subject1","subject2","subject3","subject4","subject5","total","percentage","grade"]
            w = csv.DictWriter(f, fieldnames=head)
            w.writeheader()
            for r in rows:
                w.writerow(r)

    def add(self, r):
        with open(self.path, "a", newline="") as f:
            w = csv.writer(f)
            w.writerow([
                r["id"], r["name"],
                r["subject1"], r["subject2"], r["subject3"], r["subject4"], r["subject5"],
                r["total"], f"{r['percentage']:.2f}", r["grade"]
            ])

    def save_as(self, fname):
        rows = self.load()
        with open(fname, "w", newline="") as f:
            head = ["id","name","subject1","subject2","subject3","subject4","subject5","total","percentage","grade"]
            w = csv.DictWriter(f, fieldnames=head)
            w.writeheader()
            for r in rows:
                w.writerow(r)