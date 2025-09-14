"""
Replacement for gemini_test.py using OpenAI API
"""
from openai_assistant import OpenAIAssistant
import os

def test_openai_assistant():
    """Test the OpenAI assistant functionality"""
    try:
        # Initialize assistant
        assistant = OpenAIAssistant()
        
        # Test basic query
        response = assistant.generate_response("What is 2 + 2?")
        print(f"Response: {response}")
        
        # Test query classification
        classification = assistant.classify_query("Show me the financial reports")
        print(f"Classification: {classification}")
        
    except ValueError as e:
        print(f"Configuration error: {e}")
        print("Please set OPENAI_API_KEY environment variable")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    test_openai_assistant()