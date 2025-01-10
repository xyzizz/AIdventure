#!/usr/bin/env python
import os
import sys
import warnings

from .crew import AlgorithmProblemProcesser

warnings.filterwarnings("ignore", category=SyntaxWarning, module="pysbd")

# This main file is intended to be a way for you to run your
# crew locally, so refrain from adding unnecessary logic into this file.
# Replace with inputs you want to test with, it will automatically
# interpolate any tasks and agents information

image_path = "./src/alg/material/image.png"


def run():
    """
    Run the crew.
    """
    exists = os.path.exists(image_path)
    if not exists:
        print(f"Please provide an image at the path: {image_path}")
        sys.exit(1)

    AlgorithmProblemProcesser().crew().kickoff({"image_path": image_path})
