import os
from os.path import join, dirname
from dotenv import load_dotenv  # install dotenv for python

dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)

print(os.environ.get("name"))
