def  hello():
    print("Hello AkiraChix")

def sayhello(name):
    print(f"hello {name}")

def hello_student(name,age):
    year=2025-age
    print(f"Hello {name} , born in{year}")

def hello_studnts(name="jane",age=20):
    year=2025-age
    print(f"Hello {name} ,born in {year}")

def my_country(name="Uganda"):
    print(f"I love my country {name}")

def hello_students(*students):
    for student in students:
        print(f"Hello {students}")
def welcome_student(**kwarys):
    name=kwarys.get("name","Stranger")
    age=kwarys.get("age","undefined")
    country=kwarys.get("country","unknown")
    print(f"Hello {name} from {country} ,your age is {age}")


def stats(*args ,**kwargs):
    print(args)
    print(kwargs)


    


