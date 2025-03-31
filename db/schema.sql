-- Tabela demonstracoes_contabeis
CREATE TABLE demonstracoes_contabeis
(
    id                SERIAL PRIMARY KEY,
    data              DATE,
    reg_ans           VARCHAR(20),
    cd_conta_contabil VARCHAR(50),
    descricao         VARCHAR(255),
    vl_saldo_inicial  NUMERIC(18, 2),
    vl_saldo_final    NUMERIC(18, 2),
    trimestre         VARCHAR(10),
    ano               INT
);

-- Tabela operadoras_ativas
CREATE TABLE operadoras_ativas
(
    id_operadora           SERIAL PRIMARY KEY,
    registro_ans           VARCHAR(250),
    cnpj                   VARCHAR(20),
    razao_social           VARCHAR(255),
    nome_fantasia          VARCHAR(255),
    modalidade             VARCHAR(100),
    endereco               VARCHAR(255),
    numero                 VARCHAR(255),
    complemento            VARCHAR(255),
    bairro                 VARCHAR(255),
    cidade                 VARCHAR(100),
    uf                     VARCHAR(4),
    cep                    VARCHAR(100),
    ddd                    VARCHAR(100),
    telefone               VARCHAR(50),
    fax                    VARCHAR(50),
    email                  VARCHAR(100),
    representante          VARCHAR(100),
    cargo_representante    VARCHAR(100),
    regiao_comercializacao VARCHAR(100),
    data_registro          DATE
);
