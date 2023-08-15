#!/usr/bin/env python3
"""Python function that inserts new
document using the provided keyword arguments"""
from typing import Any
from pymongo import collection


def insert_school(mongo_collection: collection, **kwargs: Any) -> str:
    """inserts new
    document in a collection based on kwargs"""
    return mongo_collection.insert_one(kwargs).inserted_id