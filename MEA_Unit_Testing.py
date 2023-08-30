#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import unittest
from your_data_collection_module import fetch_data

class TestDataCollection(unittest.TestCase):
    def test_data_collection(self):
        data = fetch_data("https://example.com/mock_data")
        self.assertIsInstance(data, list)
        self.assertTrue(len(data) > 0)

if __name__ == "__main__":
    unittest.main()

