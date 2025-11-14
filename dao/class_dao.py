from dao.db_config  import get_connection 

class ClassDAO: 

    sqlSelect = 'SELECT t.id, t.semestre, c.nome_curso, p.nome FROM turma AS t JOIN professor AS p ON t.professor_id = p.id JOIN curso AS c ON t.curso_id = c.id ORDER BY id ASC'

    def get_all(self): 
        conn = get_connection() 
        cursor = conn.cursor() 
        cursor.execute(self.sqlSelect) 
        rows = cursor.fetchall() 
        conn.close() 
        return rows
    
    def save(self, semester, course_id, teacher_id, id=None):
        conn = get_connection()
        cursor = conn.cursor()
        try:
            if id:
                cursor.execute('UPDATE turma SET semestre =%s, curso_id = %s, professor_id =%s WHERE id =%s', (semester, course_id, teacher_id, id))
            else:          
                cursor.execute('INSERT INTO turma (semestre, curso_id, professor_id) VALUES (%s, %s, %s)', (semester, course_id, teacher_id))
            conn.commit()
            return {"status": "ok"}
        except Exception as e:
            return {"status": "erro", "mensagem": f"Erro: {str(e)}"}
        finally:
            conn.close()
            
    def get_by_id(self, id):
        conn = get_connection() 
        cursor = conn.cursor() 
        cursor.execute('SELECT id, semestre, curso_id, professor_id FROM turma WHERE id = %s', (id,))
        record = cursor.fetchone()
        conn.close()
        return record
    
    def delete(self, id):
        conn = get_connection() 
        cursor = conn.cursor() 
        try:
            cursor.execute('DELETE FROM turma WHERE id = %s', (id,))
            conn.commit()
            return {"status": "ok"}
        except Exception as e:
            return {"status": "erro", "mensagem": f"Erro: {str(e)}"}
        finally:
            conn.close()