from student_manager.core import StudentManager
from student_manager.utils import get_int, get_text

def main_menu():
    sm = StudentManager()

    while True:
        print("\n--- Student Result Management System ---")
        print("1. Add Student")
        print("2. View Students")
        print("3. Search Student")
        print("4. Update Marks")
        print("5. Delete Student")
        print("6. Export CSV")
        print("0. Exit")

        choice = get_int("Choose: ")

        if choice == 1:
            name = get_text("Student name: ")

            marks = []
            for i in range(1, 6):
                m = get_int(f"Marks for Subject {i} (0-100): ", 0, 100)
                marks.append(m)

            sid = sm.addStd(name, marks)
            print("Student added. ID:", sid)

        elif choice == 2:
            data = sm.getAll()
            if len(data) == 0:
                print("No records found.")
            else:
                for s in data:
                    print(f"{s['id']} | {s['name']} | Total={s['total']} | %={s['per']:.2f} | Grade={s['grade']}")

        elif choice == 3:
            t = get_text("Enter ID or name: ")
            out = sm.search(t)
            if out:
                for s in out:
                    print(s)
            else:
                print("Not found.")

        elif choice == 4:
            sid = get_text("Enter student ID: ")
            st = sm.getByID(sid)

            if not st:
                print("Student not found.")
                continue

            print("Leave blank to keep old marks.")
            newm = []

            for i in range(1, 5+1):
                old = st[f"sub{i}"]
                x = input(f"Subject {i} [{old}]: ").strip()
                if x == "":
                    newm.append(old)
                else:
                    try:
                        x = int(x)
                        if 0 <= x <= 100:
                            newm.append(x)
                        else:
                            newm.append(old)
                    except:
                        newm.append(old)

            ok = sm.updateStd(sid, newm)
            if ok:
                print("Updated.")
            else:
                print("Update failed.")

        elif choice == 5:
            sid = get_text("ID to delete: ")
            if sm.removeStd(sid):
                print("Deleted.")
            else:
                print("Not found.")

        elif choice == 6:
            fn = get_text("Filename (ex: out.csv): ")
            sm.exportCSV(fn)
            print("Exported to", fn)

        elif choice == 0:
            print("Bye!")
            break

        else:
            print("Invalid choice.")

if __name__ == "__main__":
    main_menu()