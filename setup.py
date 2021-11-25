from cx_Freeze import setup, Executable

# // Add files
files = ['tools/']

# // Target (.exe)
target = Executable(script="main.py")

# // Hide the terminal
base="Win32GUI"

# // Setup the cx-freeze application
setup(
    name = "Color Snipper",
    version = "1.0",
    description = "Easy way to get color codes from images",
    author = "tristan#2230",
    options = {'build_exe' : {'include_files' : files}},
    executables = [target]
)

# // go to this file directory in the terminal and type => python setup.py build
