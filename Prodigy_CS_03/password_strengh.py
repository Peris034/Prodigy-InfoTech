#Developed by Peris-Gajera
def password_strength(password):
  """
  Evaluates the strength of a password based on complexity criteria.

  Args:
      password: The password to be assessed.

  Returns:
      A tuple containing:
          - Strength score (integer): Higher score indicates stronger password.
          - Feedback message (string): User-friendly message about password strength.
  """
  score = 0
  feedback = ""

  # Check password length
  if len(password) >= 12:
    score += 2
    feedback += "Great! The password length is good. "
  elif len(password) >= 8:
    score += 1
    feedback += "The password length is okay, but longer is better. "
  else:
    feedback += "Password is too short. Use at least 8 characters. "

  # Check for uppercase letters
  if any(char.isupper() for char in password):
    score += 1
    feedback += "Using uppercase letters improves strength. "
  else:
    feedback += "Consider adding uppercase letters for better security. "

  # Check for lowercase letters
  if any(char.islower() for char in password):
    score += 1
    feedback += "Using lowercase letters improves strength. "
  else:
    feedback += "Consider adding lowercase letters for better security. "

  # Check for numbers
  if any(char.isdigit() for char in password):
    score += 1
    feedback += "Using numbers improves strength. "
  else:
    feedback += "Consider adding numbers for better security. "

  # Check for special characters
  if any(char in "!@#$%^&*()-_=+[]{};':\",./<>?|\\`~" for char in password):
    score += 1
    feedback += "Using special characters improves strength significantly. "
  else:
    feedback += "Consider adding special characters for maximum security. "

  # Translate score to strength level
  strength_level = "Very Weak"
  if score >= 5:
    strength_level = "Strong"
  elif score >= 4:
    strength_level = "Good"
  elif score >= 3:
    strength_level = "Moderate"

  return score, f"Password Strength: {strength_level}. {feedback}"

def main():
  """
  Prompts the user for a password and displays the strength assessment.
  """
  password = input("Enter your password: ")
  score, feedback = password_strength(password)
  print(feedback)

if __name__ == "__main__":
  main()
