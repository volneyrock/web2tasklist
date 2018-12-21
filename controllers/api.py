@request.restful()
def rest():
    '''
    Action principal para API REST
    '''
    def GET(table_name, **vars):
        if not request.vars.id:
            tarefas = db(Tarefas.id).select()
            return response.json({'status':'success', 'tarefa':tarefas})
        elif table_name == 'tarefas':
            return response.json({'status':'success', 'tarefa':db.tarefas(**vars)})
        else:
            raise HTTP(400)
        
    def POST(table_name, **fields):
        if table_name:
            return db[tablename].validate_and_insert(**fields)
        else:
            raise HTTP(400)

    def PUT(table_name,record_id,**vars):
        return db(db[tablename]._id==record_id).update(**vars)
    
    def DELETE(table_name,record_id):
        return db(db[table_name]._id==record_id).delete()

    return locals()
