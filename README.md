# Django-Todo-App

The Todo app is a simple application that allows users to manage their tasks. It provides features such as user
registration, user authentication, creating todos, adding comments to todos, and API endpoints for managing todos and
comments.

## Project Overview

The Todo app provides the following features:

- User registration, authentication and logout.
- Creating, updating, and deleting todos.
- Adding comments to todos.
- API endpoints for managing todos and comments.
- Templates for a simple UI and Routes.
- Reset password by smtp Email.

## Implementation Cycle

The implementation of the Todo app can follow the following cycle:

1. Define Models:
    - Create models for `Todo` and `Comment` with the necessary fields and relationships.

2. Create Serializers:
    - Implement serializers for `Todo` and `Comment` models to convert data to and from JSON format.

3. Define Views:
    - Create views for CRUD operations on todos and comments, using Django's generic class-based views or custom views.

4. Configure URLs:
    - Define URL patterns in the app's `urls.py` file to map the views to specific endpoints.

5. Implement User Authentication:
    - Use Django's built-in authentication views or authentication libraries such as `rest_framework_simplejwt` to
      handle user registration and login.

6. Create Templates:
    - Build HTML templates to provide user interfaces for registration, login, todo list, and todo details pages.

7. Integrate Frontend and Backend:
    - Connect the frontend templates with the backend views using appropriate URLs and form actions.

8. Test the Application:
    - Test the functionality of the Todo app by creating, updating, and deleting todos, and adding comments.

9. Document the APIs and Routes:
    - Update the README.md file with detailed information about the APIs, routes, and their functionality.

10. Deployment:
    - Deploy the Todo app to a production environment, following best practices for security and performance.

## Running the Project

To run the Todo app locally, follow these steps:

running with docker:

- cd todo-app
- docker build -t todo-app .
- docker run -p 8000:8000 todo-app

or run with virtualenv:

1. Navigate to the project directory:
    - cd todo-app

2. Create and activate a virtual environment (optional but recommended):
    - python3 -m venv env
    - source env/bin/activate

3. Install the project dependencies:
    - pip install -r requirements.txt
4. Apply the database migrations:
    - python manage.py migrate
5. Start the development server:
    - python manage.py runserver
6. Access the Todo app in your web browser at http://localhost:8000/.

## Project Flow

1. User Registration:
    - Endpoint: `/accounts/api/register/`
    - Method: `POST`
    - Creates a new user account.

2. User Login:
    - Endpoint: `/accounts/api/login/`
    - Method: `POST`
    - Authenticates the user and provides an authentication token.

3. Todo List:
    - Endpoint: `/api/todos/`
    - Method: `GET`
    - Retrieves a list of all todos.

4. Create Todo:
    - Endpoint: `/api/todos/`
    - Method: `POST`
    - Creates a new todo.

5. Retrieve Todo:
    - Endpoint: `/api/todos/<todo_id>/`
    - Method: `GET`
    - Retrieves details of a specific todo.

6. Update Todo:
    - Endpoint: `/api/todos/<todo_id>/`
    - Method: `PUT`
    - Updates a specific todo.

7. Delete Todo:
    - Endpoint: `/api/todos/<todo_id>/`
    - Method: `DELETE`
    - Deletes a specific todo.

8. Create Comment:
    - Endpoint: `/api/comments/`
    - Method: `POST`
    - Creates a new comment for a todo.

9. Template Route: Home Page
    - Route: `/`
    - Displays the home page with a list of todos.

10. Template Route: Todo Detail Page
    - Route: `/todos/<todo_id>/`
    - Displays the details of a specific todo with its comments.

11. Template Route: User Registration Page
    - Route: `/accounts/register/`
    - Displays the user registration form.

12. Template Route: User Login Page
    - Route: `/accounts/login/`
    - Displays the user login form.

## API Routes

- User Registration API:
    - `/accounts/api/register/`

- User Login API:
    - `/accounts/api/login/`

- Todo List API:
    - `/api/todos/`

- Create Todo API:
    - `/api/todos/`

- Retrieve Todo API:
    - `/api/todos/<todo_id>/`

- Update Todo API:
    - `/api/todos/<todo_id>/`

- Delete Todo API:
    - `/api/todos/<todo_id>/`

- Create Comment API:
    - `/api/comments/`

## Template Routes

- Home Page:
    - `/`

- Todo Detail Page -id:
    - `/todos/<todo_id>/`

- Todo Detail Page -slug:
    - `/todos/<slug:slug>/`

- Todo Update Page:
    - `/todos/update/<todo_id>/`

- Todo Delete Page:
    - `/todos/delete/<todo_id>/`

- User Registration Page:
    - `/accounts/register/`

- User Login Page:
    - `/accounts/login/`

- User Logout Page:
    - `/accounts/logout/`

- User rest password Page:
    - `/accounts/rest-password/`

- User rest confirm Page:
    - `/accounts/reset-confirm/`

- User rest complete Page:
    - `/accounts/reset-complete/`

## Contact

- For any inquiries or questions, please reach out to:
    - mohammadahmadidezhnet@gmail.com
    - +989358270867