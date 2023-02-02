
import re

def chatbot(message):
  # Check for a greeting
  if re.search(r'hi|hello|hey|hola|greetings', message):
    return "Hello there!"

  # Check for a farewell
  elif re.search(r'bye|goodbye|adios|later', message):
    return "Goodbye!"

  # Check for a question
  elif re.search(r'how are you|how are you doing|how is it going', message):
    return "I'm doing well, thank you. How are you?"
  
  # Check for a request for information
  elif re.search(r'tell me about|what is|who is|define', message):
    words = message.split()
    if 'tell' in words and 'about' in words:
      topic_index = words.index('about') + 1
      return f"I'm sorry, I don't know much about {words[topic_index]}."
    else:
      return "I'm sorry, I didn't understand your request for information."

  # Default response
  else:
    return "I'm sorry, I didn't understand your message."

# Test the chatbot
print(chatbot('Hello!'))
print(chatbot('What is your name?'))
print(chatbot('Tell me about virtual private networks'))
print(chatbot('Goodbye!'))
print(chatbot('I dont understand what you are saying.'))
