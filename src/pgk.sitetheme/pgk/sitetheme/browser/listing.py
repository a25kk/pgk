# -*- coding: utf-8 -*-
"""Module providing views for the site navigation root"""
from Acquisition import aq_inner
from Products.Five.browser import BrowserView
from plone import api

from ade25.sitecontent.contentpage import IContentPage


class ListingView(BrowserView):
    """ General purpose front page view """

    def __call__(self):
        self.has_previews = len(self.snippets()) > 0
        return self.render()

    def render(self):
        return self.index()

    def snippets(self):
        preview_items = self.preview_items()
        snippets = list()
        for item in preview_items:
            item_obj = item.getObject()
            item_size = getattr(item_obj, 'elementSize', '100')
            snippets.append({
                'uuid': item.UID,
                'title': item.Title,
                'item_size': item_size,
                'template': item_obj.restrictedTraverse(
                    '@@snippet-view')()
            })
        return snippets

    def preview_items(self):
        context = aq_inner(self.context)
        items = api.content.find(
            context=context,
            depth=1,
            object_provides=IContentPage.__identifier__,
            review_state='published',
            sort_on='getObjPositionInParent')
        return items
