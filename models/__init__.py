#!/usr/bin/python3
"""
Module: models

Intialize files and load saved objects
"""

from models.engine.file_storage import FileStorage


storage = FileStorage()
storage.reload()
