# Employee System

A simple Django-based Employee System with user authentication (login, registration, password reset).

## Dependencies

- python-dotenv

Install dependencies with:

pip install django python-dotenv


## Setup Instructions:

1. Clone the repository

   git clone repo-url
   cd mini_project-1/employee_system

2. Create and activate a virtual environment

   python -m venv env
   env\Scripts\activate

3. Install dependencies

   pip install django python-dotenv

4. Apply migrations

   python manage.py migrate

5. Create a superuser

   python manage.py createsuperuser

6. Run the development server

   python manage.py runserver
   
7. Open your browser and visit http://127.0.0.1:8000/

## Notes

- Configure email settings in `settings.py` for password reset functionality.
- Static files and templates are located in the `employee_system/static` and `employee_system/templates` directories.

Screenshots

Home Page
![Home Page](employee_system/employee_system/home.png)

Login Page
![Login Page](employee_system/employee_system/login.png)

Password Reset Page
![Password Reset Page](employee_system/employee_system/password%20reset.png)

Register Page
![Register Page](employee_system/employee_system/register.png) 



## sample user and password

username: testuser (my super user)
password: 7722

username: poshnova1
password: luxshtech@2025

username: pratik77
password: luxsh@2025