#!/usr/bin/env python3
"""
Demo startup script - works without OpenAI API key
"""

import os
import sys
import subprocess

def main():
    print("=" * 50)
    print("E-Commerce Assistant Demo")
    print("=" * 50)
    
    # Check if data files exist
    if not os.path.exists("data/data.json"):
        print("Generating mock data...")
        subprocess.run([sys.executable, "generate_mock_data.py"])
    
    if not os.path.exists("data/competitor_data.json"):
        print("Generating competitor data...")
        subprocess.run([sys.executable, "web_scraper.py"])
    
    print("\nStarting backend server...")
    print("The AI chatbot will work with fallback responses (no OpenAI API key required)")
    print("\nOnce started:")
    print("1. Open index2.html in your browser")
    print("2. Try the AI Assistant tab")
    print("3. Use quick query buttons or type your own questions")
    print("\nPress Ctrl+C to stop the server")
    print("=" * 50)
    
    try:
        subprocess.run([sys.executable, "Backend_api1.py"])
    except KeyboardInterrupt:
        print("\nServer stopped.")

if __name__ == "__main__":
    main()