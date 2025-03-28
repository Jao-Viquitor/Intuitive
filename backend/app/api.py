from flask import request, Response
import json
from config import app, decimal_default
from db import get_db_connection, carregar_consulta
from flask_cors import CORS

CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'

@app.route('/api/top_operadoras', methods=['GET'])
def top_operadoras():
    periodo = request.args.get('periodo', 'ano').strip()
    trimestre = request.args.get('trimestre', '4T').strip()
    ano = request.args.get('ano', '2024').strip()
    uf = request.args.get('uf', '').strip().upper()

    conexao = get_db_connection()
    cursor = conexao.cursor(dictionary=True)

    if periodo == 'trimestre':
        query = carregar_consulta('consulta_trimestre.sql')
        params = [trimestre, ano]
    else:
        query = carregar_consulta('consulta_ano.sql')
        params = [ano]

    if uf:
        query = query.replace("GROUP BY", "AND o.uf = %s\nGROUP BY")
        params.append(uf)

    cursor.execute(query, params)
    resultados = cursor.fetchall()
    cursor.close()
    conexao.close()

    return Response(json.dumps(resultados, ensure_ascii=False, default=decimal_default),
                    content_type="application/json; charset=utf-8")


@app.route('/api/busca_operadoras', methods=['GET'])
def busca_operadoras():
    termo = request.args.get('q', '').strip()
    uf = request.args.get('uf', '').strip().upper()

    conexao = get_db_connection()
    cursor = conexao.cursor(dictionary=True)

    query = """
        SELECT registro_ans, razao_social, nome_fantasia, cnpj, uf, cidade
        FROM operadoras_ativas
        WHERE 1=1
    """
    params = []

    if termo:
        query += """
            AND (
                razao_social LIKE %s OR
                nome_fantasia LIKE %s OR
                cnpj LIKE %s
            )
        """
        params.extend([f"%{termo}%"] * 3)

    if uf:
        query += " AND uf = %s"
        params.append(uf)

    query += " ORDER BY razao_social LIMIT 10"

    cursor.execute(query, tuple(params))
    resultados = cursor.fetchall()

    cursor.close()
    conexao.close()

    return Response(json.dumps(resultados, ensure_ascii=False, default=decimal_default),
                    content_type="application/json; charset=utf-8")

if __name__ == '__main__':
    app.run(debug=True)