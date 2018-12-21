Tarefas = db.define_tables('tarefas',
                           Field('titulo', 'string', label='Título'),
                           Field('status', 'boolean', label='Tarefa concluída',
                                 default=False),
                           auth.signature,
                           format='%(titulo)s')