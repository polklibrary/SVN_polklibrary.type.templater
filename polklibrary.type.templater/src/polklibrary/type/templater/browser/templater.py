from chameleon import PageTemplate
from plone import api
from Products.CMFPlone.utils import safe_unicode
from Products.Five import BrowserView
from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile


class Templater(BrowserView):

    template = ViewPageTemplateFile("templater.pt")
    
    def __call__(self):
        return self.template()

    def get_style(self):
        return self.context.css.replace('<style','<style class="ht-marker"')
        
    def get_html(self):
        template = PageTemplate(self.context.html)
        return template(context=self.context, request=self.request, view=self)
    
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
            self.title = self.request.form.get('form.widgets.title','')
            self.description = self.request.form.get('form.widgets.description','')
            self.css = self.request.form.get('form.widgets.css','')
            self.js = self.request.form.get('form.widgets.js','')
            self.html = self.request.form.get('form.widgets.html','')
            self.suppress_title = self.request.form.get('form.widgets.suppress_title-empty-marker',False)
            self.suppress_description = self.request.form.get('form.widgets.suppress_description-empty-marker',False)
            self.set_context = self.request.form.get('form.widgets.set_context','')
    
        return self.template()

    def get_style(self):
        return self.css.replace('<style','<style class="ht-marker"')
        
    def get_html(self):
        template = PageTemplate(self.html)
        return template(context=self.set_context, request=self.request, view=self)
        
        