#!/usr/bin/python3
import unittest
import datetime

from models.base_model import BaseModel

class TestBaseModel(unittest.TestCase):

    def test_attribute(self):
        my_model1 = BaseModel()
        my_model2 = BaseModel()
        self.assertNotEqual(my_model1.id, my_model2.id)
        

    def test_instance(self):
        my_model1 = BaseModel()
        my_model2 = BaseModel()
        self.assertNotEqual(my_model1, my_model2)

    def test_isstr(self):
        my_model = BaseModel()
        self.assertIsInstance(my_model.id, str)
    
    def test_base_obj(self):
        self.assertIsInstance(BaseModel(), object)

    def test_print_format(self):
        obj = BaseModel()
        expected_format = f"[BaseModel] ({obj.id}) {obj.__dict__}"
        self.assertEqual(str(obj), expected_format)

    def test_attribute_inequalty(self):
        my_model = BaseModel()
        created_at = my_model.created_at
        updated_at = my_model.updated_at

        my_model.test_attr = "test"
        my_model.save()

        self.assertGreater(my_model.updated_at, updated_at)
        self.assertEqual(my_model.created_at, created_at)

    def test_id_inequality(self):
        my_model1 = BaseModel()
        my_model2 = BaseModel()
        self.assertNotEqual(my_model1.id, my_model2.id)

    def test_createdtime_isless(self):
        my_model = BaseModel()
        current_time = datetime.datetime.now()
        self.assertLess(my_model.created_at, current_time)

    def test_updatedat_inequality(self):
         my_model = BaseModel()

         before_save_time = my_model.updated_at

         my_model.test_attr = "tests"
         my_model.save()

         after_save_time = my_model.updated_at
         self.assertNotEqual(before_save_time, after_save_time)

    def test_check_id(self):
        my_model = BaseModel()
        self.assertTrue(uuid.UUID(my_model.id, version=4))
        self.assertEqual(len(my_model.id), 36)

    def test_iso_format_in_to_dict(self):
        model = BaseModel()

        # Convert the BaseModel instance to a dictionary using to_dict
        model_dict = model.to_dict()

        # Check the format of created_at and updated_at in the dictionary
        for key in ['created_at', 'updated_at']:
            timestamp_str = model_dict[key]
            timestamp = datetime.datetime.strptime(timestamp_str, '%Y-%m-%dT%H:%M:%S.%f')
            formatted_timestamp_str = timestamp.strftime('%Y-%m-%dT%H:%M:%S.%f')

            # Ensure the timestamp string matches the specified ISO format
            self.assertEqual(timestamp_str, formatted_timestamp_str)

        def test_updated_before_after(self):
            model = BaseModel()
            before_save = model.updated_at

            time.sleep(1)  # Sleep to ensure a time difference
            model.test_attr = "test"
            model.save()

            after_save = model.updated_at
            set.assertGreater(after_save, before_save)
        
        def test_to_dict_elements(self):
            model = BaseModel()

    
            model_dict = obj.to_dict()
            expected_keys = ['id', 'created_at', 'updated_at']
            self.assertCountEqual(model_dict.keys(), expected_keys)

            self.assertIsNotNone(obj_dict['id'])
            self.assertIsNotNone(obj_dict['created_at'])
            self.assertIsNotNone(obj_dict['updated_at'])

        def test_created_at_and_updated_at_types(self):
        
            model = BaseModel()
            self.assertIsInstance(model.created_at, datetime)

            self.assertIsInstance(obj.updated_at, datetime)

        def test_to_dict(self):
            model = BaseModel()

            model_dict = model.to_dict()
            self.assertIsInstance(model_dict, dict)

            self.assertIn('__class__', model_dict)

        def test_deserialization_and_reloading_from_json(self):
        # Create a BaseModel instance
            model = BaseModel()
            model.some_attribute = "test"

        # Serialize the BaseModel instance to JSON
            json_data = model.to_json()

        # Deserialize the JSON back into a new BaseModel instance
            deserialized_obj = BaseModel.from_json(json_data)

        # Verify that the deserialized instance is equivalent to the original one
            self.assertEqual(deserialized_obj.id, model.id)
            self.assertEqual(deserialized_obj.some_attribute, model.some_attribute)

        def test_instance_creation_with_attributes(self):
        # Create a BaseModel instance with attributes
            model = BaseModel(some_attribute="test", another_attribute=42)

        # Verify that the attributes are set correctly
            self.assertEqual(model.some_attribute, "test")
            self.assertEqual(model.another_attribute, 42)

        def test_obj_id_equal_with_kwargs_not_empty(self):
    
            kwargs = {'some_attribute': 'some_value'}
            model1 = BaseModel(**kwargs)
            model2 = BaseModel(**kwargs)

        # Verify that the IDs are equal and not empty
            self.assertEqual(model1.id, model2.id)
            self.assertNotEqual(model1.id, '')
            self.assertNotEqual(model2.id, '')

        def test_obj_id_equal_with_empty_kwargs(self):

            model1 = BaseModel()
            model2 = BaseModel()

            self.assertEqual(obj1.id, obj2.id)
            self.assertNotEqual(obj1.id, '')
            self.assertNotEqual(obj2.id, '')
