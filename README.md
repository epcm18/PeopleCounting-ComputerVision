
# Real-Time People Counting System with YOLOv8 and OpenCV


![People Counting](https://github.com/epcm18/PeopleCounting-ComputerVision/assets/104779449/9b33bba6-c9ce-4144-b90d-3e294a655b96)

This repository contains the code for a real-time people-counting system using YOLOv8 and OpenCV. The system utilizes YOLOv8, a state-of-the-art object detection algorithm, to detect people in images and videos. Additionally, it includes a custom class that can be used for detecting people without relying on YOLOv8.

## Table of Contents

- [Introduction](#introduction)
- [Installation](#installation)
- [Usage](#usage)
- [Custom People Detection](#custom-people-detection)
- [Contributing](#contributing)
- [License](#license)

## Introduction

The real-time people-counting system is designed to detect and count the number of people present in images or live video streams. YOLOv8, which stands for "You Only Look Once version 8," is a deep learning-based object detection model that can recognize multiple objects in an image simultaneously. This system utilizes YOLOv8 as the core object detection algorithm and integrates it with OpenCV to achieve real-time detection.

## Installation

To use the real-time people counting system, follow these steps to set up the environment:

1. Clone this GitHub repository to your local machine:

   \`git clone https://github.com/epcm18/PeopleCounting-ComputerVision.git\`
   \`cd PeopleCounting-ComputerVisiony\`

2. Install the required dependencies. It is recommended to create a virtual environment before installing the dependencies:

   \`python -m venv venv\`
   \`source venv/bin/activate\`  # On Windows, use \`venv\Scripts\activate\`

   Install dependencies:

   \`pip install -r requirements.txt\`

## Usage

This we can use to detect people in a camera frame and also get a count of people who are present on the screen now.

### Running the People Counting System

To run the real-time people counting system using YOLOv8 and OpenCV, execute the following command:

\`python countingYolov8.py\`

This will start the application, and it will use your webcam by default to capture live video and count the number of people in the frames. The processed video with bounding boxes around detected people and the count will be displayed in real-time.

### Keyboard Shortcuts

- **'Esc'**: Quit the application.

## Custom People Detection

Apart from using YOLOv8, this repository also includes a custom class for detecting people. The custom people detection class can be found in \`custom_people_detection.py\`.

To use the custom people detection class, follow these steps:

1. Import the class in your script:

   \`from Person import Myperson\`

2. Create an instance of the \`Myperson\` class:

   \`people_detector = Myperson()\`
   
4. To detect multiple people going with each other import \`ManyPeople`\ class

## Contributing

Contributions to this real-time people counting system are welcome. If you have any ideas, bug fixes, or improvements, please open an issue or submit a pull request.

When contributing to this repository, please first discuss the changes you wish to make by opening an issue. 



