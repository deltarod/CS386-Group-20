from django.test import TestCase
from .models import School, Profile
from django.contrib.auth.models import User


class TestWebsite(TestCase):

    #Unit test to create a user
    def createUser(self):
        print("Creating a user object")
        return User.objects.create(username="TestUsername")

    #Unit test to create a school
    def createSchool(self):
        print("Creating a school object")
        return School.objects.create(schoolName="TestSchool", location="A Place")


    # Integration test to test that the algorithm for joining schools works
    def testSchoolJoin(self):
        profileInstance = self.createUser()

        schoolinstance = self.createSchool()

        print("Unit test for school join running")

        profileInstance.college = schoolinstance

        self.assertIs( profileInstance.college, schoolinstance)


