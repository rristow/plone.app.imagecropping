from zope.component import queryUtility
from Products.CMFCore.utils import getToolByName
from plone.registry.interfaces import IRegistry
from .browser.settings import ISettings
import logging

logger = logging.getLogger('plone.app.imagecropping')
PROFILE_ID = 'profile-plone.app.imagecropping:default'


def migrate0002to0003(context):
    setup_tool = getToolByName(context, 'portal_setup')
    setup_tool.runImportStepFromProfile(PROFILE_ID, 'plone.app.registry')

    registry = queryUtility(IRegistry)
    settings = registry.forInterface(ISettings, check=False)
    if not hasattr(settings, 'constrain_cropping'):
        settings.constrain_cropping = False
    if not hasattr(settings, 'cropping_for'):
        settings.cropping_for = []
    if not hasattr(settings, 'default_cropping_for'):
        settings.default_cropping_for = []
    logger.info('Registry cleanup operation performed')
    logger.info('Migrated to profile version 0003')
