# Todo App with Flask and React

This is a simple Todo web application built using Flask (backend) and React (frontend). The app allows users to create, read, update, and delete (CRUD) tasks. The backend uses Flask-SQLAlchemy for database operations.

---

## Features
- Add new tasks
- Mark tasks as complete/incomplete
- Delete tasks
- Persistent data storage using SQLite

---

## Project Structure
```
backend/
├── app.py           # Main Flask application
├── models.py        # SQLAlchemy models
├── database.py      # SQLAlchemy instance
├── templates/       # HTML templates for the Flask app
│   └── index.html
frontend/            # React application (if applicable)
```

---

## Getting Started

### Prerequisites
Ensure you have the following installed:
- Python 3.7+
- Node.js (for the React frontend, if applicable)
- pip (Python package manager)

---

### Backend Setup

1. **Clone the repository:**
   ```bash
   git clone <repository-url>
   cd backend
   ```

2. **Install dependencies:**
   ```bash
   pip install flask flask-sqlalchemy
   ```

3. **Run the backend server:**
   ```bash
   python app.py
   ```

4. The Flask app will be available at:
   ```
   http://127.0.0.1:5000/
   ```

---

### Frontend Setup (Optional for React)
If you plan to use React for the frontend:

1. **Navigate to the `frontend/` directory:**
   ```bash
   cd frontend
   ```

2. **Install dependencies:**
   ```bash
   npm install
   ```

3. **Run the React development server:**
   ```bash
   npm start
   ```

4. The React app will be available at:
   ```
   http://localhost:3000/
   ```

---

## API Endpoints

### Base URL
```
http://127.0.0.1:5000/
```

### Routes
1. **Fetch all Todos**
   - `GET /todos`
   - **Response:**
     ```json
     [
       {
         "id": 1,
         "title": "Buy groceries",
         "completed": false
       }
     ]
     ```

2. **Add a new Todo**
   - `POST /todos`
   - **Request Body:**
     ```json
     {
       "title": "New Task"
     }
     ```

3. **Update a Todo**
   - `PUT /todos/<id>`
   - **Request Body:**
     ```json
     {
       "title": "Updated Task",
       "completed": true
     }
     ```

4. **Delete a Todo**
   - `DELETE /todos/<id>`

---

## Technologies Used
- **Backend:** Flask, Flask-SQLAlchemy
- **Frontend:** React (optional)
- **Database:** SQLite

---

## Future Enhancements
- Add user authentication
- Integrate a frontend framework (React or Vue.js)
- Deploy the app to a cloud platform like AWS, Heroku, or Vercel

---

## License
This project is licensed under the MIT License.

---

## Contribution
Feel free to contribute to this project by submitting a pull request or opening an issue!

# todo-app
# todo-app
