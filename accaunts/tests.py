import tempfile
from PIL import Image
from django.urls import reverse
import pytest
from rest_framework.test import APIClient
from django.contrib.auth import get_user_model
from datetime import timedelta
from django.utils import timezone

User = get_user_model()


@pytest.mark.django_db
def test_create_story_success():

    user = User.objects.create_user(email='testuser@gmail.com', password='testpass123')


    image = Image.new('RGB', (100, 100))
    temp_file = tempfile.NamedTemporaryFile(suffix=".jpg")
    image.save(temp_file, format='JPEG')
    temp_file.seek(0)


    video_file = tempfile.NamedTemporaryFile(suffix=".mp4")
    video_file.write(b"fake-video-data")
    video_file.seek(0)


    client = APIClient()
    client.force_authenticate(user=user)

    url = reverse("story-create")  


    data = {
        "title": "Test Story",
        "description": "Test description",
        "expires_at": (timezone.now() + timedelta(hours=1)).isoformat(),
        "is_active": True,
        "image": temp_file,
        "video": video_file
    }

    response = client.post(url, data, format='multipart')


    assert response.status_code == 201
    assert response.data["title"] == "Test Story"
    assert response.data["description"] == "Test description"
