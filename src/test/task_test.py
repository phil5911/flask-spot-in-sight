import unittest

import app
from flask import request


class TaskTestCase(unittest.TestCase):

    def setUp(self):
        self.app = app.create_app()
        # self.app.app_context().push()
        self.client = self.app.test_client()

    def test_get_task(self):
        response = self.client.get("/task")
        print(response)


if __name__ == "_main__":
    unittest.main()
