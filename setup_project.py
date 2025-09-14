#!/usr/bin/env python3
"""
Setup script for E-Commerce Assistant project
Initializes data and runs basic checks
"""

import os
import sys
import subprocess
import json
from pathlib import Path

def check_python_version():
    """Check if Python version is compatible"""
    if sys.version_info < (3, 8):
        print("Error: Python 3.8 or higher is required")
        return False
    print(f"Python {sys.version_info.major}.{sys.version_info.minor} detected - OK")
    return True

def install_requirements():
    """Install required packages"""
    try:
        print("Installing requirements...")
        subprocess.check_call([sys.executable, "-m", "pip", "install", "-r", "requirements.txt"])
        print("Requirements installed successfully")
        return True
    except subprocess.CalledProcessError as e:
        print(f"Error installing requirements: {e}")
        return False

def create_directories():
    """Create necessary directories"""
    directories = ["data", "zaphire_ledger", "logs"]
    for directory in directories:
        Path(directory).mkdir(exist_ok=True)
        print(f"Created directory: {directory}")

def generate_mock_data():
    """Generate mock data for testing"""
    try:
        print("Generating mock data...")
        import generate_mock_data
        print("Mock data generated successfully")
        return True
    except Exception as e:
        print(f"Error generating mock data: {e}")
        return False

def run_web_scraper():
    """Run web scraper to generate competitor data"""
    try:
        print("Running web scraper...")
        import web_scraper
        print("Competitor data generated successfully")
        return True
    except Exception as e:
        print(f"Error running web scraper: {e}")
        return False

def check_environment():
    """Check environment variables"""
    required_vars = ["OPENAI_API_KEY"]
    missing_vars = []
    
    for var in required_vars:
        if not os.environ.get(var):
            missing_vars.append(var)
    
    if missing_vars:
        print(f"Warning: Missing environment variables: {', '.join(missing_vars)}")
        print("Please set these variables or create a .env file")
        print("See .env.example for reference")
        return False
    else:
        print("All required environment variables are set")
        return True

def test_openai_connection():
    """Test OpenAI API connection"""
    try:
        from openai_assistant import OpenAIAssistant
        assistant = OpenAIAssistant()
        response = assistant.generate_response("test", max_tokens=5)
        print("OpenAI API connection successful")
        return True
    except Exception as e:
        print(f"OpenAI API test failed: {e}")
        print("The application will use fallback responses")
        return False

def main():
    """Main setup function"""
    print("Setting up E-Commerce Assistant Project...")
    print("=" * 50)
    
    success = True
    
    # Check Python version
    if not check_python_version():
        success = False
    
    # Create directories
    create_directories()
    
    # Install requirements
    if not install_requirements():
        success = False
    
    # Generate mock data
    if not generate_mock_data():
        success = False
    
    # Run web scraper
    if not run_web_scraper():
        success = False
    
    # Check environment
    env_ok = check_environment()
    
    # Test OpenAI (optional)
    if env_ok:
        test_openai_connection()
    
    print("=" * 50)
    if success:
        print("Setup completed successfully!")
        print("\nNext steps:")
        print("1. Set your OpenAI API key: set OPENAI_API_KEY=your-key-here")
        print("2. Run the application: python backend3.py")
        print("3. Or run the full API: python Backend_api1.py")
    else:
        print("Setup completed with some errors")
        print("Please check the error messages above and try again")
    
    return success

if __name__ == "__main__":
    main()