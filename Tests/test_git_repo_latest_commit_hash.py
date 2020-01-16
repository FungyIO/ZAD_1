import unittest
from git_repo_latest_commit_hash import get_git_commit_hash


class TestFrom_file(unittest.TestCase):
    def test_parse_functions_names_from_file(self):
        hash = get_git_commit_hash("../../test-repo")
        self.assertEqual(hash, "c4058527df84b73a208251e2aa82d3fca4af4879")
