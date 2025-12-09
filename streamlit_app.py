"""
Top-level Streamlit entrypoint for Streamlit Cloud.
This runs the app in `src/app.py` by adding src to sys.path.
"""

import os
import sys

# Add src directory to Python path so imports work
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'src'))

# Now import and run the app
import app  # noqa: F401 (module executes on import)
