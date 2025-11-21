from .storage import Storage
from .utils import calculate_total_percentage_grade,generate_id

class StudentManager:
    def __init__(self,storage_path='students.csv'):
        self.storage=Storage(storage_path)
    def add_student(self,name,marks):
        total,percentage,grade=calculate_total_percentage_grade(marks) 
        sid =generate_id()
        row={
            'id':sid,
            'name':name,
            'subject1':marks[0],
            'subject2':marks[1],
            'subject3':marks[2],
            'subject4':marks[3],
            'subject5':marks[4],
            'total':total,
            'percentage':percentage,
            'grade':grade
        }   
        self.storage.append(row)
        return sid
    def list_students(self):
        return self.storage.read_all()
    def get_student_by_id(self,sid):
        rows=self.list_students()
        for r in rows:
            if r['id']==sid:
                return r
            return None
    def find_student(self,term):
        term=term.strip().lower()
        rows=self.list_students()
        found=[]
        for r in rows:
            if r['id']==term or term in r['name'].lower():
                found.append(r)
        return found
    def update_student(self,sid,new_marks):
        rows=self.list_students()
        update = False
        for r in rows:
            if r['id']==sid:
                total,percentage,grade=calculate_total_percentage_grade(new_marks)
                r['subject1']=new_marks[0]
                r['subject2']=new_marks[1]
                r['subject3']=new_marks[2]
                r['subject4']=new_marks[3]
                r['subject5']=new_marks[4]
                r['total']=total
                r['percentage']=percentage
                r['grade']=grade
                updated=True
                break
            if updated:
                self.storage.save_all(rows)
            return updated
    def delete_student(self,sid):
        rows=self.list_students()
        new_rows=[r for r in rows if r['id']!=sid] 
        if len(new_rows)==len(rows):
            return False
        self.storage.save_all(new_rows)
        return True
    def export_csv(self,path):
        rows=self.list_students()
        with open(path,'w',newline='',encoding='utf-8')as f:
            import csv
            fieldnames=['id','name','subject1','subject2','subject3','subject4','subject5','total','percentage','grade']
            writer=csv.DictWriter(f,fieldnames=fieldnames)
            writer.writeheader()
            for r in rows:
                writer.writerow(r)
                        
                       
    
        