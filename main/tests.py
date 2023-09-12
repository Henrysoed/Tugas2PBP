from django.test import TestCase, Client
from django.urls import reverse

class mainTest(TestCase):
    def test_main_url_is_exist(self):
        response = Client().get('/main/')
        self.assertEqual(response.status_code, 200)

    def test_main_using_main_template(self):
        response = Client().get('/main/')
        self.assertTemplateUsed(response, 'main.html')

    def test_main_html_content(self):
        response = self.client.get(reverse('main.html')) 

        # Memeriksa apakah halaman berhasil dimuat (status kode 200)
        self.assertEqual(response.status_code, 200)

        # Memeriksa apakah konten HTML sesuai dengan yang diharapkan
        self.assertContains(response, '<h5>Name: </h5>')
        self.assertContains(response, '<p>Henry Soedibjo</p>')
        self.assertContains(response, '<h5>Class: </h5>')
        self.assertContains(response, '<p>PBP A</p>')
        self.assertContains(response, '<h5>Amount: </h5>')
        self.assertContains(response, '<p>100</p>')
        self.assertContains(response, '<h5>Description </h5>')
        self.assertContains(response, 'henrysoed Investment Portofolio Inventory for individu task 2 PBP')
