# -*- coding: utf-8 -*-
# this file is released under public domain and you can use without limitations

# ----------------------------------------------------------------------------------------------------------------------
# this is the main application menu add/remove items as required
# ----------------------------------------------------------------------------------------------------------------------

response.menu = [
    (T('Tasklist'), False, URL('default', 'index'), []),
    (T('New task'), False, URL('default', 'crud_tarefa'), [])
]
