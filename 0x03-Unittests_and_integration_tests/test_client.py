#!/usr/bin/env python3
"""A test module for a client class"""
import unittest
from unittest.mock import patch, PropertyMock, Mock
from parameterized import parameterized_class, parameterized
from client import GithubOrgClient
from fixtures import TEST_PAYLOAD
from utils import (
    get_json,
    access_nested_map,
    memoize,
)


class TestGithubOrgClient(unittest.TestCase):
    """Tests the github client class"""
    @parameterized.expand([
        ('google',),
        ('abc',),
        ])
    @patch('client.get_json', return_value={'login': 'trial'})
    def test_org(self, org_name, mock_get_json):
        client = GithubOrgClient(org_name)
        result = client.org
        self.assertEqual(result, {'login': 'trial'})
        mock_get_json.assert_called_once_with(GithubOrgClient.
                                              ORG_URL.format(org=org_name))

    @patch('client.GithubOrgClient.org', new_callable=PropertyMock)
    def test_public_repos_url(self, mock_org):
        org_payload = {'repos_url':
                       'https://api.github.com/orgs/testorg/repos'}
        mock_org.return_value = org_payload
        client = GithubOrgClient('testorg')
        result = client._public_repos_url
        expected_result = GithubOrgClient.ORG_URL.format(
                org='testorg') + '/repos'
        self.assertEqual(result, expected_result)

    @patch('client.GithubOrgClient._public_repos_url',
           new='https://api.github.com/orgs/testorg/repos')
    @patch('client.get_json', return_value=[{"name": "1report"},
           {"name": "2report"}])
    def test_public_repos(self, mock_get_json):
        client = GithubOrgClient('testorg')
        repos = client.public_repos()
        expected_repos = ['1report', '2report']
        self.assertEqual(repos, expected_repos)
        mock_get_json.assert_called_once()
        self.assertEqual(mock_get_json.call_count, 1)

    @parameterized.expand([
        [{"license": {"key": "my_license"}}, "my_license", True],
        [{"license": {"key": "other_license"}}, "my_license", False]
    ])
    def test_has_license(self, repo, license_key, expected_result):
        client = GithubOrgClient('testorg')
        result = client.has_license(repo, license_key)
        self.assertEqual(result, expected_result)

@parameterized_class(('org_payload', 'repos_payload', 'expected_repos', 'apache2_repos'), TEST_PAYLOAD)
class TestIntegrationGithubOrgClient(unittest.TestCase):
    """GothubOrgClient's integration tests"""

    @classmethod
    def setUpClass(cls):
        cls.get_patcher = patch('requests.get')
        cls.mock_get = cls.get_patcher.start()

    @classmethod
    def tearDownClass(cls):
        cls.get_patcher.stop()

    def setUp(self):
        self.mock_get.return_value.json.side_effect = [self.org_payload, self.repos_payload]

    def test_public_repos(self):
        client = GithubOrgClient('testorg')
        repos = client.public_repos()
        self.assertEqual(repos, self.expected_repos)

    def test_public_repos_with_license(self):
        client = GithubOrgClient('testorg')
        self.assertEqual(client.public_repos(), self.expected_repos)
        self.assertEqual(client.public_repos("XLICENSE"), [])
        self.assertEqual(client.public_repos(
            "apache-2.0"), self.apache2_repos)


if __name__ == '__main__':
    unittest.main()
