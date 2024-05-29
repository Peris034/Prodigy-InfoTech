#Developed by Peris-Gajera
def caesar_cipher(text, shift, mode):
  """
  Encrypts or decrypts text using Caesar Cipher.

  Args:
      text: The text to encrypt or decrypt.
      shift: The number of positions to shift letters (positive for encryption, negative for decryption).
      mode: 'encrypt' or 'decrypt' to specify the operation.

  Returns:
      The encrypted or decrypted text.
  """
  alphabet = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
  shifted_alphabet = alphabet[shift:] + alphabet[:shift]
  result = ''

  for char in text:
    if char.isalpha():
      index = alphabet.find(char)
      new_char = shifted_alphabet[index]
    else:
      new_char = char  # Keep non-alphabetic characters the same

    result += new_char

  return result

def main():
  """
  Prompts the user for input, performs encryption/decryption, and displays the result.
  """
  while True:
    print("Caesar Cipher")
    print("1. Encrypt")
    print("2. Decrypt")
    print("3. Exit")
    choice = input("Enter your choice: ")

    if choice == '1':
      text = input("Enter the message to encrypt: ")
      shift = int(input("Enter the shift value (positive integer): "))
      encrypted_text = caesar_cipher(text, shift, 'encrypt')
      print("Encrypted message:", encrypted_text)

    elif choice == '2':
      text = input("Enter the message to decrypt: ")
      shift = int(input("Enter the shift value (positive integer): "))
      decrypted_text = caesar_cipher(text, -shift, 'decrypt')  # Use negative shift for decryption
      print("Decrypted message:", decrypted_text)

    elif choice == '3':
      print("Exiting...")
      break

    else:
      print("Invalid choice. Please try again.")

if __name__ == "__main__":
  main()
