#!/usr/bin/env python3
"""function that lists all documents in a collection"""
from pymongo import collection
from typing import List


def list_all(mongo_collection: collection) -> List:
    """lists all documents in a collection"""
    return list(mongo_collection.find())