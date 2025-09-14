#!/usr/bin/env python3
"""
Test script to verify backend functionality
"""

import requests
import json
import time
import subprocess
import sys
from threading import Thread

def start_backend():
    """Start the backend server"""
    try:
        subprocess.run([sys.executable, "Backend_api1.py"], check=True)
    except KeyboardInterrupt:
        pass

def test_endpoints():
    """Test various API endpoints"""
    base_url = "http://127.0.0.1:5000"
    
    # Wait for server to start
    time.sleep(3)
    
    print("Testing API endpoints...")
    
    # Test basic endpoints
    endpoints = [
        "/customers",
        "/inventory", 
        "/financials",
        "/competitors",
        "/purchases"
    ]
    
    for endpoint in endpoints:
        try:
            response = requests.get(f"{base_url}{endpoint}", timeout=5)
            print(f"✓ {endpoint}: {response.status_code}")
        except Exception as e:
            print(f"✗ {endpoint}: {e}")
    
    # Test AI query endpoint
    try:
        ai_query = {
            "query": "What are our current financials?"
        }
        response = requests.post(f"{base_url}/ai/query", 
                               json=ai_query, 
                               timeout=10)
        print(f"✓ /ai/query: {response.status_code}")
        if response.status_code == 200:
            result = response.json()
            print(f"  Response type: {type(result.get('response'))}")
    except Exception as e:
        print(f"✗ /ai/query: {e}")

if __name__ == "__main__":
    print("Starting backend test...")
    
    # Start backend in a separate thread
    backend_thread = Thread(target=start_backend, daemon=True)
    backend_thread.start()
    
    # Test endpoints
    test_endpoints()
    
    print("Test completed. Press Ctrl+C to stop backend.")