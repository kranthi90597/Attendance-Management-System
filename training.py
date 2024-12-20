import cv2
import os
import numpy as np
from PIL import Image

# Create a face recognizer object
recognizer = cv2.face.LBPHFaceRecognizer_create()

# Create a detector object for frontal face detection
detector = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

def getImagesAndLabels(path):
    """
    Function to get the images and their corresponding IDs from a given path.

    Args:
        path (str): Path to the directory containing the images.

    Returns:
        tuple: A tuple containing two lists:
            - faceSamples: List of face images.
            - Ids: List of corresponding IDs for each face image.
    """

    # Get the path of all images in the folder
    imagePaths = [os.path.join(path, f) for f in os.listdir(path)]

    # Initialize empty lists for face samples and IDs
    faceSamples = []
    Ids = []

    # Loop through all image paths
    for imagePath in imagePaths:
        # Load the image and convert it to grayscale
        pilImage = Image.open(imagePath).convert('L')

        # Convert the PIL image to a NumPy array
        imageNp = np.array(pilImage, 'uint8') 1 

        # Extract the ID from the image path (assuming ID is the filename without extension)
        Id = int(os.path.split(imagePath)[-1].split(".")[0])

        # Detect faces in the image
        faces = detector.detectMultiScale(imageNp)

        # Loop through detected faces
        for (x, y, w, h) in faces:
            # Extract the face region from the image
            faceSample = imageNp[y:y+h, x:x+w]

            # Append the face sample and ID to the lists
            faceSamples.append(faceSample)
            Ids.append(Id)

    return faceSamples, Ids

# Example usage:
# Assuming you have a folder named 'dataset' containing images with filenames like 'person1.jpg', 'person2.png', etc.
faces, Ids = getImagesAndLabels('TrainingImage')

# Train the recognizer
recognizer.train(faces, np.array(Ids))

# Save the trained model
recognizer.save('TrainingImageLabel/trainner.yml')