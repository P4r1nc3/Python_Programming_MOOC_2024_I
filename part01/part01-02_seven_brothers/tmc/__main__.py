from unittest import TestProgram
from .runner import TMCTestRunner
import sys

django_defined = False
try:
    with open('.tmcproject.yml') as f:
        for line in f:
            try:
                (key, value) = line.split(":")
                if key.strip().lower() == "django":
                    django_defined = str(value.strip().lower())
            except ValueError:
                pass
except FileNotFoundError:
    pass

if django_defined:
    import os
    import django
    import django.conf
    from django.test.utils import get_runner
    from django.conf import settings
    os.environ['DJANGO_SETTINGS_MODULE'] = django_defined + '.config.settings'
    django.setup()

if sys.argv.__len__() > 1 and sys.argv[1] == 'available_points':
    TMCTestRunner().available_points()
    sys.exit()

if django_defined:
    settings.TEST_RUNNER = 'tmc.django.TMCDiscoverRunner'
    TestRunner = get_runner(settings)
    test_runner = TestRunner()
    failures = test_runner.run_tests(["test"])
    sys.exit(bool(failures))

main = TestProgram
main(testRunner=TMCTestRunner, module=None, failfast=False, buffer=True)
