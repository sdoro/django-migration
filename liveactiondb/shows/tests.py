from django.test import TestCase

import os
from .models import Show, Episode

class BasicTests(TestCase):

    def test_ver(self):
        f = os.popen('pip freeze | grep -i django')
        ver = f.read()
        self.assertEqual(ver, "Django==1.10.6\n")

    def setUp(self):
        pass
        s = Show.objects.create(title="Crozza", description="satyric TV")
        Episode.objects.create(show=s, title="puntata 3", description="la rottamazione")
        Episode.objects.create(show=s, title="puntata 4", description="rottamato")

    def test_Episode(self):
        show1 = Show.objects.get(title="Crozza")
        self.assertEqual(show1.title, 'Crozza')
        self.assertEqual(show1.description, 'satyric TV')
