import os

import juxtapy
import juxtapy.model as model

from flask_testing import TestCase

class JuxtapyTestCase(TestCase):

    def create_app(self):
        return juxtapy.app

    def setUp(self):
        """ Put all of the data into the tables """
        self._check_for_testing_env()
        juxtapy.db.create_all()

        #self.fixtures = CasetrackrApiFixtures()
        #self.fixtures.install()

    def tearDown(self):
        """ Remove our session, and remove the data from the testing database """
        juxtapy.db.drop_all()
        juxtapy.db.session.remove()

        #self.fixtures.uninstall()

    def _check_for_testing_env(self):
        """
        Make damn sure we're in the testing environment so we don't screw up any
        real databases.
        """
        env_var = 'JUXTAPY_ENV'
        if not env_var in os.environ:
            raise Exception("Could not find juxtapy environment in OS environment")

        casetrackr_api_env = os.environ[env_var]
        if casetrackr_api_env != 'testing':
            raise Exception("Did not find testing environment - instead, found [%s]" % casetrackr_api_env)
