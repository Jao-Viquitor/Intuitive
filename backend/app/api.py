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

    query_base = """
        SELECT
            o.registro_ans,
            o.razao_social,
            o.nome_fantasia,
            o.cnpj,
            SUM(d.vl_saldo_final) AS total_despesa
        FROM demonstracoes_contabeis d
        JOIN operadoras_ativas o ON d.reg_ans = o.registro_ans
        WHERE d.descricao = 'EVENTOS/ SINISTROS CONHECIDOS OU AVISADOS  DE ASSISTÊNCIA A SAÚDE MEDICO HOSPITALAR '
    """
    filtros = []
    params = []

    if periodo == 'trimestre':
        filtros.append("d.trimestre = %s")
        filtros.append("d.ano = %s")
        params.extend([trimestre, ano])
    else:
        filtros.append("d.ano = %s")
        params.append(ano)

    if uf:
        filtros.append("o.uf = %s")
        params.append(uf)

    where_clause = " AND ".join(filtros)
    query_final = f"""
        {query_base}
        AND {where_clause}
        GROUP BY o.registro_ans, o.razao_social, o.nome_fantasia, o.cnpj
        ORDER BY total_despesa DESC
        LIMIT 10
    """

    with get_db_connection() as conn:
        with conn.cursor() as cursor:
            cursor.execute(query_final, params)
            rows = cursor.fetchall()

    return Response(json.dumps(rows, ensure_ascii=False, default=decimal_default),
                    content_type="application/json; charset=utf-8")



@app.route('/api/busca_operadoras', methods=['GET'])
def busca_operadoras():
    termo = request.args.get('q', '').strip()
    uf = request.args.get('uf', '').strip().upper()

    query = """
        SELECT registro_ans, razao_social, nome_fantasia, cnpj, uf, cidade
        FROM operadoras_ativas
        WHERE 1=1
    """
    params = []

    if termo:
        query += """
            AND (
                razao_social ILIKE %s OR
                nome_fantasia ILIKE %s OR
                cnpj ILIKE %s
            )
        """
        params.extend([f"%{termo}%"] * 3)

    if uf:
        query += " AND uf = %s"
        params.append(uf)

    query += " ORDER BY razao_social LIMIT 10"

    with get_db_connection() as conn:
        with conn.cursor() as cursor:
            cursor.execute(query, params)
            rows = cursor.fetchall()

    return Response(json.dumps(rows, ensure_ascii=False, default=decimal_default),
                    content_type="application/json; charset=utf-8")


if __name__ == '__main__':
    app.run(debug=True)