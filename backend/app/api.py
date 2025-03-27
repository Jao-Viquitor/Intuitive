from flask import request, Response
import json
from config import app, decimal_default
from db import get_db_connection, carregar_consulta

@app.route('/api/top_operadoras', methods=['GET'])
def top_operadoras():
    periodo = request.args.get('periodo', 'ano').strip()
    trimestre = request.args.get('trimestre', '4T').strip()
    ano = request.args.get('ano', '2024').strip()

    conexao = get_db_connection()
    cursor = conexao.cursor(dictionary=True)

    if periodo == 'trimestre':
        query = carregar_consulta('consulta_trimestre.sql')
        params = (trimestre, ano)
    else:
        query = carregar_consulta('consulta_ano.sql')
        params = (ano,)

    cursor.execute(query, params)
    resultados = cursor.fetchall()
    cursor.close()
    conexao.close()

    return Response(json.dumps(resultados, ensure_ascii=False, default=decimal_default), content_type="application/json; charset=utf-8")

@app.route('/api/busca_operadoras', methods=['GET'])
def busca_operadoras():
    termo = request.args.get('q', '').strip()
    conexao = get_db_connection()
    cursor = conexao.cursor(dictionary=True)

    query = """
        SELECT registro_ans, razao_social, nome_fantasia, cnpj, uf, cidade
        FROM operadoras_ativas
        WHERE razao_social LIKE %s OR nome_fantasia LIKE %s
        LIMIT 10;
    """
    params = (f"%{termo}%", f"%{termo}%")

    cursor.execute(query, params)
    resultados = cursor.fetchall()

    cursor.close()
    conexao.close()

    return Response(json.dumps(resultados, ensure_ascii=False), content_type="application/json; charset=utf-8")

if __name__ == '__main__':
    app.run(debug=True)