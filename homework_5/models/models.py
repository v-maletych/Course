import json
from framework.models import Model

class Plant(Model):
    file = "database/plants.json"
    fields = ["name", "address"]

    def __init__(self, name, address, id=None):
        self.name = name
        self.address = address
        self.id = id

    @classmethod
    def get_el_by_id(cls, id):
        data = cls.get_file_data()
        for el in data:
            if el["id"] == id:
                return cls(el["name"], el["address"], id=el["id"])


class Salon(Model):
    file = "database/salons.json"
    fields = ["name", "address"]

    def __init__(self, name, address, id=None):
        self.name = name
        self.address = address
        self.id = id

    @classmethod
    def get_el_by_id(cls, id):
        data = cls.get_file_data()
        for el in data:
            if el["id"] == id:
                return cls(el["name"], el["address"], id=el["id"])


class Employee(Model):
    file = "database/employees.json"
    fields = ["name", "email", "work_class", "work_id"]

    def __init__(self, name, email, work_class, work_id, id=None):
        self.name = name
        self.email = email
        self.work_class = work_class
        self.work_id = work_id
        self.id = id

    def generate_dict(self):
        data = super().generate_dict()
        data["work_class"] = self.work_class
        data["work_id"] = self.work_id
        return data

    @classmethod
    def get_el_by_id(cls, id):
        data = cls.get_file_data()
        for el in data:
            if el["id"] == id:
                return cls(el["name"], el["email"], el["work_class"], el["work_id"], id=el["id"])

    def update(self):
        data = self.get_file_data()
        for el in data:
            if el["id"] == self.id:
                el["name"] = input("Type a new name: ")
                el["email"] = input("Type a new email: ")
                el["work_class"] = input("Type a new work_class(Plant/Salon): ")
                el["work_id"] = int(input("Type a new work_id: "))
        self.save_to_file(data)

    @classmethod
    def get_employee_workplace(cls, id):
        data = cls.get_file_data()
        for el in data:
            if el["id"] == id:
                if el["work_class"] == "Plant":
                    with open("database/plants.json", "r") as f:
                        plants = json.load(f)
                    for plant in plants:
                        if plant["id"] == el["work_id"]:
                            print(f"Plant name: {plant['name']}")
                            print(f"Plant address: {plant['address']}")
                elif el["work_class"] == "Salon":
                    with open("database/salons.json", "r") as f:
                        salons = json.load(f)
                    for salon in salons:
                        if salon["id"] == el["work_id"]:
                            print(f"Salon name: {salon['name']}")
                            print(f"Salon address: {salon['address']}")
                else:
                    print("No workplace with this name exist")
