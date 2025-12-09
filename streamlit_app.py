"""
Top-level Streamlit entrypoint for Streamlit Cloud.
This imports and runs the app in `src/app.py` so the cloud can use a root file path.
"""

from src import app  # noqa: F401 (module executes on import)
