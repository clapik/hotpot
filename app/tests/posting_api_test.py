__author__ = 'toanngo'
import unittest
from app.api.posting_api import get_postings_helper, jsonify_postings, edit_posting_helper
import datetime


class PostingApiTest(unittest.TestCase):
    def test_get_postings_helper(self):
        postings = get_postings_helper()
        self.assertTrue(len(postings) > 1)

    def test_get_postings_helper_with_query(self):
        postings = get_postings_helper(query={'username': 'toanngo'})
        self.assertTrue(len(postings) > 1)
        postings = jsonify_postings(postings).get('result')
        for posting in postings:
            self.assertTrue(posting.get('cook_username') == 'toanngo')

    def test_jsonify_postings(self):
        postings = get_postings_helper()
        result = jsonify_postings(postings)
        self.assertTrue(isinstance(result, dict))
        if len(result) > 0:
            result = result.get('result')[0]
            self.assertTrue(isinstance(result, dict))
            self.assertTrue('id' in result and 'cook_username' in result)

    def test_edit_posting_helper(self):
        posting = {'id': 11, 'description': 'South Vietname Authentic',
                   'date': datetime.date(year=2015, month=5, day=20),
                   'price': 13.99}
        p = edit_posting_helper(posting)
        self.assertTrue(p)
        self.assertTrue(p.description == posting['description'])
        self.assertTrue(p.price == posting['price'])

    def test_delete_posting_helper(self):
        pass


if __name__ == '__main__':
    unittest.main()