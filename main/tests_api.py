from django.contrib.auth.models import User, Group
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase, APIClient

from main.models import Experience


class ExperienceAPITest(APITestCase):
    def setUp(self):
        self.experience = Experience.objects.create(
            title="Test Experience",
            description="Experience for API testing.",
            category="research",
        )

        self.visitor_client = APIClient()

        self.user = User.objects.create_user(
            username="testuser",
            password="testpassword123",
        )

        self.user_client = APIClient()
        self.user_client.force_authenticate(user=self.user)

        self.editor_group = Group.objects.create(name="Editor")

        self.editor = User.objects.create_user(
            username="editor",
            password="editpassword123",
        )
        self.editor.groups.add(self.editor_group)

        self.editor_client = APIClient()
        self.editor_client.force_authenticate(user=self.editor)

        self.owner = User.objects.create_superuser(
            username="owner",
            email="owner@example.com",
            password="ownerpassword123",
        )

        self.owner_client = APIClient()
        self.owner_client.force_authenticate(user=self.owner)

        self.list_url = reverse("api:experience-list")
        self.detail_url = reverse(
            "api:experience-detail",
            kwargs={"experience_id": self.experience.id},
        )
        self.star_url = reverse(
            "api:experience-star",
            kwargs={"experience_id": self.experience.id},
        )

    def test_visitor_can_read_experiences(self):
        response = self.visitor_client.get(self.list_url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_ordinary_user_cannot_create_experience(self):
        response = self.user_client.post(
            self.list_url,
            {
                "title": "New Experience",
                "description": "Should be rejected.",
                "category": "research",
            },
            format="json",
        )

        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
        self.assertEqual(Experience.objects.count(), 1)

    def test_editor_can_patch_experience(self):
        response = self.editor_client.patch(
            self.detail_url,
            {"description": "Updated by editor."},
            format="json",
        )

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.experience.refresh_from_db()
        self.assertEqual(
            self.experience.description,
            "Updated by editor.",
        )

    def test_editor_cannot_create_experience(self):
        response = self.editor_client.post(
            self.list_url,
            {
                "title": "Editor Test",
                "description": "Should be rejected.",
                "category": "research",
            },
            format="json",
        )

        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
        self.assertEqual(Experience.objects.count(), 1)

    def test_editor_cannot_delete_experience(self):
        response = self.editor_client.delete(self.detail_url)

        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
        self.assertTrue(
            Experience.objects.filter(pk=self.experience.pk).exists()
        )

    def test_owner_can_create_experience(self):
        response = self.owner_client.post(
            self.list_url,
            {
                "title": "Owner Test",
                "description": "Created by owner.",
                "category": "research",
            },
            format="json",
        )

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Experience.objects.count(), 2)

    def test_owner_can_delete_experience(self):
        response = self.owner_client.delete(self.detail_url)

        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertFalse(
            Experience.objects.filter(pk=self.experience.pk).exists()
        )

    def test_invalid_title_is_rejected(self):
        response = self.owner_client.post(
            self.list_url,
            {
                "title": "   ",
                "description": "Invalid title.",
                "category": "research",
            },
            format="json",
        )

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(Experience.objects.count(), 1)

    def test_visitor_cannot_star_experience(self):
        response = self.visitor_client.post(self.star_url)

        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
        self.assertFalse(
            self.experience.starred_by.exists()
        )

    def test_ordinary_user_can_star_experience(self):
        response = self.user_client.post(self.star_url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertTrue(
            self.experience.starred_by.filter(pk=self.user.pk).exists()
        )

    def test_csrf_protection(self):
        csrf_client = APIClient(enforce_csrf_checks=True)
        csrf_client.login(
            username="owner",
            password="ownerpassword123",
        )

        response = csrf_client.post(
            self.list_url,
            {
                "title": "CSRF Test",
                "description": "Should be rejected.",
                "category": "research",
            },
            format="json",
        )

        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
        self.assertEqual(Experience.objects.count(), 1)