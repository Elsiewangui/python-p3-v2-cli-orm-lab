from models.department import Department
from models.employee import Employee


def exit_program():
    print("Goodbye!")
    exit()

# We'll implement the department functions in this lesson


def list_departments():
    departments = Department.get_all()
    for department in departments:
        print(department)


def find_department_by_name():
    name = input("Enter the department's name: ")
    department = Department.find_by_name(name)
    print(department) if department else print(
        f'Department {name} not found')


def find_department_by_id():
    # use a trailing underscore not to override the built-in id function
    id_ = input("Enter the department's id: ")
    department = Department.find_by_id(id_)
    print(department) if department else print(f'Department {id_} not found')


def create_department():
    name = input("Enter the department's name: ")
    location = input("Enter the department's location: ")
    try:
        department = Department.create(name, location)
        print(f'Success: {department}')
    except Exception as exc:
        print("Error creating department: ", exc)


def update_department():
    id_ = input("Enter the department's id: ")
    if department := Department.find_by_id(id_):
        try:
            name = input("Enter the department's new name: ")
            department.name = name
            location = input("Enter the department's new location: ")
            department.location = location

            department.update()
            print(f'Success: {department}')
        except Exception as exc:
            print("Error updating department: ", exc)
    else:
        print(f'Department {id_} not found')


def delete_department():
    id_ = input("Enter the department's id: ")
    if department := Department.find_by_id(id_):
        department.delete()
        print(f'Department {id_} deleted')
    else:
        print(f'Department {id_} not found')


# You'll implement the employee functions in the lab

def list_employees():
    employees = Employee.get_all()
    for employee in employees:
        print(employee)


def find_employee_by_name():
    name = input("Enter the employee's name: ")
    employee = Employee.find_by_name(name)
    print(employee) if employee else print(
        f'Employee {name} not found')


def find_employee_by_id():
    id_ = input("Enter the employee's id: ")
    employee = Employee.find_by_id(id_)
    print(employee) if employee else print(f'Employee {id_} not found')



def create_employee():
    try:
        # Prompt for and read in the employee's details
        name = input("Enter the employee's name: ")
        job_title = input("Enter the employee's job title: ")
        department_id = input("Enter the employee's department ID: ")

        # Convert department_id to an integer
        department_id = int(department_id)

        # Check if the department ID exists in the database
        department = Department.find_by_id(department_id)
        if not department:
            print(f"Error: Department ID {department_id} does not exist.")
            return

        # Create and persist a new Employee instance
        employee = Employee.create(name, job_title, department_id)

        # Print success message
        print(f'Success: Employee {employee.name} created with ID {employee.id}.')

    except ValueError:
        print("Error: Department ID must be a number.")
    except Exception as exc:
        print(f"Error creating employee: {exc}")

def update_employee():
    id_ = input("Enter the employee's id: ")
    employee = Employee.find_by_id(id_)

    if not employee:
        print(f'Employee {id_} not found.')
        return

    try:
        # Prompt for and update the employee's name
        name = input("Enter the employee's new name: ")
        employee.name = name  # This may throw an exception if validation fails

        # Prompt for and update the employee's job title
        job_title = input("Enter the employee's new job title: ")
        employee.job_title = job_title  # This may throw an exception if validation fails

        # Prompt for and update the employee's department ID
        department_id = input("Enter the employee's new department ID: ")
        department_id = int(department_id)  # Ensure the department_id is an integer

        # Check if the department ID exists in the database
        department = Department.find_by_id(department_id)
        if not department:
            print(f"Error: Department ID {department_id} does not exist.")
            return

        employee.department_id = department_id  # This may throw an exception if validation fails

        # Update the employee in the database
        employee.update()
        print(f'Success: Employee {id_} updated.')

    except ValueError:
        print("Error: Department ID must be a number.")
    except Exception as exc:
        print(f"Error updating employee: {exc}")


def delete_employee():
    id_ = input("Enter the employee's id: ")
    if employee := Employee.find_by_id(id_):
        employee.delete()
        print(f'Employee{id_} deleted')
    else:
        print(f'Employee {id_} not found')


def list_department_employees():
    department_id = input("Enter the department id: ")
    department = Department.find_by_id(department_id)

    if department:
        employees = department.employees()  # Assuming Department has an instance method `employees`
        
        if employees:
            print(f"Employees in {department.name} department:")
            for employee in employees:
                print(f"- {employee.name} (Job Title: {employee.job_title}, ID: {employee.id})")
        else:
            print(f"No employees found in {department.name} department.")
    else:
        print(f"Department with id {department_id} not found.")
