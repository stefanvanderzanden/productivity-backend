from django.test import TestCase


class TimeRegistrationModelTestCase(TestCase):
    def setUp(self) -> None:
        pass

    def test_save_override_without_end(self):
        """Test that when there is no end time set, the duration field is also not set"""
        pass

    def test_save_override_with_end(self):
        """Test that when there is an end time set, the duration field is calculated and set"""
        pass

    def test_save_override_with_ticket_and_no_subproject(self):
        """Test that `projects.SubProject` gets set to the `projects.SubProject` of the `projects.Ticket`"""
        pass

    def test_save_override_with_ticket_and_other_subproject(self):
        """Test that when a `timeregistrations.TimeRegistration` is saved and the `projects.Ticket` and
        `projects.SubProject` don't match the sub_project is set to the `projects.SubProject` of the `projects.Ticket`
        """
        pass
