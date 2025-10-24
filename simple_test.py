#!/usr/bin/env python3
"""
Simple API Test Script
"""

import requests
import json

BASE_URL = "http://localhost:8000/api"

def test_basic_connectivity():
    """Test basic API connectivity"""
    print("Testing basic connectivity...")
    
    try:
        # Test GET patients
        response = requests.get(f"{BASE_URL}/patients/")
        print(f"GET /patients/ - Status: {response.status_code}")
        if response.status_code == 200:
            print(f"Response: {response.json()}")
        else:
            print(f"Error response: {response.text}")
        
        # Test POST patient
        patient_data = {
            "patient_id": "P002",
            "first_name": "Jane",
            "last_name": "Smith",
            "date_of_birth": "1985-03-20",
            "gender": "Female"
        }
        
        response = requests.post(f"{BASE_URL}/patients/", json=patient_data)
        print(f"\nPOST /patients/ - Status: {response.status_code}")
        if response.status_code == 201:
            print(f"Response: {response.json()}")
        else:
            print(f"Error response: {response.text}")
            
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    test_basic_connectivity()
