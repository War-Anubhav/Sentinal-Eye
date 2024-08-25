# config.py

import os

# Paths to your data and models
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
MODEL_DIR = os.path.join(BASE_DIR, 'models')
OUTPUT_DIR = os.path.join(BASE_DIR, 'output')

# File paths
FACE_RECOGNITION_MODEL_PATH = os.path.join(MODEL_DIR, 'deepface_model.h5')
OBJECT_DETECTION_MODEL_PATH = os.path.join(MODEL_DIR, 'yolov8n.onnx')
AUDIO_MODEL_PATH = os.path.join(MODEL_DIR, 'audio_model.pth')

# Thresholds and parameters
FACE_RECOGNITION_THRESHOLD = 0.6  # Confidence threshold for face recognition
HEAD_POSE_THRESHOLD = 15  # Maximum degrees deviation allowed for normal head pose
AUDIO_AMPLITUDE_THRESHOLD = 0.7  # Threshold for flagging high audio levels
CHEAT_PROBABILITY_THRESHOLD = 0.75  # Threshold for detecting suspicious behavior

# Frame processing settings
FRAME_RATE = 30  # Frames per second for video processing
BATCH_SIZE = 32  # Batch size for processing frames in batches

# Logging and Debugging
LOGGING_LEVEL = 'DEBUG'  # Can be 'DEBUG', 'INFO', 'WARNING', 'ERROR', 'CRITICAL'
LOG_FILE = os.path.join(BASE_DIR, 'app.log')

# Camera and video settings
CAMERA_INDEX = 0  # Default camera index
VIDEO_RESOLUTION = (640, 480)  # Resolution of the video feed

# Audio processing settings
AUDIO_SAMPLE_RATE = 16000  # Sample rate for audio processing
AUDIO_BUFFER_SIZE = 1024  # Buffer size for reading audio samples

# API and External services (if any)
API_KEY = 'your_api_key_here'  # Placeholder for API key if needed
API_URL = 'https://api.example.com/endpoint'  # Placeholder for external API endpoint

# Multi-model ensemble settings
USE_ENSEMBLE = True  # Whether to use an ensemble of models for face recognition
ENSEMBLE_MODELS = ['vgg_face', 'resnet50', 'facenet']  # List of models to use in ensemble

# Miscellaneous settings
SAVE_OUTPUT = True  # Whether to save processed output (e.g., flagged frames)
SHOW_VIDEO_FEED = True  # Whether to display video feed during processing
DEBUG_MODE = True  # Enable or disable debug mode

# Additional settings specific to your project can be added here...













#You can import this config.py file in your other scripts to access these configurations:

# from config import FACE_RECOGNITION_THRESHOLD, MODEL_DIR

# # Example usage
# print(f"The face recognition model is located at: {MODEL_DIR}")
# print(f"The current face recognition threshold is set to: {FACE_RECOGNITION_THRESHOLD}")
