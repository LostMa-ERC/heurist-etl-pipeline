import unittest
import pytest
import os

from heurist.api.connection import HeuristConnection
from heurist.api.exceptions import MissingParameterException, AuthenticationError

IN_GITHUB_ACTIONS = os.getenv("GITHUB_ACTIONS") == "true"


class ConnectionWithEnvVars(unittest.TestCase):
    @pytest.mark.skipif(
        IN_GITHUB_ACTIONS, reason="Do not run connection test in GitHub Actions."
    )
    def test_database_env_var(self):
        database = HeuristConnection.load_database(db_name=None)
        self.assertIsNotNone(database)

    @pytest.mark.skipif(
        IN_GITHUB_ACTIONS, reason="Do not run connection test in GitHub Actions."
    )
    def test_database_connection(self):
        login = HeuristConnection.load_login(login=None)
        database = HeuristConnection.load_database(db_name=None)
        password = HeuristConnection.load_password(password=None)
        HeuristConnection.test_connection(
            db=database,
            password=password,
            login=login,
        )

    @pytest.mark.skipif(
        IN_GITHUB_ACTIONS, reason="Do not run connection test in GitHub Actions."
    )
    def test_client_request(self):
        client = HeuristConnection(database_name="api_dev")
        response = client.get_records(form="json", record_type_id=103)
        expected = "Symphony No. 1 in D major"
        actual = [i["rec_Title"] for i in response if i["rec_ID"] == "279"][0]
        self.assertEqual(expected, actual)


class ConnectionWithoutEnvVars(unittest.TestCase):
    def test_missing_login(self):
        with pytest.raises(MissingParameterException):
            HeuristConnection.load_login(login=None, debugging=True)

    def test_missing_db_name(self):
        with pytest.raises(MissingParameterException):
            HeuristConnection.load_database(db_name=None, debugging=True)

    def test_missing_password(self):
        with pytest.raises(MissingParameterException):
            HeuristConnection.load_password(password=None, debugging=True)

    def test_invalid_database_credentials(self):
        with pytest.raises(AuthenticationError):
            HeuristConnection(
                database_name="test_db",
                login="test_user",
                password="test_pass",
            )


if __name__ == "__main__":
    unittest.main()
