import csv
import unittest
import json

from pathlib import Path

from heurist.api.connection import HeuristConnection
from heurist.cli.schema import schema_command
from heurist.api.exceptions import MissingParameterException
from heurist.validators.record_validator import VALIDATION_LOG


class SchemaBase(unittest.TestCase):
    tempdir = Path(__file__).parent.joinpath("temp")
    tempfile_json = tempdir.joinpath("recordTypes.json")
    client = None
    debugging = False

    def tearDown(self):
        for f in self.tempdir.iterdir():
            f.unlink(missing_ok=True)
        self.tempdir.rmdir()
        VALIDATION_LOG.unlink(missing_ok=True)
        return super().tearDown()

    def json(self):
        _ = schema_command(
            client=self.client,
            record_group=["My record types"],
            outdir=self.tempdir,
            output_type="json",
            debugging=True,
        )
        with open(self.tempfile_json) as f:
            data = json.load(f)
        actual = len(data["items"])
        self.assertGreater(actual, 0)

    def csv(self):
        _ = schema_command(
            client=self.client,
            record_group=["My record types"],
            outdir=self.tempdir,
            output_type="csv",
            debugging=True,
        )
        for file in self.tempdir.iterdir():
            with open(file, mode="r") as f:
                reader = csv.DictReader(f)
                row_count = len([_ for r in reader])
                self.assertGreater(row_count, 0)


class OfflineSchemaCommand(SchemaBase):
    def setUp(self):
        self.tempdir.mkdir(exist_ok=True)
        self.client = HeuristConnection(
            database_name="test_db",
            login="test_login",
            password="test_pass",
            debugging=True,
        )

    def test_json(self):
        self.json()

    def test_csv(self):
        self.csv()


class OnlineSchemaCommand(SchemaBase):
    def setUp(self):
        self.tempdir.mkdir(exist_ok=True)
        try:
            self.client = HeuristConnection()
        except MissingParameterException:
            self.skipTest(
                "Connection could not be established.\nCannot test client without \
                    database connection."
            )

    def test_json(self):
        self.json()

    def test_csv(self):
        self.csv()


if __name__ == "__main__":
    unittest.main()
