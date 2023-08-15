#!/usr/bin/env python3
""" python function that changes all topics of a school document """


def schools_by_topic(mongo_collection, topic):
    """ it returns the list of school and topic """
    return mongo_collection.find({"topics": topic})