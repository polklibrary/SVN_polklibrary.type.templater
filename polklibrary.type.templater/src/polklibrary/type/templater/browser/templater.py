from plone import api
from Products.CMFPlone.utils import safe_unicode
from Products.Five import BrowserView
from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile

class Templater(BrowserView):

    template = ViewPageTemplateFile("templater.pt")
    
    def __call__(self):
        return self.template()

    def get_html(self):
        return self._transformed_html()
    
    def _transformed_html(self):
        html = self.context.html
        html = html.replace('${context/absolute_url}', self.context.absolute_url())
        html = html.replace('${portal/absolute_url}', self.portal.absolute_url())
        return html
        
    @property
    def portal(self):
        return api.portal.get()
        
        
        
        