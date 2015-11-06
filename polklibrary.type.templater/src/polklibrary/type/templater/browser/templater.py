from plone import api
from Products.CMFPlone.utils import safe_unicode
from Products.Five import BrowserView
from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile

class Templater(BrowserView):

    template = ViewPageTemplateFile("templater.pt")
    
    def __call__(self):
        return self.template()

    def get_html(self):
        return self._transformed_html(self.context.html, self.context.set_context)
    
    def _transformed_html(self, html, context):
        """ I can't figure out how to send through tal interpreter, so this will do for now. """
        if not context:
            context = self.context
        
        html = html.replace('${context/absolute_url}', context.absolute_url())
        html = html.replace('${portal/absolute_url}', self.portal.absolute_url())
        return html
        
    @property
    def portal(self):
        return api.portal.get()
        
        

class PreviewTemplater(Templater):
        
    template = ViewPageTemplateFile("previewtemplater.pt")
    title = ''
    description = ''
    css = ''
    js = ''
    html = ''
    body = ''
    suppress_title = False
    suppress_description = False
    set_context = ''
    
    def __call__(self):
    
        if self.request.form.get('form.buttons.preview',''):
            print "LOADING >>>>>>"
            self.title = self.request.form.get('form.widgets.title','')
            self.description = self.request.form.get('form.widgets.description','')
            self.css = self.request.form.get('form.widgets.css','')
            self.js = self.request.form.get('form.widgets.js','')
            self.html = self.request.form.get('form.widgets.html','')
            self.suppress_title = self.request.form.get('form.widgets.suppress_title-empty-marker',False)
            self.suppress_description = self.request.form.get('form.widgets.suppress_description-empty-marker',False)
            self.set_context = self.request.form.get('form.widgets.set_context','')
    
        return self.template()

        
    def get_html(self):
        return self._transformed_html(self.html, self.set_context)