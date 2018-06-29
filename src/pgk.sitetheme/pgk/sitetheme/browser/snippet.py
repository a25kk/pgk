# -*- coding: utf-8 -*-
"""Module providing content page snippets"""
from Acquisition import aq_inner
from Products.Five.browser import BrowserView
from plone import api

from ade25.sitecontent.contentpage import IContentPage


class SnippetView(BrowserView):
    """ Embeddable preview card for content pages """

    def has_image(self):
        context = aq_inner(self.context)
        try:
            lead_img = context.image
        except AttributeError:
            lead_img = None
        if lead_img is not None:
            return True
        return False


class SnippetPreview(BrowserView):
    """Preview embeddable content page preview cards"""

    def __call__(self):
        return self.render()

    def render(self):
        return self.index()

    def rendered_snippet(self):
        context = aq_inner(self.context)
        template = context.restrictedTraverse('@@snippet-view')()
        return template
