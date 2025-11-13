from dao.db_config  import get_connection 

class TeacherDAO: 

    sqlSelect = 'SELECT id, nome, disciplina FROM professor ORDER BY id ASC'

    def get_all(self): 
        conn = get_connection() 
        cursor = conn.cursor() 
        cursor.execute(self.sqlSelect) 
        rows = cursor.fetchall() 
        conn.close() 
        return rows
    
    def save(self, name, subject, id=None):
        conn = get_connection()
        cursor = conn.cursor()
        try:            
            cursor.execute('INSERT INTO professor (nome, disciplina) VALUES (%s, %s)', (name, subject))
            conn.commit()
            return {"status": "ok"}
        except Exception as e:
            return {"status": "erro", "mensagem": f"Erro: {str(e)}"}
        finally:
            conn.close()