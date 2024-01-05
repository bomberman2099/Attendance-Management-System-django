# Attendance App

The Attendance App is a web application developed using Django framework. It allows users to track their attendance and calculate job time for different tasks.

## Features

- User registration and login functionality
- Start and end attendance tracking
- Calculation of job time based on start and end times
- Display of attendance records for each user
- Edit and update attendance records

## Installation

1. Clone the repository:
```
 git clone https://github.com/bomberman2099/Attendance-Management-System-django.git
```

3. Install the required dependencies using pip:

```
pip install -r requirements.txt
```
4.Apply database migrations:

```
python manage.py migrate
```
5.Start the development server:

```
python manage.py runserver
```
6.Access the application in your browser at http://localhost:8000.

# Usage
Register a new user account or log in with an existing account.
Once logged in, click on "Start Attendance" to start tracking your attendance for a task.
Click on "End Attendance" when you finish the task to stop tracking.
View your attendance records and calculated job time in the "Attendance List" section.
Edit or update your attendance records if needed.
Log out when you are done.
Contributing
Contributions to the Attendance App are welcome! If you find any issues or have suggestions for improvements, please open an issue or submit a pull request.


# Acknowledgements
This project was inspired by the need to track attendance and calculate job time accurately.
The Django framework was used to develop the web application.
