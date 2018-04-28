from django.test import TestCase
from .models import School, Profile
from django.contrib.auth.models import User


class TestWebsite(TestCase):

    #Unit test to create a user
    def createUser(self):
        print("Creating a user object")
        return User.objects.create(username="TestUsername", first_name="Adam")

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

    # Test that a user is able to change their name
    def testEditAccount(self):
        print("Creating a user object")
        profileInstance = self.createUser()

        print("Creating a new name")
        new_name = "Eve"

        print("Unit test for name change running")
        profileInstance.first_name = new_name
        self.assertIs(profileInstance.first_name, new_name)