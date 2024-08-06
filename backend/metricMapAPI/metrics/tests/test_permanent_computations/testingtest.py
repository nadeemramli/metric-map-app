from django.test import TestCase

class MinimalTest(TestCase):
    def test_minimal(self):
        print("Running minimal test")
        self.assertTrue(True)

if __name__ == '__main__':
    from django.core.management import call_command
    call_command('test')