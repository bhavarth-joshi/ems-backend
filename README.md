## Employee Scheduler API

This project implements a backend API for managing employee schedules in a retail store chain. It allows for creating and managing employee information, defining shifts, and assigning shifts to employees based on availability and predicted customer traffic (to be implemented in the future).

### Functionalities

* **Employee Management:**
    * Create new employees with details like name, department, role, and availability.
    * Retrieve a list of all employees.
* **Shift Management:**
    * Create new shifts with start and end times, associated department, and required skills.
    * Retrieve a list of all shifts.
* **Shift Assignment (Planned):**
    * Assign shifts to employees considering their availability and skills (future implementation).
* **Employee Schedule Retrieval (Planned):**
    * View an employee's schedule for a specific period (future implementation).

### Technologies Used

* Python 3
* Django web framework
* Django REST Framework (DRF) for API development
* SQLite3 database (for development environment)

### Installation

1. **Prerequisites:** Ensure you have Python 3 and `pip` installed on your system.
2. **Clone the repository:** Clone this repository using `git clone https://github.com/bhavarth-joshi/ems-backend.git`.
3. **Create a virtual environment:**
   ```bash
   python3 -m venv venv
   source venv/bin/activate  # Activate the virtual environment (Windows: venv\Scripts\activate)
   ```
4. **Install dependencies:**
   ```bash
   pip install django djangorestframework
   ```
5. **Run database migrations:**
   ```bash
   python manage.py migrate
   ```

### Usage

1. **Start the development server:**
   ```bash
   python manage.py runserver
   ```
   This will start the Django development server, typically accessible at http://127.0.0.1:8000/ in your web browser.

2. **API Endpoints:**
    * **List all employees:** `GET /employees/`
    * **Create a new employee:** `POST /employees/` (data in JSON format)
    * **List all shifts:** `GET /shifts/`
    * **Create a new shift:** `POST /shifts/` (data in JSON format)

**Note:** Functionality for assigning shifts and retrieving employee schedules is planned for future development.

### Development Status

This is a work-in-progress project demonstrating core functionalities for employee and shift management. Future development will focus on:

* Implementing shift assignment considering availability and skills.
* Integrating predicted customer traffic for optimized scheduling.
* Adding functionalities for retrieving employee schedules based on assigned shifts.

### Contributing

Feel free to contribute to this project by creating pull requests with improvements, bug fixes, or additional features.
