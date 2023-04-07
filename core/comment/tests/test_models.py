import pytest
from core.fixtures.user import user
from core.fixtures.post import post
from core.comment.models import Comment

@pytest.mark.jango_db
def test_create_comment(user, post):
    body = 'Test Comment Body'
    comment = Comment.objects.create(author=user, post=post, body=body)
    assert comment.author == user
    assert comment.post == post
    assert comment.body == body