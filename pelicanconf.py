#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'W3H'
SITENAME = u"工匠安全实验室 | 专注于工控安全"
SITEURL = "http://icsmaster.com"
#SITEURL = 'http://0.0.0.0:8080'

# 时间日期设置
TIMEZONE = 'Asia/Shanghai'
DEFAULT_DATE = 'fs'  # use filesystem's mtime
DATE_FORMATS = {
        'zh_CN': '%Y-%m-%d %H:%M:%S',
}
DEFAULT_DATE_FORMAT = '%Y-%m-%d %H:%M:%S'
FALLBACK_ON_FS_DATE = True
SITELOGO = 'logo.png'
HIDE_SITENAME = True
SITELOGO_SIZE_W = 40
SITELOGO_SIZE_H = 40

# 文章格式设置
DEFAULT_LANG = u'ch'
DEFAULT_PAGINATION = 8
SUMMARY_MAX_LENGTH = 15
FILENAME_METADATA = '(?P<slug>.*)'
RELATIVE_URLS = True

# 最新日志个数
RECENT_POST_COUNT= 10

# use directory name as category if not set
USE_FOLDER_AS_CATEGORY = True
DEFAULT_CATEGORY = '未分类'

# 静态目录和页面设置
EXTRA_PATH_METADATA = {
        'extra/favicon.ico' : { 'path': 'favicon.ico' },
        'extra/robots.txt' : { 'path': 'robots.txt' },
        'extra/logo.png' : { 'path': 'logo.png' },
}

STATIC_PATHS = [
    'static',    
    'extra/robots.txt',
    'extra/favicon.ico',
    'extra/logo.png',
    ]

ARTICLE_URL = '{category}/{slug}.html'
ARTICLE_SAVE_AS = ARTICLE_URL
PAGE_URL = '{slug}.html'
PAGE_SAVE_AS = PAGE_URL
CATEGORY_URL = 'category/{slug}.html'
CATEGORY_SAVE_AS = CATEGORY_URL
CATEGORIES_SAVE_AS = 'category/index.html'
TAG_URL = 'tag/{slug}.html'
TAG_SAVE_AS = TAG_URL
TAGS_SAVE_AS = 'tag/index.html'
ARCHIVES_SAVE_AS = 'archives.html'  # The location to save the article archives page.
YEAR_ARCHIVE_SAVE_AS = False    # The location to save per-year archives of your posts.
MONTH_ARCHIVE_SAVE_AS = False   # The location to save per-month archives of your posts.
DAY_ARCHIVE_SAVE_AS = False # The location to save per-day archives of your posts.

# disable author pages
AUTHOR_URL = 'author/{slug}.html'
AUTHOR_SAVE_AS = 'author/{slug}.html'
AUTHORS_SAVE_AS = ''

# Tag_Cloud Config
TAG_CLOUD_STEPS = 4 # Count of different font sizes in the tag cloud.
TAG_CLOUD_MAX_ITEMS = 100  # Maximum number of tags in the cloud.

# Feed generation is usually not desired when developing
# feed config
FEED_DOMAIN = SITEURL
FEED_ALL_RSS = 'feed.xml'
FEED_MAX_ITEMS = 20
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None

# Blogroll
LINKS =  ( 
            ('DRAGONCON', 'http://dragoncon.hk/'),
            ('独自等待', 'http://www.waitalone.cn/'),
            ('灯塔实验室', 'http://plcscan.org/blog/'),
         )

# Social widget
# SOCIAL = (('You can add links in your config file', '#'),
#           ('Another social link', '#'),)


# JiaThis
JIATHIS_PROFILE = True #分享图标

# Theme Config
THEME = 'themes/bootstrap3' # 不错

# 配置方案
#BOOTSTRAP_THEME = 'cerulean'

# 设置主题格式
PYGMENTS_STYLE = 'emacs'
DISPLAY_RECENT_POSTS_ON_SIDEBAR = True
MENUITEMS = (
                ('首页',SITEURL+'/index.html'),
                ('最新资讯',SITEURL+'/category/news.html'),
                ('安全研究',SITEURL+'/category/security.html'),
                ('开源工具',SITEURL+'/category/tool.html'),
                ('工控安全导航',SITEURL+'/nav.html'),        
                ('关于我们',SITEURL+'/other/about.html'),
            )

DISPLAY_PAGES_ON_MENU = True
# DISPLAY_BREADCRUMBS = True
DISPLAY_CATEGORIES_ON_SIDEBAR = True
DISPLAY_TAGS_ON_SIDEBAR = False
DISPLAY_HIGH = True
DISPLAY_CATEGORIES_ON_MENU = False

PLUGIN_PATHS = [u"plugins",]
PLUGINS = ["sitemap", "random_article", "update-date", "neighbors","code_include"] #"gzip_cache"]

# 配置sitemap 插件
SITEMAP = {
    "format": "xml",
    "priorities": {
        "articles": 0.5,
        "indexes": 0.5,
        "pages": 0.5,
    },
    "changefreqs": {
        "articles": "monthly",
        "indexes": "daily",
        "pages": "monthly",
    }
}

# 配置 random_article 插件
RANDOM = "random.html"
DISPLAY_RANDOM = False

# 配置 neighbors 插件
DISPLAY_NEIGHBORS = True

# 配置评论
#DISQUS_SITENAME = "w3h"
UYAN_SITENAME = 'w3h'

NETEASE_SITENAME = True

# 配置Google Analiytics
#GOOGLE_ANALYTICS_UNIVERSAL = r'UA-50980139-1'
#GOOGLE_ANALYTICS_UNIVERSAL_PROPERTY = r'webhhh.net'

# 配置BAIDU Analiytics
BAIDU_ANALYTICS_UNIVERSAL = r'w3h'

# 显示作者
SHOW_ARTICLE_AUTHOR = True

# Github配置
GITHUB_USER = 'w3h'

# 以创建时间更新Date
UPDATE_LOCALE_TO_CREATE_TIME = True

