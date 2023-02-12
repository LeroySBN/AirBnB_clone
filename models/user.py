#!/usr/bin/env python3
"""
defines a User class
"""


class User(BaseModel):
    """creates a user instance"""
    email = ""
    password = ""
    first_name = ""
    last_name = ""

    def __init__(self, *args, **kwargs):
        """initializes user instance"""
        super().__init__(*args, **kwargs)
