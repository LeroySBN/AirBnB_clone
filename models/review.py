#!/usr/bin/python3
"""Defines a Review class"""
from models.base_model import BaseModel


class Review(BaseModel):
    """Creates a Review instance"""
    place_id = ""
    user_id = ""
    text = ""
