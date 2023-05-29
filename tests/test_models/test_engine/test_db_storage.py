#!/usr/bin/python3
"""
Contains the TestDBStorageDocs and TestDBStorage classes
"""

import inspect
import os
import unittest
from datetime import datetime

import models
import pep8
from models.amenity import Amenity
from models.base_model import BaseModel
from models.city import City
from models.engine import db_storage
from models.engine.db_storage import classes
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User

DBStorage = db_storage.DBStorage


class TestDBStorageDocs(unittest.TestCase):
    """Tests to check the documentation and style of DBStorage class"""
    @classmethod
    def setUpClass(cls):
        """Set up for the doc tests"""
        cls.dbs_f = inspect.getmembers(DBStorage, inspect.isfunction)

    def test_pep8_conformance_db_storage(self):
        """Test that models/engine/db_storage.py conforms to PEP8."""
        pep8s = pep8.StyleGuide(quiet=True)
        result = pep8s.check_files(['models/engine/db_storage.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")

    def test_db_storage_module_docstring(self):
        """Test for the db_storage.py module docstring"""
        self.assertIsNot(db_storage.__doc__, None,
                         "db_storage.py needs a docstring")
        self.assertTrue(len(db_storage.__doc__) >= 1,
                        "db_storage.py needs a docstring")

    def test_db_storage_class_docstring(self):
        """Test for the DBStorage class docstring"""
        self.assertIsNot(DBStorage.__doc__, None,
                         "DBStorage class needs a docstring")
        self.assertTrue(len(DBStorage.__doc__) >= 1,
                        "DBStorage class needs a docstring")

    def test_dbs_func_docstrings(self):
        """Test for the presence of docstrings in DBStorage methods"""
        for func in self.dbs_f:
            self.assertIsNot(func[1].__doc__, None,
                             "{:s} method needs a docstring".format(func[0]))
            self.assertTrue(len(func[1].__doc__) >= 1,
                            "{:s} method needs a docstring".format(func[0]))


class TestFileStorage(unittest.TestCase):
    @classmethod
    def tearDown(self):
        try:
            models.storage.close()
            os.environ.pop("HBNB_MYSQL_USER", None)
            os.environ.pop("HBNB_MYSQL_PWD", None)
            os.environ.pop("HBNB_MYSQL_HOST", None)
            os.environ.pop("HBNB_MYSQL_DB", None)
            os.environ.pop("HBNB_ENV", None)
            os.environ.pop("HBNB_TYPE_STORAGE", None)
        except IOError:
            pass

    """Test the FileStorage class"""
    @unittest.skipIf(models.storage_t != 'db', "not testing db storage")
    def test_all_returns_dict(self):
        """Test that all returns a dictionaty"""
        expected = dict
        result = models.storage.all()
        self.assertIs(type(result), dict)

    @unittest.skipIf(models.storage_t != 'db', "not testing db storage")
    def test_all_no_class(self):
        """Test that all returns all rows when no class is passed"""

    @unittest.skipIf(models.storage_t != 'db', "not testing db storage")
    def test_new(self):
        """test that new adds an object to the database"""

    @unittest.skipIf(models.storage_t != 'db', "not testing db storage")
    def test_save(self):
        """Test that save properly saves objects to file.json"""


class TestGetMethod(unittest.TestCase):
    @classmethod
    def tearDown(self):
        try:
            models.storage.close()
            os.environ.pop("HBNB_MYSQL_USER", None)
            os.environ.pop("HBNB_MYSQL_PWD", None)
            os.environ.pop("HBNB_MYSQL_HOST", None)
            os.environ.pop("HBNB_MYSQL_DB", None)
            os.environ.pop("HBNB_ENV", None)
            os.environ.pop("HBNB_TYPE_STORAGE", None)
        except IOError:
            pass

    def test_invalid_class(self):
        """Return None if given classname does is invalid"""
        model = "BModel"
        id = '74220232-66f4-4a70-af13-0adf796f9edf'
        expected = None
        result = models.storage.get(model, id)
        self.assertEqual(result, expected)

    def test_incorrect_id(self):
        """Return None if the ID is incorrect"""
        model = "BaseModel"
        id = "74220232-66f4-4a70-af13-0adf796f9edf"
        expected = None
        result = models.storage.get(model, id)
        self.assertEqual(result, expected)

    def test_correctness(self):
        """Test that the correct object is retrieved when the correct class and ID are passed"""
        model = State
        inst = State(name="Lagos")
        id = inst.id
        inst.save()
        all = models.storage.all()
        result = models.storage.get(model, id)
        expected = id
        self.assertEqual(expected, result.id)


class TestCountMethod(unittest.TestCase):
    @classmethod
    def setUp(cls) -> None:
        # models.storage.drop_all()
        new_state = State(name="Akwa_Ibom")
        new_user = User(email="johndoe@mail.com",
                        password="P@55w0rd",
                        first_name="John",
                        last_name="Doe",
                        )
        new_state.save()
        new_user.save()

    @classmethod
    def tearDown(self):
        try:
            models.storage.close()
            os.environ.pop("HBNB_MYSQL_USER", None)
            os.environ.pop("HBNB_MYSQL_PWD", None)
            os.environ.pop("HBNB_MYSQL_HOST", None)
            os.environ.pop("HBNB_MYSQL_DB", None)
            os.environ.pop("HBNB_ENV", None)
            os.environ.pop("HBNB_TYPE_STORAGE", None)
        except IOError:
            pass

    def test_class_as_None(self):
        """Test that the total data count is returned if the \
            class parameter is None"""
        expected = 2
        result = models.storage.count()
        self.assertEqual(result, expected)

    def test_class_count(self):
        """Return specified class count"""
        expected = 2
        result = models.storage.count("State")
        self.assertEqual(result, expected)
