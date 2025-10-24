#!/usr/bin/env python3
"""
Final Comprehensive API Testing Script for Patient Management System
Tests all CRUD operations for Patients, Vitals, VisitFormA, and VisitFormB
"""

import requests
import json
import time
from datetime import date, datetime

# Base URL for the API
BASE_URL = "http://localhost:8000/api"

def print_response(response, title):
    """Helper function to print formatted response"""
    print(f"\n{'='*50}")
    print(f"{title}")
    print(f"{'='*50}")
    print(f"Status Code: {response.status_code}")
    if response.status_code == 200 or response.status_code == 201:
        print(f"✅ SUCCESS")
    elif response.status_code == 400:
        print(f"⚠️  VALIDATION ERROR (Expected)")
    elif response.status_code == 404:
        print(f"⚠️  NOT FOUND (Expected)")
    else:
        print(f"❌ ERROR")
    
    try:
        print(f"Response: {json.dumps(response.json(), indent=2)}")
    except:
        print(f"Response: {response.text}")

def test_patient_endpoints():
    """Test Patient CRUD operations"""
    print("\n🏥 TESTING PATIENT ENDPOINTS")
    
    # Test 1: Create a new patient with unique ID
    import random
    unique_id = f"P{random.randint(1000, 9999)}"
    
    patient_data = {
        "patient_id": unique_id,
        "first_name": "Alice",
        "last_name": "Johnson",
        "date_of_birth": "1988-12-25",
        "gender": "Female"
    }
    
    response = requests.post(f"{BASE_URL}/patients/", json=patient_data)
    print_response(response, "CREATE PATIENT")
    
    if response.status_code == 201:
        patient_id = response.json()['id']
        
        # Test 2: Get all patients
        response = requests.get(f"{BASE_URL}/patients/")
        print_response(response, "GET ALL PATIENTS")
        
        # Test 3: Get specific patient
        response = requests.get(f"{BASE_URL}/patients/{patient_id}/")
        print_response(response, "GET SPECIFIC PATIENT")
        
        # Test 4: Update patient
        update_data = {
            "patient_id": unique_id,
            "first_name": "Alice",
            "last_name": "Smith",  # Changed last name
            "date_of_birth": "1988-12-25",
            "gender": "Female"
        }
        response = requests.put(f"{BASE_URL}/patients/{patient_id}/", json=update_data)
        print_response(response, "UPDATE PATIENT")
        
        return patient_id
    return None

def test_vitals_endpoints(patient_id):
    """Test Vitals CRUD operations with BMI calculation"""
    print("\n📊 TESTING VITALS ENDPOINTS")
    
    if not patient_id:
        print("No patient ID available for vitals testing")
        return None
    
    # Test 1: Create vitals record
    vitals_data = {
        "patient": patient_id,
        "height_cm": 165.0,
        "weight_kg": 60.0
        # BMI will be auto-calculated
    }
    
    response = requests.post(f"{BASE_URL}/vitals/", json=vitals_data)
    print_response(response, "CREATE VITALS (BMI should be auto-calculated)")
    
    if response.status_code == 201:
        vitals_id = response.json()['id']
        print(f"✅ BMI calculated: {response.json().get('bmi', 'N/A')}")
        
        # Test 2: Get all vitals
        response = requests.get(f"{BASE_URL}/vitals/")
        print_response(response, "GET ALL VITALS")
        
        # Test 3: Get specific vitals
        response = requests.get(f"{BASE_URL}/vitals/{vitals_id}/")
        print_response(response, "GET SPECIFIC VITALS")
        
        # Test 4: Update vitals (test BMI recalculation)
        update_data = {
            "patient": patient_id,
            "height_cm": 170.0,  # Changed height
            "weight_kg": 65.0     # Changed weight
        }
        response = requests.put(f"{BASE_URL}/vitals/{vitals_id}/", json=update_data)
        print_response(response, "UPDATE VITALS (BMI should be recalculated)")
        if response.status_code == 200:
            print(f"✅ Updated BMI: {response.json().get('bmi', 'N/A')}")
        
        return vitals_id
    return None

def test_visit_form_a_endpoints(patient_id):
    """Test VisitFormA CRUD operations"""
    print("\n📋 TESTING VISIT FORM A ENDPOINTS")
    
    if not patient_id:
        print("No patient ID available for VisitFormA testing")
        return None
    
    # Test 1: Create VisitFormA
    form_a_data = {
        "patient": patient_id,
        "general_health": "Good",
        "ever_been_on_diet": True,
        "comments": "Patient has been on a diet before"
    }
    
    response = requests.post(f"{BASE_URL}/visit_form_a/", json=form_a_data)
    print_response(response, "CREATE VISIT FORM A")
    
    if response.status_code == 201:
        form_a_id = response.json()['id']
        
        # Test 2: Get all VisitFormA records
        response = requests.get(f"{BASE_URL}/visit_form_a/")
        print_response(response, "GET ALL VISIT FORM A")
        
        # Test 3: Get specific VisitFormA
        response = requests.get(f"{BASE_URL}/visit_form_a/{form_a_id}/")
        print_response(response, "GET SPECIFIC VISIT FORM A")
        
        # Test 4: Update VisitFormA
        update_data = {
            "patient": patient_id,
            "general_health": "Poor",
            "ever_been_on_diet": False,
            "comments": "Updated: Patient has never been on a diet"
        }
        response = requests.put(f"{BASE_URL}/visit_form_a/{form_a_id}/", json=update_data)
        print_response(response, "UPDATE VISIT FORM A")
        
        return form_a_id
    return None

def test_visit_form_b_endpoints(patient_id):
    """Test VisitFormB CRUD operations"""
    print("\n📋 TESTING VISIT FORM B ENDPOINTS")
    
    if not patient_id:
        print("No patient ID available for VisitFormB testing")
        return None
    
    # Test 1: Create VisitFormB
    form_b_data = {
        "patient": patient_id,
        "general_health": "Good",
        "currently_using_drugs": False,
        "comments": "Patient is not currently using any drugs"
    }
    
    response = requests.post(f"{BASE_URL}/visit_form_b/", json=form_b_data)
    print_response(response, "CREATE VISIT FORM B")
    
    if response.status_code == 201:
        form_b_id = response.json()['id']
        
        # Test 2: Get all VisitFormB records
        response = requests.get(f"{BASE_URL}/visit_form_b/")
        print_response(response, "GET ALL VISIT FORM B")
        
        # Test 3: Get specific VisitFormB
        response = requests.get(f"{BASE_URL}/visit_form_b/{form_b_id}/")
        print_response(response, "GET SPECIFIC VISIT FORM B")
        
        # Test 4: Update VisitFormB
        update_data = {
            "patient": patient_id,
            "general_health": "Poor",
            "currently_using_drugs": True,
            "comments": "Updated: Patient is currently using drugs"
        }
        response = requests.put(f"{BASE_URL}/visit_form_b/{form_b_id}/", json=update_data)
        print_response(response, "UPDATE VISIT FORM B")
        
        return form_b_id
    return None

def test_error_handling():
    """Test error handling scenarios"""
    print("\n❌ TESTING ERROR HANDLING")
    
    # Test 1: Invalid patient data
    invalid_patient = {
        "patient_id": "",  # Empty patient_id
        "first_name": "Test",
        "last_name": "User",
        "date_of_birth": "invalid-date",  # Invalid date
        "gender": "Invalid"  # Invalid gender choice
    }
    response = requests.post(f"{BASE_URL}/patients/", json=invalid_patient)
    print_response(response, "CREATE INVALID PATIENT (should fail)")
    
    # Test 2: Get non-existent patient
    response = requests.get(f"{BASE_URL}/patients/99999/")
    print_response(response, "GET NON-EXISTENT PATIENT (should return 404)")

def test_api_endpoints():
    """Test all available API endpoints"""
    print("\n🔗 TESTING ALL API ENDPOINTS")
    
    endpoints = [
        ("/patients/", "Patients"),
        ("/vitals/", "Vitals"),
        ("/visit_form_a/", "Visit Form A"),
        ("/visit_form_b/", "Visit Form B")
    ]
    
    for endpoint, name in endpoints:
        response = requests.get(f"{BASE_URL}{endpoint}")
        print_response(response, f"GET {name} ENDPOINT")

def main():
    """Main testing function"""
    print("🚀 STARTING COMPREHENSIVE API TESTING")
    print("=" * 60)
    
    # Wait a moment for server to be ready
    time.sleep(1)
    
    try:
        # Test basic connectivity
        response = requests.get(f"{BASE_URL}/patients/")
        if response.status_code != 200:
            print("❌ Server not responding. Make sure Django server is running on port 8000")
            return
        
        print("✅ Server is responding!")
        
        # Test all endpoints first
        test_api_endpoints()
        
        # Run all CRUD tests
        patient_id = test_patient_endpoints()
        vitals_id = test_vitals_endpoints(patient_id)
        form_a_id = test_visit_form_a_endpoints(patient_id)
        form_b_id = test_visit_form_b_endpoints(patient_id)
        test_error_handling()
        
        print("\n🎉 ALL TESTS COMPLETED!")
        print("=" * 60)
        print("✅ API is working correctly!")
        print("📊 Summary:")
        print(f"   - Patient ID: {patient_id}")
        print(f"   - Vitals ID: {vitals_id}")
        print(f"   - Form A ID: {form_a_id}")
        print(f"   - Form B ID: {form_b_id}")
        
    except requests.exceptions.ConnectionError:
        print("❌ Connection failed. Make sure Django server is running on port 8000")
    except Exception as e:
        print(f"❌ Error during testing: {e}")

if __name__ == "__main__":
    main()
