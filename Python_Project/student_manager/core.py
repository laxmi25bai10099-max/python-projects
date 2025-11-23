from .storage import Storage
from .utils import make_id, calc_result

class StudentManager:
    def __init__(self, path="students.csv"):
        self.db = Storage(path)

    def addStd(self, name, m):
        total, percentage, grade = calc_result(m)
        sid = make_id()

        row = {
            "id": sid,
            "name": name,
            "subject1": m[0],
            "subject2": m[1],
            "subject3": m[2],
            "subject4": m[3],
            "subject5": m[4],
            "total": total,
            "percentage": percentage,
            "grade": grade
        }
        self.db.add(row)
        return sid

    def getAll(self):
        return self.db.load()

    def getByID(self, sid):
        for r in self.db.load():
            if r["id"] == sid:
                return r
        return None

    def search(self, text):
        text = text.lower()
        out = []
        for r in self.db.load():
            if text in r["id"].lower() or text in r["name"].lower():
                out.append(r)
        return out

    def updateStd(self, sid, newm):
        rows = self.db.load()
        ok = False

        for r in rows:
            if r["id"] == sid:
                total, percentage, grade = calc_result(newm)

                r["subject1"] = newm[0]
                r["subject2"] = newm[1]
                r["subject3"] = newm[2]
                r["subject4"] = newm[3]
                r["subject5"] = newm[4]
                r["total"] = total
                r["percentage"] = percentage
                r["grade"] = grade
                ok = True
                break

        if ok:
            self.db.save(rows)

        return ok

    def removeStd(self, sid):
        rows = self.db.load()
        new_list = [r for r in rows if r["id"] != sid]

        if len(new_list) == len(rows):
            return False

        self.db.save(new_list)
        return True

    def exportCSV(self, fname):
        self.db.save_as(fname)