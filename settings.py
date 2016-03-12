import os
import tornado.template

path = lambda root,*a: os.path.join(root, *a)
ROOT = os.path.dirname(os.path.abspath(__file__))

TEMPLATE_ROOT = path(ROOT, 'templates')
STATIC_ROOT = path(ROOT, 'static')

settings = {
    'template_loader': tornado.template.Loader(TEMPLATE_ROOT),
    'static_path': STATIC_ROOT
}
