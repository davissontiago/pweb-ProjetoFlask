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
            if id:
                cursor.execute('UPDATE professor SET nome = %s, disciplina =%s WHERE id =%s', (name, subject, id))
            else:
                cursor.execute('INSERT INTO professor (nome, disciplina) VALUES (%s, %s)', (name, subject))
            conn.commit()
            return {"status": "ok"}
        except Exception as e:
            return {"status": "erro", "mensagem": f"Erro: {str(e)}"}
        finally:
            conn.close()
            
    def get_by_id(self, id):
        conn = get_connection() 
        cursor = conn.cursor() 
        cursor.execute('SELECT id, nome, disciplina FROM professor WHERE id = %s', (id,))
        record = cursor.fetchone()
        conn.close()
        return record
    
    def delete(self, id):
        conn = get_connection() 
        cursor = conn.cursor() 
        try:
            cursor.execute('DELETE FROM professor WHERE id = %s', (id,))
            conn.commit()
            return {"status": "ok"}
        except Exception as e:
            return {"status": "erro", "mensagem": f"Erro: {str(e)}"}
        finally:
            conn.close()