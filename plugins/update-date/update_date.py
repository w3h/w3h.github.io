# -*- encoding: UTF-8 -*-
# @author: wilbur.ma@foxmail.com
# @date: 2013-10-11
# @license: BSD 3-Clause Licencse
'''
A simple pelican plugin which can
    1) use the value of `update' metadata as update date
    2) use filesystem's mtime value as update date if the `update' metadata is not defined
    3) save a list of articles ordered descending by update date in the global pelican context

New variables:
    1) article.updatedate
    2) page.updatedate
    3) context.articles_updatedate
'''

import os, logging
from datetime import datetime
from pelican import signals
from pelican.utils import get_date

class UpdateDateArticleListGenerator(object):
    '''This generator insert a list of articles ordered descending
    by update date into the global pelican context.
    '''
    def __init__(self, context, path, *arguments, **keywords):
        self.context = context

    def generate_context(self):
        self.context['articles_updatedate'] = sorted([article for article in self.context['articles'] if hasattr(article, "updatedate")],
                key=lambda x: x.updatedate, reverse=True)

def set_update_date(content):
    '''read `update' metadata or filesysystem's mtime
    '''

    if not content._context:
        return

    for k, v in content.metadata.items():
        if "update" == k.lower():
            content.updatedate = get_date(v)
            return

    if 'UPDATEDATE_MODE' in content.settings and content.settings['UPDATEDATE_MODE'] == 'metadata':
        return

    if 'UPDATE_LOCALE_TO_CREATE_TIME' in content.settings and content.settings['UPDATE_LOCALE_TO_CREATE_TIME']:
        content.locale_date = datetime.fromtimestamp(os.path.getctime(content.source_path))
        content.locale_date = content.locale_date.replace(microsecond = 0)

    try:
        content.updatedate = datetime.fromtimestamp(os.path.getmtime(content.source_path))
        content.updatedate = content.updatedate.replace(microsecond = 0)
        #content.date = content.updatedate
    except os.error:
        logging.error("{} not exists or not readable".format(content.source_path))

def register():
    signals.content_object_init.connect(set_update_date)

def get_generators(generators):
    return UpdateDateArticleListGenerator
      
def register():
    signals.content_object_init.connect(set_update_date)
    signals.get_generators.connect(get_generators)

