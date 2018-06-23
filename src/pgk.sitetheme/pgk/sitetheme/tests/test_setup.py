# -*- coding: utf-8 -*-
"""Setup/installation tests for this package."""

from pgk.buildout.testing import IntegrationTestCase
from plone import api


class TestInstall(IntegrationTestCase):
    """Test installation of pgk.buildout into Plone."""

    def setUp(self):
        """Custom shared utility setup for tests."""
        self.portal = self.layer['portal']
        self.installer = api.portal.get_tool('portal_quickinstaller')

    def test_product_installed(self):
        """Test if pgk.buildout is installed with portal_quickinstaller."""
        self.assertTrue(self.installer.isProductInstalled('pgk.buildout'))

    def test_uninstall(self):
        """Test if pgk.buildout is cleanly uninstalled."""
        self.installer.uninstallProducts(['pgk.buildout'])
        self.assertFalse(self.installer.isProductInstalled('pgk.buildout'))

    # browserlayer.xml
    def test_browserlayer(self):
        """Test that IPgkBuildoutLayer is registered."""
        from pgk.buildout.interfaces import IPgkBuildoutLayer
        from plone.browserlayer import utils
        self.failUnless(IPgkBuildoutLayer in utils.registered_layers())
