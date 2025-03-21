import unittest

from heurist.api.connection import HeuristConnection
from heurist.cli.schema import get_database_schema
from heurist.api.exceptions import MissingParameterException


class SchemaTest(unittest.TestCase):

    def setUp(self):
        try:
            self.client = HeuristConnection()
        except MissingParameterException:
            self.skipTest(
                "Connection could not be established.\nCannot test client without \
                    database connection."
            )
        self.debugging = True

    def test(self):
        db = get_database_schema(
            record_groups=["My record types"],
            client=self.client,
            debugging=True,
        )
        actual = len(db.pydantic_models)
        self.assertGreater(actual, 0)


if __name__ == "__main__":
    unittest.main()
