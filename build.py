# build.py

import PyInstaller.__main__
import os
import sys

# Define the main script to be packaged
MAIN_SCRIPT = "main_gui.py"

# Define the output directory for the executable
OUTPUT_DIR = "dist"

# Define the name for the executable
APP_NAME = "RS232Tester"

def build_executable():
    """Builds the executable using PyInstaller."""
    if not os.path.exists(MAIN_SCRIPT):
        print(f"Error: Main script '{MAIN_SCRIPT}' not found.")
        sys.exit(1)

    # PyInstaller command-line arguments
    # --onefile: Package into a single executable file
    # --windowed: Do not show a console window when the application runs
    # --name: Name of the executable
    # --distpath: Directory to put the bundled app
    # --workpath: Directory to put temporary work files
    # --clean: Clean PyInstaller cache and remove temporary files before building
    pyinstaller_args = [
        '--onefile',
        '--windowed',
        f'--name={APP_NAME}',
        f'--distpath={OUTPUT_DIR}',
        f'--workpath=build',
        '--clean',
        MAIN_SCRIPT
    ]

    print(f"Running PyInstaller with arguments: {pyinstaller_args}")
    try:
        PyInstaller.__main__.run(pyinstaller_args)
        print(f"Executable successfully built and placed in '{OUTPUT_DIR}/{APP_NAME}.exe'!")
    except Exception as e:
        print(f"An error occurred during PyInstaller build: {e}")
        sys.exit(1)

if __name__ == "__main__":
    # Before building, ensure the necessary Python files are in the same directory
    # or adjust paths accordingly if they are in subdirectories.
    # For this example, we assume serial_handler.py and challenge_response_logic.py
    # are in the same directory as build.py and main_gui.py.

    # You might want to add checks here to ensure other required files exist.

    build_executable()
