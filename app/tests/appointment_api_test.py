__author__ = 'toanngo'
import unittest
from app.api.appointment_api import get_appointments_helper, create_appointment_helper
from app.models import Users, Posting


class PostingApiTest(unittest.TestCase):
    @unittest.skip("skip to prevent creating too many appointments")
    def test_create_appointment_helper(self):

        user = Users.query.filter_by(username='toanngo').first()
        posting_id = Posting.query.filter(Posting.cook_id != user.id).first().id
        appointment = create_appointment_helper(user, posting_id)
        self.assertTrue(appointment)
        self.assertTrue(appointment.customer_id == user.id)

    def test_get_appointments_helper(self):
        user = Users.query.filter_by(username='toanngo').first()
        appointments = get_appointments_helper(user)
        for appointment in appointments:
            print(appointment)
        self.assertTrue(appointments)


if __name__ == '__main__':
    unittest.main()