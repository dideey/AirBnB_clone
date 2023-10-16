#!/usr/bin/python3
"""test module"""
import unittest
from datetime import datetime
import uuid
from models.base_model import BaseModel


class TestBaseModel(unittest.TestCase):
    """test module"""

    def test_attribute(self):
        """test_attribute"""
        my_model1 = BaseModel()
        my_model2 = BaseModel()
        self.assertNotEqual(my_model1.id, my_model2.id)

    def test_instance(self):
        """test_instance"""
        my_model1 = BaseModel()
        my_model2 = BaseModel()
        self.assertNotEqual(my_model1, my_model2)

    def test_isstr(self):
        """test_isstr"""
        my_model = BaseModel()
        self.assertIsInstance(my_model.id, str)

    def test_base_obj(self):
        """test_base_obj"""
        self.assertIsInstance(BaseModel(), object)

    def test_print_format(self):
        """test_print_format"""
        obj = BaseModel()
        expected_format = f"[BaseModel] ({obj.id}) {obj.__dict__}"
        self.assertEqual(str(obj), expected_format)

    def test_attribute_inequalty(self):
        """test_attribute_inequalty"""
        my_model = BaseModel()
        created_at = my_model.created_at
        updated_at = my_model.updated_at

        my_model.test_attr = "test"
        my_model.save()

        self.assertGreater(my_model.updated_at, updated_at)
        self.assertEqual(my_model.created_at, created_at)

    def test_id_inequality(self):
        """test_id_inequality"""
        my_model1 = BaseModel()
        my_model2 = BaseModel()
        self.assertNotEqual(my_model1.id, my_model2.id)

    def test_createdtime_isless(self):
        """test_createdtime_isless"""
        my_model = BaseModel()
        current_time = datetime.now()
        self.assertLess(my_model.created_at, current_time)

    def test_updatedat_inequality(self):
        """test_updatedat_inequality"""
        my_model = BaseModel()

        before_save_time = my_model.updated_at

        my_model.test_attr = "tests"
        my_model.save()

        after_save_time = my_model.updated_at
        self.assertNotEqual(before_save_time, after_save_time)

    def test_check_id(self):
        """test_check_id"""
        my_model = BaseModel()
        self.assertTrue(uuid.UUID(my_model.id, version=4))
        self.assertEqual(len(my_model.id), 36)

    def test_iso_format_in_to_dict(self):
        """test_iso_format_in_to_dict"""
        model = BaseModel()

        # Convert the BaseModel instance to a dictionary using to_dict
        model_dict = model.to_dict()

        # Check the format of created_at and updated_at in the dictionary
        for key in ['created_at', 'updated_at']:
            timestamp_str = model_dict[key]
            timestamp = datetime.strptime(timestamp_str,
                                          '%Y-%m-%dT%H:%M:%S.%f')
            format_timestamp_str = timestamp.strftime('%Y-%m-%dT%H:%M:%S.%f')

            # Ensure the timestamp string matches the specified ISO format
            self.assertEqual(timestamp_str, format_timestamp_str)

    def test_updated_before_after(self):
        """test_updated_before_after"""
        model = BaseModel()
        before_save = model.updated_at
        model.test_attr = "test"
        model.save()

        after_save = model.updated_at
        self.assertGreater(after_save, before_save)

    def test_to_dict_elements(self):
        """test_to_dict_elements"""
        model = BaseModel()

        model_dict = model.to_dict()
        expected_keys = ('id', 'created_at', 'updated_at',"__class__")
        self.assertCountEqual(model_dict.keys(), expected_keys)

        self.assertIsNotNone(model_dict['id'])
        self.assertIsNotNone(model_dict['created_at'])
        self.assertIsNotNone(model_dict['updated_at'])

    def test_created_at_and_updated_at_types(self):
        """test_created_at_and_updated_at_types"""
        model = BaseModel()
        self.assertIsInstance(model.created_at, datetime)
        self.assertIsInstance(model.updated_at, datetime)

    def test_to_dict(self):
        """test_to_dict"""
        model = BaseModel()

        model_dict = model.to_dict()
        self.assertIsInstance(model_dict, dict)

        self.assertIn('__class__', model_dict)

    def test_deserialization_and_reloading_from_json(self):
        """test_deserialization_and_reloading_from_json"""
    # Create a BaseModel instance
        model = BaseModel()
        model.some_attribute = "test"

    # Serialize the BaseModel instance to JSON
        json_data = model.to_dict()

    # Deserialize the JSON back into a new BaseModel instance
        deserialized_obj = BaseModel(**json_data)

    # Verify that the deserialized instance is equivalent to the original one
        self.assertEqual(deserialized_obj.id, model.id)
        self.assertEqual(deserialized_obj.some_attribute, model.some_attribute)

    def test_instance_creation_with_attributes(self):
        """test_instance_creation_with_attributes"""
    # Create a BaseModel instance with attributes
        model = BaseModel(some_attribute="test", another_attribute=42)

    # Verify that the attributes are set correctly
        self.assertEqual(model.some_attribute, "test")
        self.assertEqual(model.another_attribute, 42)

    def test_obj_id_equal_with_kwargs_not_empty(self):
        """test_obj_id_equal_with_kwargs_not_empty"""

        kwargs = {'some_attribute': 'some_value'}
        model1 = BaseModel(**kwargs)
        model2 = BaseModel(**kwargs)

    # Verify that the IDs are equal and not empty
        self.assertNotEqual(model1.id, model2.id)
        self.assertNotEqual(model1.id, '')
        self.assertNotEqual(model2.id, '')

    def test_obj_id_equal_with_empty_kwargs(self):
        """test_obj_id_equal_with_empty_kwargs"""

        model1 = BaseModel()
        model2 = BaseModel()

        self.assertNotEqual(model1.id, model2.id)
        self.assertNotEqual(model1.id, '')
        self.assertNotEqual(model2.id, '')
