# -*- coding: utf-8 -*-

# ---- index page ----
def index():
    tarefas = db(Tarefas.id>0).select()
    return dict(tarefas=tarefas)

# ---- crud da tabela Tarefas ----
def crud_tarefa():
    '''
    Esta action, faz um crud completo para a tabela "Tarefas"
    '''
    tarefa  = request.args(0)
    if tarefa:
        form = SQLFORM(Tarefas, tarefa, showid=False, deletable=True)
    else:
        form = SQLFORM(Tarefas)
    if form.process().accepted:
        session.flash = "Tarefa criada/editada"                     
        redirect(URL('default', 'index'))
    elif form.errors:
        response.flash = "Erro ao cadastrar!"
    return dict(form=form)

# ---- Action for login/register/etc (required for auth) -----
def user():
    """
    exposes:
    http://..../[app]/default/user/login
    http://..../[app]/default/user/logout
    http://..../[app]/default/user/register
    http://..../[app]/default/user/profile
    http://..../[app]/default/user/retrieve_password
    http://..../[app]/default/user/change_password
    http://..../[app]/default/user/bulk_register
    use @auth.requires_login()
        @auth.requires_membership('group name')
        @auth.requires_permission('read','table name',record_id)
    to decorate functions that need access control
    also notice there is http://..../[app]/appadmin/manage/auth to allow administrator to manage users
    """
    return dict(form=auth())

# ---- action to server uploaded static content (required) ---
@cache.action()
def download():
    """
    allows downloading of uploaded files
    http://..../[app]/default/download/[filename]
    """
    return response.download(request, db)
