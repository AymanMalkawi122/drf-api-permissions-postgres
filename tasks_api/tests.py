from django.test import TestCase

# Create your tests here.
from django.test import TestCase
from django.contrib.auth import get_user_model
from django.urls import reverse
from rest_framework.test import APITestCase
from rest_framework import status

from .models import Task
# Create your tests here.
class TaskTest(APITestCase):
    @classmethod
    def setUpTestData(cls):
        testuser1 = get_user_model().objects.create_user(
            username="testuser1", password="pass"
        )
        testuser1.save()
        testuser2 = get_user_model().objects.create_user(
            username="admin", password="admin",is_staff = True
        )
        testuser2.save() 

    

        test_task = Task.objects.create(
            assignee = testuser1,
            desc = "empty"
        )
        test_task.save()

    def setUp(self) -> None:
         self.client.login(username="testuser1", password="pass")  

   
    def test_tasks_model(self):
        task = Task.objects.get(id=1)
        actual_owner = str(task.assignee)
        actual_desc = str(task.desc)
        self.assertEqual(actual_owner, "testuser1")
        self.assertEqual(actual_desc, "empty")

    def test_get_task_list(self):
        url = reverse("tasks_list")
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        tasks = response.data
        self.assertEqual(len(tasks), 1)
        self.assertEqual(tasks[0]["desc"], "empty")

    def test_only_admin_can_modify_task(self):
        self.client.logout()
        self.client.login(username="testuser2", password="pass2")
        url = reverse("task_detail",args=[1])  
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)