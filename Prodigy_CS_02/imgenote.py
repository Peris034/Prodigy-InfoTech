from PIL import Image
import numpy as np

def encrypt_image(input_image_path, output_image_path, key):
    img = Image.open(input_image_path)
    img_array = np.array(img)
    
    # Adjust key generation based on the image mode
    if img.mode == 'RGBA':
        key = np.random.randint(0, 256, size=(img_array.shape[0], img_array.shape[1], 4), dtype=np.uint8)
    else:
        key = np.random.randint(0, 256, size=(img_array.shape[0], img_array.shape[1], 3), dtype=np.uint8)
    
    encrypted_array = np.bitwise_xor(img_array, key)
    encrypted_img = Image.fromarray(encrypted_array)

    # Convert to RGB if necessary before saving
    if encrypted_img.mode == 'RGBA':
        encrypted_img = encrypted_img.convert('RGB')

    encrypted_img.save(output_image_path)
    print("Image encrypted successfully.")
    return encrypted_array, key  # Return the key for decryption

def decrypt_image(encrypted_array, output_image_path, key):
    decrypted_array = np.bitwise_xor(encrypted_array, key)
    decrypted_img = Image.fromarray(decrypted_array)

    # Convert to RGB if necessary before saving
    if decrypted_img.mode == 'RGBA':
        decrypted_img = decrypted_img.convert('RGB')

    decrypted_img.save(output_image_path)
    print("Image decrypted successfully.")

if __name__ == "__main__":
    input_image_path = r"sample_input.jpg"  # Ensure this path is correct
    img = Image.open(input_image_path)
    
    width, height = img.size
    # No need to pre-generate key here; it is generated in encrypt_image based on image mode
    encrypted_image_path = 'encrypted_output.jpg'    
    encrypted_array, key = encrypt_image(input_image_path, encrypted_image_path, key=None)  # key=None, it will be generated
    
    decrypted_image_path = 'decrypted_output.jpg'
    decrypt_image(encrypted_array, decrypted_image_path, key)
