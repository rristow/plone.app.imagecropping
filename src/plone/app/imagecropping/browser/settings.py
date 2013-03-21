from zope.interface import (
    Interface,
    implementer
)
from zope.schema.interfaces import IVocabularyFactory
from zope.schema.vocabulary import SimpleVocabulary
from plone.app.registry.browser.controlpanel import (
    ControlPanelFormWrapper,
    RegistryEditForm,
)
from plone.z3cform import layout
from plone.registry.field import (
    List,
    Choice,
    TextLine,
    Bool,
)
from plone.app.imaging.utils import getAllowedSizes
from plone.app.imagecropping import imagecroppingMessageFactory as _


@implementer(IVocabularyFactory)
class SizesVocabulary(object):

    def __call__(self, context):
        allowed_sizes = getAllowedSizes()
        size_names = allowed_sizes and allowed_sizes.keys() or []
        return SimpleVocabulary.fromValues(size_names)


class ISettings(Interface):
    """ Define settings data structure """

    large_size = TextLine(
        title=_(u"Crop Editor Large Size"),
        description=_(u"width:height"),
        required=False,
        default=u"768:768",
    )

    min_size = TextLine(
        title=_(u"Minimum Crop Area Size"),
        description=_(u"width:height"),
        required=False,
        default=u"50:50",
    )

    constrain_cropping = Bool(
        title=_(u"Enable to constrain cropable scales"),
        description=_(u"Enable to reduce the scales shown for cropping in the "
                      u"list of scales with crop support."),
        default=False,
        required=False,
    )

    cropping_for = List(
        title=_(u"List of scales with crop support"),
        description=_(u"Select the scales with cropping support enabled. Only "
                      u"active if enabled with checkbox."),
        required=False,
        default=[],
        value_type=Choice(
            vocabulary="plone.app.imagecropping.all_sizes"),
    )

    auto_cropping_for = List(
        title=_(u"Scales with auto crop"),
        description=_(u"Scales to be auto cropped in center of image."),
        required=False,
        default=[],
        value_type=Choice(
            vocabulary="plone.app.imagecropping.all_sizes"),
    )


class SettingsEditForm(RegistryEditForm):
    """
    Define form logic
    """
    schema = ISettings
    label = _(u"Image Cropping Settings")


SettingsView = layout.wrap_form(SettingsEditForm, ControlPanelFormWrapper)
