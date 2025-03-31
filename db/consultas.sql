SELECT
    o.registro_ans,
    o.razao_social,
    o.nome_fantasia,
    o.cnpj,
    SUM(d.vl_saldo_final) AS total_despesa
FROM demonstracoes_contabeis d
         JOIN operadoras_ativas o ON d.reg_ans = o.registro_ans
WHERE d.descricao = 'EVENTOS/ SINISTROS CONHECIDOS OU AVISADOS  DE ASSISTÊNCIA A SAÚDE MEDICO HOSPITALAR '
  AND d.trimestre = '4T'
  AND d.ano = 2024
GROUP BY o.registro_ans, o.razao_social, o.nome_fantasia, o.cnpj
ORDER BY total_despesa DESC
LIMIT 10;

SELECT
    o.registro_ans,
    o.razao_social,
    o.nome_fantasia,
    o.cnpj,
    SUM(d.vl_saldo_final) AS total_despesa
FROM demonstracoes_contabeis d
         JOIN operadoras_ativas o ON d.reg_ans = o.registro_ans
WHERE d.descricao = 'EVENTOS/ SINISTROS CONHECIDOS OU AVISADOS  DE ASSISTÊNCIA A SAÚDE MEDICO HOSPITALAR '
  AND d.ano = 2024
GROUP BY o.registro_ans, o.razao_social, o.nome_fantasia, o.cnpj
ORDER BY total_despesa DESC
LIMIT 10;

CREATE INDEX idx_demo_reg_ans ON demonstracoes_contabeis(reg_ans);
CREATE INDEX idx_demo_ano ON demonstracoes_contabeis(ano);
CREATE INDEX idx_demo_trimestre ON demonstracoes_contabeis(trimestre);
CREATE INDEX idx_demo_descricao ON demonstracoes_contabeis(descricao);

CREATE INDEX idx_op_uf ON operadoras_ativas(uf);
CREATE INDEX idx_op_razao_social ON operadoras_ativas(razao_social);
CREATE INDEX idx_op_nome_fantasia ON operadoras_ativas(nome_fantasia);
CREATE INDEX idx_op_cnpj ON operadoras_ativas(cnpj);
