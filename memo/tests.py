from django.test import TestCase, Client
from django.contrib.auth.models import User
from .models import Memo


class MemoTestCase(TestCase):
    def setUp(self):
        # テスト用のユーザーとメモを作成
        self.user = User.objects.create_user(
            username='testuser', password='testpass123'
        )
        self.other_user = User.objects.create_user(
            username='otheruser', password='testpass123'
        )
        self.memo = Memo.objects.create(
            title='テストメモ',
            content='テスト内容',
            user=self.user
        )
        self.client = Client()

    def test_login_required(self):
        """未ログインではメモ一覧にアクセスできない"""
        response = self.client.get('/')
        self.assertNotEqual(response.status_code, 200)

    def test_memo_list_shows_own_memos(self):
        """自分のメモだけ表示される"""
        self.client.login(username='testuser', password='testpass123')
        response = self.client.get('/')
        self.assertContains(response, 'テストメモ')

    def test_memo_list_hides_others_memos(self):
        """他人のメモは表示されない"""
        self.client.login(username='otheruser', password='testpass123')
        response = self.client.get('/')
        self.assertNotContains(response, 'テストメモ')

    def test_create_memo(self):
        """メモを作成できる"""
        self.client.login(username='testuser', password='testpass123')
        response = self.client.post('/new/', {
            'title': '新しいメモ',
            'content': '新しい内容'
        })
        self.assertEqual(Memo.objects.count(), 2)

    def test_cannot_edit_others_memo(self):
        """他人のメモは編集できない（404になる）"""
        self.client.login(username='otheruser', password='testpass123')
        response = self.client.get(f'/{self.memo.pk}/edit/')
        self.assertEqual(response.status_code, 404)