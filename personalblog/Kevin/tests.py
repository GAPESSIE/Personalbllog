from django.test import TestCase
from .models import *
# Create your tests here.

class UserRegistrationAuthenticationTest(TestCase):
    def test_user_registration(self):
        user = User.objects.create(username='testuser', email='test@example.com', password='testpassword')
        self.assertEqual(user.username, 'testuser')
        self.assertEqual(user.email, 'test@example.com')
        # Add more assertions as needed

    def test_user_authentication(self):
        user = User.objects.create(username='testuser', email='test@example.com', password='testpassword')
        authenticated_user = User.objects.get(username='testuser')
        self.assertEqual(user, authenticated_user)
        # Add more assertions as needed


class PostCreationUpdateDeletionTest(TestCase):
    def setUp(self):
        self.user = User.objects.create(username='testuser', email='test@example.com', password='testpassword')

    def test_post_creation(self):
        post = KevinPost.objects.create(title='Test Post', content='This is a test post.', user=self.user)
        self.assertEqual(post.title, 'Test Post')
        self.assertEqual(post.content, 'This is a test post.')
        # Add more assertions as needed

    def test_post_update(self):
        post = KevinPost.objects.create(title='Test Post', content='This is a test post.', user=self.user)
        post.title = 'Updated Post'
        post.content = 'This is an updated post.'
        post.save()
        updated_post = KevinPost.objects.get(pk=post.pk)
        self.assertEqual(updated_post.title, 'Updated Post')
        self.assertEqual(updated_post.content, 'This is an updated post.')
        # Add more assertions as needed

    def test_post_deletion(self):
        post = KevinPost.objects.create(title='Test Post', content='This is a test post.', user=self.user)
        post.delete()
        with self.assertRaises(KevinPost.DoesNotExist):
            KevinPost.objects.get(pk=post.pk)
        # Add more assertions as needed


class CommentAdditionDeletionTest(TestCase):
    def setUp(self):
        self.user = User.objects.create(username='testuser', email='test@example.com', password='testpassword')
        self.post = KevinPost.objects.create(title='Test Post', content='This is a test post.', user=self.user)

    def test_comment_addition(self):
        comment = KevinComment.objects.create(content='This is a test comment.', post=self.post, user=self.user)
        self.assertEqual(comment.content, 'This is a test comment.')
        # Add more assertions as needed

    def test_comment_deletion(self):
        comment = KevinComment.objects.create(content='This is a test comment.', post=self.post, user=self.user)
        comment.delete()
        with self.assertRaises(KevinComment.DoesNotExist):
            KevinComment.objects.get(pk=comment.pk)
        # Add more assertions as needed