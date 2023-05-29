#!/usr/bin/python3
"""Initial test"""
import os
storage_t = os.getenv("HBNB_TYPE_STORAGE")

if storage_t == "db":
    os.environ["HBNB_MYSQL_USER"] = "hbnb_test"
    os.environ["HBNB_MYSQL_PWD"] = "hbnb_test_pwd"
    os.environ["HBNB_MYSQL_HOST"] = "localhost"
    os.environ["HBNB_MYSQL_DB"] = "hbnb_test_db"
    os.environ["HBNB_ENV"] = "test"
