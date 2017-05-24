"""Script to run conversion from ipynb to html."""

import os

from subprocess import run

print("Converting all ipynb files in notebooks/ to html.")
print("cwd:", os.getcwd())

run(["python", "-m", "nbconvert", "notebooks/hello_world.ipynb", "--template=resources/my_templates/intro_python_base.tpl",
        "--FilesWriter.build_directory='html_site'"])

