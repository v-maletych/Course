from models import Plant, Employee, Salon


while True:
    print("1. Add Plant\n2. Gel all plants\n3. Add Employee\n4. Get all employees\n5. Add Salon\n6. Get all salons\n7. Update employee\n8. Update Plant\n9. Update Salon")
    flag = int(input("Choose menu item: "))
    if flag == 1:
        name = input("Plant name: ")
        address = input("Plant address: ")
        plant = Plant(name, address)
        plant.save()
    elif flag == 2:
        Plant.get_all()
    elif flag == 3:
        name = input("Employee name: ")
        email = input("Employee email: ")
        work_class = input("Work class(Plant/Salon): ")
        work_id = int(input("Work id: "))
        employee = Employee(name, email, work_class=work_class, work_id=work_id)
        employee.save()
    elif flag == 4:
        Employee.get_all()
    elif flag == 5:
        name = input("Salon name: ")
        address = input("Salon address: ")
        salon = Salon(name, address)
        salon.save()
    elif flag == 6:
        Salon.get_all()
    elif flag == 7:
        print("1. Update employee info\n2. Get employee workplace info ")
        flag = int(input("Choose menu item: "))
        if flag == 1:
            id = int(input("ID which employee you want to update: "))
            employee = Employee.get_el_by_id(id)
            employee.update()
        elif flag == 2:
            id = int(input("ID which employee`s workplace you want to get: "))
            Employee.get_employee_workplace(id)
    elif flag == 8:
        id = int(input("ID which plant you want to update: "))
        plant = Plant.get_el_by_id(id)
        plant.update()
    elif flag == 9:
        id = int(input("ID which salon you want to update: "))
        salon = Salon.get_el_by_id(id)
        salon.update()
    else:
        print("Try again.")
