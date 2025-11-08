from dao.db_config  import get_connection 

class StudentDAO: 

    sqlSelect = 'SELECT id, nome, idade, cidade FROM aluno'

    def get_all(self): 
        conn = get_connection() 
        cursor = conn.cursor() 
        cursor.execute(self.sqlSelect) 
        rows = cursor.fetchall() 
        conn.close() 
        return rows
    
    def save(id=None, self, name, age, city):
        conn = get_connection()
        cursor = conn.cursor()
        try:            
            cursor.execute('INSERT INTO aluno (nome, idade, cidade) VALUES (%s, %s, %s)', (name, age, city))
            conn.commit()
            return {"status": "ok"}
        except Exception as e:
            return {"status": "erro", "mensagem": f"Erro: {str(e)}"}
        finally:
            conn.close()
