import pytest
from core.fixtures.user import user
from core.post.models import Post

@pytest.mark.jango_db
def test_create_post(user):
    body = 'Test Post Body'
    post = Post.objects.create(author=user, body=body)
    assert post.body == body
    assert post.author == user