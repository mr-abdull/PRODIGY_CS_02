import cv2
import numpy as np

def encrypt_image(image_path, key):
    # Load the image
    img = cv2.imread(image_path)

    # Generate a random key if not provided
    if key is None:
        key = np.random.randint(0, 256, img.shape, dtype=np.uint8)

    # Perform encryption by XORing each pixel value with the key
    encrypted_img = cv2.bitwise_xor(img, key)

    # Save the encrypted image
    cv2.imwrite("encrypted_image.png", encrypted_img)

    return key

def decrypt_image(encrypted_image_path, key):
    # Load the encrypted image
    encrypted_img = cv2.imread(encrypted_image_path)

    # Perform decryption by XORing each pixel value with the key
    decrypted_img = cv2.bitwise_xor(encrypted_img, key)

    # Save the decrypted image
    cv2.imwrite("decrypted_image.png", decrypted_img)

# Example usage
image_path = "example.jpg"
key = encrypt_image(image_path, None)
decrypt_image("encrypted_image.png", key)
