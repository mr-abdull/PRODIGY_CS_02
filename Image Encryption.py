import cv2
import numpy as np

def encrypt_image(image_path, key=None):
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

# Example usage for encryption
image_path = r"C:\OS\image.png"
key = encrypt_image(image_path)
print("Image encrypted successfully.")
