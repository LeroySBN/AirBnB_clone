#!/usr/bin/env python3
"""
Defines a City class
"""

from models.base_model import BaseModel


class City(BaseModel):
    """Creates a city instance"""
    state_id = ""
    name = ""
