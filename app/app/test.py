"""
Sample Test
"""

"""
docker-compose run --rm app sh -c "python manage.py test"
"""

from django.test import SimpleTestCase

from app import calc

class CalcTests(SimpleTestCase):
    ''' Test the calc module '''

    def test_add_number(self):
        """Test Adding Number Together"""

        res = calc.add(4,6)

        self.assertEqual(res, 10)

    def test_subtract_number(self):
        """Test Subtract Number"""

        res = calc.subtract(10, 5)

        self.assertEqual(res, 5)