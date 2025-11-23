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
            w.writerow(["id","name","sub1","sub2","sub3","sub4","sub5","total","per","grade"])

    def load(self):
        data = []
        with open(self.path, "r") as f:
            r = csv.DictReader(f)
            for x in r:
                for s in ["sub1","sub2","sub3","sub4","sub5","total"]:
                    x[s] = int(x[s])
                x["per"] = float(x["per"])
                data.append(x)
        return data

    def save(self, rows):
        with open(self.path, "w", newline="") as f:
            head = ["id","name","sub1","sub2","sub3","sub4","sub5","total","per","grade"]
            w = csv.DictWriter(f, fieldnames=head)
            w.writeheader()
            for r in rows:
                w.writerow(r)

    def add(self, r):
        with open(self.path, "a", newline="") as f:
            w = csv.writer(f)
            w.writerow([
                r["id"], r["name"],
                r["sub1"], r["sub2"], r["sub3"], r["sub4"], r["sub5"],
                r["total"], f"{r['per']:.2f}", r["grade"]
            ])

    def save_as(self, fname):
        rows = self.load()
        with open(fname, "w", newline="") as f:
            head = ["id","name","sub1","sub2","sub3","sub4","sub5","total","per","grade"]
            w = csv.DictWriter(f, fieldnames=head)
            w.writeheader()
            for r in rows:
                w.writerow(r)