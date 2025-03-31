COPY demonstracoes_contabeis(data, reg_ans, cd_conta_contabil, descricao, vl_saldo_inicial, vl_saldo_final, trimestre, ano)
FROM PROGRAM 'cat /../dados/demonstracoes_contabeis/demonstracoes_contabeis_completo.csv'
WITH (FORMAT csv, HEADER true, DELIMITER ';', ENCODING 'UTF8');

COPY operadoras_ativas(id_operadora, registro_ans, cnpj, razao_social, nome_fantasia, modalidade, endereco, numero,
                       complemento, bairro, cidade, uf, cep, ddd, telefone, fax, email, representante,
                       cargo_representante, regiao_comercializacao, data_registro)
FROM PROGRAM 'cat /../dados/operadoras_ativas/operadoras_ativas_limpo.csv'
WITH (FORMAT csv, HEADER true, DELIMITER ',', ENCODING 'UTF8');
