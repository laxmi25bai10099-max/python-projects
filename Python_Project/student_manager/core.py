from .storage import Storage
from .utils import make_id, calc_result

class StudentManager:
    def __init__(self, path="students.csv"):
        self.db = Storage(path)

    def addStd(self, name, m):
        tot, per, gr = calc_result(m)
        sid = make_id()

        row = {
            "id": sid,
            "name": name,
            "sub1": m[0],
            "sub2": m[1],
            "sub3": m[2],
            "sub4": m[3],
            "sub5": m[4],
            "total": tot,
            "per": per,
            "grade": gr
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
                tot, per, gr = calc_result(newm)

                r["sub1"] = newm[0]
                r["sub2"] = newm[1]
                r["sub3"] = newm[2]
                r["sub4"] = newm[3]
                r["sub5"] = newm[4]
                r["total"] = tot
                r["per"] = per
                r["grade"] = gr
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