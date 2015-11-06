from polklibrary.type.templater import MessageFactory as _
from plone import api
from plone.app.textfield import RichText
from plone.supermodel import model
from zope import schema
from zope.interface import directlyProvides
from zope.schema.interfaces import IContextSourceBinder
from zope.schema.vocabulary import SimpleVocabulary


class ITemplater(model.Schema):

    title = schema.TextLine(
            title=u"Title",
            required=True,
        )

    description = schema.Text(
            title=u"Description",
            required=False,
        )
            
    js = schema.Text(
            title=u"Javascript",
            description=u"You must include the &lt;script&gt; elements",
            required=False,
        )
         
    css = schema.Text(
            title=u"CSS",
            description=u"You must include the &lt;style&gt; elements",
            required=False,
        )
        
    html = schema.Text(
            title=u"HTML",
            required=False,
        )
        
        
    suppress_title = schema.Bool(
            title=u"Suppress Title",
            default=False,
            required=False,
        )
        
    suppress_description = schema.Bool(
            title=u"Suppress Description",
            default=False,
            required=False,
        )
        
    exclude_from_nav = schema.Bool(
            title=u"Exclude from nav",
            default=False,
            required=False,
        )
        
    set_context = schema.TextLine(
            title=u"Set Context Path",
            description=u"If provided, this page will load in the object context of the provided path: e.x. /yoursite/folder/my-document",
            default=u"",
            required=False,
        )
        