import unittest
from coverage import Coverage

cov = Coverage()
cov.set_option("run:branch", True)
cov.start()

barGraphSuite = unittest.TestLoader().discover('C:\Python27\Projects\PublicDashboard\Dashboard\Factories Tests\Bar Graph Tests\\', pattern = '*Tests.py')
factoryHelperFunctionsSuite = unittest.TestLoader().discover('C:\Python27\Projects\PublicDashboard\Dashboard\Factories Tests\General Helper Functions Tests\\', pattern = '*Tests.py')
alltests = unittest.TestSuite((barGraphSuite, factoryHelperFunctionsSuite))
unittest.TextTestRunner(verbosity=2).run(alltests)

cov.stop()
cov.html_report(directory='C:\Python27\Projects\PublicDashboard\Dashboard\Factories Tests\Test Coverage', include = 'C:\Python27\Projects\PublicDashboard\Dashboard\*', omit = '*Tests.py')
