import uuid
def calculate_total_percentage_grade(marks):
    total=sum(marks)
    percentage=total/(len(marks)*100)*100
    if percentage>=90:
        grade="A+"
    elif percentage>=80:
        grade="A"
    elif percentage >=70:
        grade="B"
    elif percentage >=60:
        grade="C"  
    elif percentage >=50:
        grade="D"
    else:
        grade="F"
    return total,percentage,grade
def generate_id():
    return str (uuid.uuid4())[:8]
def input_int(prompt,minv=None,maxv=None):
    while True:
        val=input(prompt)
        try:
            ival=int(val)
            if(minv is not None and ival<minv)or(maxv is not None and ival>maxv):
                print("value out of range:")    
                continue
            return ival
        except ValueError:
            print("Enter a valid integer.")
def input_str(prompt):
    while True:
        s=input(prompt).strip()     
        if s=="":
            print("Input cannot be empty")
        else:
            return s           
