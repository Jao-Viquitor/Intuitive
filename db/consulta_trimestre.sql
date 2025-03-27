-- Consultas por trimestre
SELECT
    o.registro_ans,
    o.razao_social,
    o.nome_fantasia,
    o.cnpj,
    SUM(d.vl_saldo_final) AS total_despesa
FROM demonstracoes_contabeis d
         JOIN operadoras_ativas o ON d.reg_ans = o.registro_ans
WHERE d.descricao = 'EVENTOS/ SINISTROS CONHECIDOS OU AVISADOS  DE ASSISTÊNCIA A SAÚDE MEDICO HOSPITALAR '
  AND d.trimestre = %s
  AND d.ano = %s
GROUP BY o.registro_ans, o.razao_social, o.nome_fantasia, o.cnpj
ORDER BY total_despesa DESC
LIMIT 10;