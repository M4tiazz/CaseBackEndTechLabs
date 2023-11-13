-- CRIANDO O BANCO DE DADOS
CREATE DATABASE api_crud;

-- Criação tabela PESSOAS;
CREATE TABLE pessoas (
	id int not null auto_increment,
	nome_completo varchar(50) not null,
    data_nascimento date not null,
    endereço varchar(200) not null,
	cpf varchar(15) not null,
    estado_civil varchar(20) not null,
    primary key(id)
 );
