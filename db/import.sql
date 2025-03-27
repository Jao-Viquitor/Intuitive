USE db_intuitive;
LOAD DATA INFILE 'C:/ProgramData/MySQL/MySQL Server 8.0/Uploads/Relatorio_cadop.csv'
    INTO TABLE operadoras_ativas
    CHARACTER SET utf8mb4
    FIELDS TERMINATED BY ';' ENCLOSED BY '"'
    IGNORE 1 LINES
    (Registro_ANS, CNPJ, Razao_Social, Nome_Fantasia, Modalidade, Endereco, Numero, Complemento, Bairro, Cidade, UF, CEP, DDD, Telefone, Fax, email, Representante, Cargo_Representante, regiao_comercializacao, @data_registro)
    SET data_registro = STR_TO_DATE(@data_registro, '%Y-%m-%d');