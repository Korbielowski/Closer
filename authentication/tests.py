from django.test import TestCase

from .models import CloserUser

# from  .views import login

# TODO: Add tests!!!


class AuthenticationTest(TestCase):
    # def testLogin(self):
    #     response = self.client.post("login/", data=("julia@gmail.com", "julia"))
    #     self.assertEqual(response.status_code, 100, "OOps")
    def testCloserUserModel(self):
        user = CloserUser.objects.create(
            email="julian@gmail.com", password="password123"
        )
        self.assertEqual(str(user), "julian@gmail.com password123")
