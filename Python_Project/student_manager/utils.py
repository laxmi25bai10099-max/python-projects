import uuid

def calc_result(m):
    tot = sum(m)
    per = (tot / (len(m) * 100)) * 100

    if per >= 90:
        g = "A+"
    elif per >= 80:
        g = "A"
    elif per >= 70:
        g = "B"
    elif per >= 60:
        g = "C"
    elif per >= 50:
        g = "D"
    else:
        g = "F"

    return tot, per, g


def make_id():
    return str(uuid.uuid4())[:6]


def get_int(msg, mn=None, mx=None):
    while True:
        x = input(msg)
        try:
            x = int(x)
            if mn is not None and x < mn:
                print("Out of range.")
                continue
            if mx is not None and x > mx:
                print("Out of range.")
                continue
            return x
        except:
            print("Enter number only.")


def get_text(msg):
    while True:
        s = input(msg).strip()
        if s == "":
            print("Can't be empty.")
        else:
            return s