"""Compatibility entry point. The shared generator owns the profile design."""
import runpy
from pathlib import Path
runpy.run_path(str(Path(__file__).with_name('build_profile.py')), run_name='__main__')
