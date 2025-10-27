# Backend API
<img width="1366" height="768" alt="image" src="https://github.com/user-attachments/assets/eb36decb-0018-4005-99ec-1a9a555ccea1" />

## Patient Registration
<img width="1366" height="768" alt="image" src="https://github.com/user-attachments/assets/8c0fd6e8-306a-46d2-b137-2e8789233fbf" />

## Vitals
<img width="1366" height="768" alt="image" src="https://github.com/user-attachments/assets/b9a98ae9-6261-44f1-8776-899f71debc16" />

## Visit Forms A & B
<img width="1366" height="768" alt="image" src="https://github.com/user-attachments/assets/4bffde0c-bcd5-4daf-a6ce-dfc7cdb7dcb0" />
<img width="1366" height="768" alt="image" src="https://github.com/user-attachments/assets/6245ea37-1217-4e3f-a8db-d6a64a86adc9" />

# Patient Management Backend API

A Django REST API for managing patient data, vitals, and visit forms with automatic BMI calculation.

## 🏥 Features

- **Patient Management**: Full CRUD operations for patient records
- **Vitals Tracking**: Height, weight, and automatic BMI calculation
- **Visit Forms**: Two different visit forms (A & B) for patient assessments
- **RESTful API**: Clean, browsable API interface
- **Pagination**: Built-in pagination for large datasets
- **Data Validation**: Comprehensive input validation and error handling

## 📋 API Endpoints

| Endpoint | Method | Description |
|----------|--------|-------------|
| `/api/patients/` | GET, POST | List/Create patients |
| `/api/patients/{id}/` | GET, PUT, DELETE | Retrieve/Update/Delete specific patient |
| `/api/vitals/` | GET, POST | List/Create vitals records |
| `/api/vitals/{id}/` | GET, PUT, DELETE | Retrieve/Update/Delete specific vitals |
| `/api/visit_form_a/` | GET, POST | List/Create Visit Form A records |
| `/api/visit_form_a/{id}/` | GET, PUT, DELETE | Retrieve/Update/Delete specific Form A |
| `/api/visit_form_b/` | GET, POST | List/Create Visit Form B records |
| `/api/visit_form_b/{id}/` | GET, PUT, DELETE | Retrieve/Update/Delete specific Form B |

## 🚀 Quick Start

### Prerequisites

- Python 3.8+
- PostgreSQL
- pip (Python package manager)

### 1. Clone and Setup

```bash
# Clone the repository
git clone https://github.com/DavidSaruni/patient-management-backend.git
cd patient_management_backend

# Create virtual environment
python -m venv venv

# Activate virtual environment on Linux:
source venv/bin/activate

# On Windows:
venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt
```

### 2. Database Setup

```bash
# Create PostgreSQL database
sudo -u postgres createdb patient_db

# Or using psql
sudo -u postgres psql -c "CREATE DATABASE patient_db;"
```

### 3. Configure Settings

Update `core/settings.py` if needed:

```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'patient_db',
        'USER': 'postgres',
        'PASSWORD': 'your_password',  # Update this
        'HOST': 'localhost',
        'PORT': '5432',
    }
}

# For development - allow all hosts
ALLOWED_HOSTS = ['*']
```

### 4. Run Migrations

```bash
# Apply database migrations
python manage.py makemigrations
python manage.py migrate
```

### 5. Start the Server

```bash
# Start development server
python manage.py runserver 0.0.0.0:8000
```

The API will be available at:
- **Local**: http://localhost:8000/api/
- **Network**: http://[your-ip]:8000/api/

## 📖 Usage Examples

### Create a Patient

```bash
curl -X POST http://localhost:8000/api/patients/ \
  -H "Content-Type: application/json" \
  -d '{
    "patient_id": "P031",
    "first_name": "John",
    "last_name": "Doe",
    "date_of_birth": "1990-05-15",
    "gender": "Male"
  }'
```

### Add Vitals (BMI auto-calculated)

```bash
curl -X POST http://localhost:8000/api/vitals/ \
  -H "Content-Type: application/json" \
  -d '{
    "patient": P031,
    "height_cm": 175.0,
    "weight_kg": 70.0
  }'
```

### Create Visit Form A

```bash
curl -X POST http://localhost:8000/api/visit_form_a/ \
  -H "Content-Type: application/json" \
  -d '{
    "patient": P031,
    "general_health": "Good",
    "ever_been_on_diet": true,
    "comments": "Patient has been on a diet before"
  }'
```

## 🧪 Testing

### Run Automated Tests

```bash
# Run the comprehensive test suite
python final_test.py
```

### Production Settings

For production deployment:

```python
# core/settings.py
DEBUG = False
ALLOWED_HOSTS = ['your-domain.com', 'www.your-domain.com']
SECRET_KEY = 'your-production-secret-key'
```

## 📱 Android App Connection

The API is configured to accept requests from any IP address in development mode. To connect the Android app:

Ensure both PC and phone are on the same Wi-Fi network.

Find your local IP:
1. Find your IP address:
   ```bash
   hostname -I
   
   192.168.xxx.xxx```
2. Update the API base URL in the Android project in the file `ApiClient` :
   <img width="960" height="59" alt="image" src="https://github.com/user-attachments/assets/b779179c-7853-4d41-a34b-4da6268cbcf2" />

   ```const val BASE_URL = "http://192.168.xxx.xxx:8000/"```

4. Run the Django server again with:
   ```bash
   python manage.py runserver 0.0.0.0:8000
   This makes it accessible to other devices on the same network.
   





