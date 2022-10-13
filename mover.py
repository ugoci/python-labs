# Write a script that moves all files with the .png extension
# from one folder to another

# Import pathlib

# Find the path to my Desktop

# Create a new folder

# Filter for screenshots only

# Create a new path for each file

# Move the screenshot there
import pathlib

my_desktop = pathlib.Path("C:/Users/Ugo/Desktop")
new_path = pathlib.Path("/Users/Ugo/Desktop/Test Folder")

for filepath in my_desktop.iterdir():
    
    if filepath.suffix == ".docx":
        new_filepath = new_path.joinpath(filepath.name)
        filepath.replace(new_filepath)

        




