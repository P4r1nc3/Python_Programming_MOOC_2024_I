from django.test.runner import DiscoverRunner
from tmc import runner


class TMCDiscoverRunner(DiscoverRunner):
    test_runner = runner.TMCTestRunner
