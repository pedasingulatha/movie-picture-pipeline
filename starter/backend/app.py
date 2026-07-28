import os
import sys

from movies import app as application  # noqa: E402, F401

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

app = application
