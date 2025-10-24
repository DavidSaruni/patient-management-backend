# Patient Management API Documentation

## Overview
This is a Django REST API for managing patient data, vitals, and visit forms. The API provides full CRUD operations for all entities.

## Base URL
```
http://localhost:8000/api/
```

## Authentication
Currently, no authentication is required (development mode).

## Endpoints

### 1. Patients
Base endpoint: `/api/patients/`

#### GET /api/patients/
- **Description**: List all patients with pagination
- **Response**: Paginated list of patients
- **Example Response**:
```json
{
  "count": 17,
  "next": "http://localhost:8000/api/patients/?page=2",
  "previous": null,
  "results": [
    {
      "id": 1,
      "patient_id": "P001",
      "registration_date": "2025-10-24",
      "first_name": "John",
      "last_name": "Doe",
      "date_of_birth": "1990-05-15",
      "gender": "Male"
    }
  ]
}
```

#### POST /api/patients/
- **Description**: Create a new patient
- **Request Body**:
```json
{
  "patient_id": "P001",
  "first_name": "John",
  "last_name": "Doe",
  "date_of_birth": "1990-05-15",
  "gender": "Male"
}
```
- **Response**: Created patient object

#### GET /api/patients/{id}/
- **Description**: Get a specific patient by ID
- **Response**: Patient object

#### PUT /api/patients/{id}/
- **Description**: Update a specific patient
- **Request Body**: Same as POST
- **Response**: Updated patient object

#### DELETE /api/patients/{id}/
- **Description**: Delete a specific patient
- **Response**: 204 No Content

### 2. Vitals
Base endpoint: `/api/vitals/`

#### GET /api/vitals/
- **Description**: List all vitals records with pagination
- **Response**: Paginated list of vitals

#### POST /api/vitals/
- **Description**: Create a new vitals record
- **Request Body**:
```json
{
  "patient": 1,
  "height_cm": 175.0,
  "weight_kg": 70.0
}
```
- **Note**: BMI is automatically calculated and cannot be set manually
- **Response**: Created vitals object with calculated BMI

#### GET /api/vitals/{id}/
- **Description**: Get a specific vitals record
- **Response**: Vitals object

#### PUT /api/vitals/{id}/
- **Description**: Update a specific vitals record
- **Note**: BMI is automatically recalculated on update

#### DELETE /api/vitals/{id}/
- **Description**: Delete a specific vitals record

### 3. Visit Form A
Base endpoint: `/api/visit_form_a/`

#### GET /api/visit_form_a/
- **Description**: List all Visit Form A records

#### POST /api/visit_form_a/
- **Description**: Create a new Visit Form A record
- **Request Body**:
```json
{
  "patient": 1,
  "general_health": "Good",
  "ever_been_on_diet": true,
  "comments": "Patient has been on a diet before"
}
```

#### GET /api/visit_form_a/{id}/
- **Description**: Get a specific Visit Form A record

#### PUT /api/visit_form_a/{id}/
- **Description**: Update a specific Visit Form A record

#### DELETE /api/visit_form_a/{id}/
- **Description**: Delete a specific Visit Form A record

### 4. Visit Form B
Base endpoint: `/api/visit_form_b/`

#### GET /api/visit_form_b/
- **Description**: List all Visit Form B records

#### POST /api/visit_form_b/
- **Description**: Create a new Visit Form B record
- **Request Body**:
```json
{
  "patient": 1,
  "general_health": "Good",
  "currently_using_drugs": false,
  "comments": "Patient is not currently using any drugs"
}
```

#### GET /api/visit_form_b/{id}/
- **Description**: Get a specific Visit Form B record

#### PUT /api/visit_form_b/{id}/
- **Description**: Update a specific Visit Form B record

#### DELETE /api/visit_form_b/{id}/
- **Description**: Delete a specific Visit Form B record

## Data Models

### Patient
- `id`: Auto-generated primary key
- `patient_id`: Unique string identifier (max 50 chars)
- `registration_date`: Date field (auto-set to current date)
- `first_name`: String (max 100 chars)
- `last_name`: String (max 100 chars)
- `date_of_birth`: Date field
- `gender`: Choice field (Male, Female, Other)

### Vitals
- `id`: Auto-generated primary key
- `patient`: Foreign key to Patient
- `visit_date`: Date field (auto-set to current date)
- `height_cm`: Float field
- `weight_kg`: Float field
- `bmi`: Float field (auto-calculated, read-only)

### VisitFormA
- `id`: Auto-generated primary key
- `patient`: Foreign key to Patient
- `visit_date`: Date field (auto-set to current date)
- `general_health`: Choice field (Good, Poor)
- `ever_been_on_diet`: Boolean field
- `comments`: Text field (optional)

### VisitFormB
- `id`: Auto-generated primary key
- `patient`: Foreign key to Patient
- `visit_date`: Date field (auto-set to current date)
- `general_health`: Choice field (Good, Poor)
- `currently_using_drugs`: Boolean field
- `comments`: Text field (optional)

## Pagination
All list endpoints support pagination with a page size of 10 items.

## Error Handling
- **400 Bad Request**: Invalid data or validation errors
- **404 Not Found**: Resource not found
- **500 Internal Server Error**: Server error

## Testing
Run the comprehensive test script:
```bash
python final_test.py
```

## Server Status
The Django development server is running on `http://localhost:8000`

## Database
- **Engine**: PostgreSQL
- **Database**: patient_db
- **Host**: localhost:5432
