__author__ = 'toanngo'
import unittest
from app.api.posting_api import get_postings_helper, jsonify_postings


class PostingApiTest(unittest.TestCase):
    def test_get_postings_helper(self):
        postings = get_postings_helper()
        self.assertTrue(len(postings) > 1)

    def test_get_postings_helper_with_query(self):
        postings = get_postings_helper(query={'username': 'toanngo2'})
        self.assertTrue(len(postings) > 1)
        postings = jsonify_postings(postings).get('result')
        for posting in postings:
            self.assertTrue(posting.get('cook_username') == 'toanngo2')

    def test_jsonify_postings(self):
        postings = get_postings_helper()
        result = jsonify_postings(postings)
        self.assertTrue(isinstance(result, dict))
        if len(result) > 0:
            result = result.get('result')[0]
            self.assertTrue(isinstance(result, dict))
            self.assertTrue('id' in result and 'cook_username' in result)


if __name__ == '__main__':
    unittest.main()