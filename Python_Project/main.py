from student_manager.core import StudentManager
from student_manager.utils import input_int, input_str

def main_menu():
    sm=StudentManager()
    while True:
        print("\n--- Student Result Management System ---")
        print("1.Add student")
        print("2.View all students")
        print("3.Search student")
        print("4.Update student")
        print("5.Delete student")
        print("6.Export CSV")
        print("0.Exit")
        choice =input_int("Choose an Option:")
        if choice == 1:
            name = input_str("Student name: ")
            marks = []
            for i in range(1, 6):
                m = input_int(f"Marks for Subject{i} (0-100): ")
                marks.append(m)
            sid = sm.add_student(name, marks)
            print(f"Student added with ID: {sid}")
        elif choice==2:
            rows=sm.list_students()
            if not rows:
                print("No student found ")
            else:
                for r in rows:
                    print(f"ID:{r['id']}|Name:{r['name']}|Total:{r['total']}|%:{r['percentage']:.2f}|Grade:{r['grade']}")

        elif choice==3:
            term=input_str("Enter student ID or name of search:")  
            res=sm.find_student(term)
            if res:
                for r in res:
                    print(r)
            else:
                print("no matching found.")
        elif choice ==4:
            sid=input_str("Enter student ID to update:")  
            student=sm.get_student_id(sid)
            if not student:
                print("student not found.") 
                continue
            print("Enter new marks (leave blank space to keep current):") 
            new_marks=[]
            for i in range(1,6):
                val=input(f"Subject{i}[{student[f'subject{i}']}]:").strip()  
                if val=="" :
                    new_marks.append(int(student[f"subject{i}"]))
                else:
                    try:
                        mv=int(val) 
                        if 0 <=mv<=100:
                            new_marks.append(mv)
                        else:
                            print("Invalid mark,keeping old.")
                    except:
                        print("Invalid input,keeping old.") 
                        new_marks.append(int(student[f"subjects{i}"]))
                        updated=sm.update_student(sid,new_marks)   
                        if updated:
                            print("student updated.")    
                        else:
                            print("update failed.")    
        elif choice==5:
            sid=input_str("Enter student ID to delete:") 
            ok=sm.delete_student(sid)
            if ok:
                print("Deleted successfully.")  
            else:
                print("Delete failed or student not found.")  
        elif choice==6:
            path=input_str("Enter filename to export (e.g.export.csv):")    
            sm.export_csv(path)
            print(f"Exported to {path}")
        elif choice==0:
            print("Goodbye.") 
            break
        else:
            print("Invalid choice.")   
if __name__=="__main__" :
    main_menu()                                  

