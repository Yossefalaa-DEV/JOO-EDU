# JOO EDU - Educational Platform

An educational platform that allows students to access course materials using activation codes.

## Features

- Student registration and authentication
- Course browsing and activation
- Video content access with activation codes
- Admin dashboard for content and user management
- Code generation system (5 uses per code)

## Setup Instructions

### Backend Setup

1. Create a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Run migrations:
```bash
python manage.py migrate
```

4. Create superuser:
```bash
python manage.py createsuperuser
```

5. Run the development server:
```bash
python manage.py runserver
```

### Frontend Setup

1. Navigate to the frontend directory:
```bash
cd frontend
```

2. Install dependencies:
```bash
npm install
```

3. Start the development server:
```bash
npm start
```

## Environment Variables

Create a `.env` file in the root directory with the following variables:

```
SECRET_KEY=your_secret_key
DEBUG=True
ALLOWED_HOSTS=localhost,127.0.0.1
```

## Deployment

The application is configured for deployment on PythonAnywhere. 