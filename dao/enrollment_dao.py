from dao.db_config  import get_connection 

class EnrollmentDAO: 

    sqlSelect = 'SELECT m.id, t.semestre, a.nome AS nome_aluno, c.nome_curso, p.nome AS nome_professor, p.disciplina FROM matricula AS m JOIN aluno AS a ON m.aluno_id = a.id JOIN turma AS t ON m.turma_id = t.id JOIN curso AS c ON t.curso_id = c.id JOIN professor AS p ON t.professor_id = p.id ORDER BY m.id ASC;'

    def get_all(self):
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute(self.sqlSelect)
        rows = cursor.fetchall()
        conn.close()
        return rows

    def save(self, student_id, class_id, id=None):
        conn = get_connection()
        cursor = conn.cursor()
        try:
            if id:
                # Edição: Atualiza o aluno ou a turma da matrícula
                cursor.execute('UPDATE matricula SET aluno_id=%s, turma_id=%s WHERE id=%s', (student_id, class_id, id))
            else:
                # Criação: Cria nova matrícula ligando aluno e turma
                cursor.execute('INSERT INTO matricula (aluno_id, turma_id) VALUES (%s, %s)', (student_id, class_id))
            conn.commit()
            return {"status": "ok"}
        except Exception as e:
            return {"status": "erro", "mensagem": f"Erro: {str(e)}"}
        finally:
            conn.close()

    def get_by_id(self, id):
        conn = get_connection()
        cursor = conn.cursor()
        # Busca os IDs brutos para pré-selecionar nos dropdowns do formulário
        cursor.execute('SELECT id, aluno_id, turma_id FROM matricula WHERE id = %s', (id,))
        record = cursor.fetchone()
        conn.close()
        return record

    def delete(self, id):
        conn = get_connection()
        cursor = conn.cursor()
        try:
            cursor.execute('DELETE FROM matricula WHERE id = %s', (id,))
            conn.commit()
            return {"status": "ok"}
        except Exception as e:
            return {"status": "erro", "mensagem": f"Erro: {str(e)}"}
        finally:
            conn.close()