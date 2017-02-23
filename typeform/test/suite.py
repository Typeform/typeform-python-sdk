import unittest


def test_suite():
    test_loader = unittest.TestLoader()
    return test_loader.discover('typeform.test', pattern='test_*.py')
