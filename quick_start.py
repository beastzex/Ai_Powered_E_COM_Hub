import subprocess
import sys
import os

print("=" * 50)
print("E-Commerce AI Assistant - Quick Start")
print("=" * 50)

# Generate data if missing
if not os.path.exists("data/data.json"):
    print("Generating data...")
    subprocess.run([sys.executable, "generate_mock_data.py"])

print("\nStarting AI Backend...")
print("Once started:")
print("1. Open index2.html in your browser")
print("2. Click on 'AI Assistant' tab")
print("3. Try the quick buttons or type questions")
print("\nPress Ctrl+C to stop")
print("=" * 50)

subprocess.run([sys.executable, "simple_backend.py"])