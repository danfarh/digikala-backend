from category.models import Category
from comment.models import Comment
from product.models import Product
from rest_framework.test import APITestCase
from rest_framework.reverse import reverse as api_reverse

# Standard library import
from django.contrib.auth import get_user_model

User = get_user_model()


class UserTestCase(APITestCase):
    def setUp(self):
        user = User(
            username='test',
            email='test@gmail.com',
        )
        user.set_password('testpassword')
        user.save()

        category = Category(
            title='digital',
            slug='digital',
            status=True
        )
        category.save()

        product = Product(
            title='product1',
            category=category,
            description='this is product1',
            slug= 'product1',
            weight=150,
            status='p',
            price=2000
        )
        product.save()

        comment = Comment(
            user=user,
            product=product,
            title='comment1',
            text='this product was great',
            rate='5',
            confirm=True
        )
        comment.save()

    def test_single_comment(self):
        comment_count = Comment.objects.count()
        self.assertEqual(comment_count, 1)
    
    # def test_user_sign_up(self):
    #     data = {
    #         'username': 'dani',
    #         'email': 'dani@email.com',
    #         'password1': 'Dani12345678dani',
    #         'password2': 'Dani12345678dani'
    #     }
    #     url = api_reverse('accounts:register')
    #     response = self.client.post(url, data, format='json')
    #     self.assertEqual(response.status_code, 201)
    
    # def test_user_retrieve(self):
    #     response = self.client.get('/api/user/', format='json')
    #     self.assertEqual(response.status_code, 401)
    
    # def test_user_update(self):
    #     data = {'phone_number': '09373538508'}
    #     response = self.client.put('/api/user/update/', data, format='json')
    #     self.assertEqual(response.status_code, 401)

