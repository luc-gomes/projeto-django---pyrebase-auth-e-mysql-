show databases;

create database conteudo_site;

use conteudo_site;

show tables;

create table autores (
    codigo_autor int not null auto_increment,
    nome varchar (20),
    sobrenome varchar (30),
    email varchar (60),
    primary key (codigo_autor) 
);

 select * from autores;
 
create table conteudos (
    codigo_pb int auto_increment,
    titulo varchar(60) not null,
    subtitulo varchar (60),
    texto varchar (5000) not null,
    data_pub date,
    visibilidade boolean,
    codigo_autor int,
    primary key (codigo_pb)
);
 show tables;
alter table conteudos
add    foreign key (codigo_autor) references autores(codigo_autor);

describe conteudos;

select * from conteudos;

select * from autores;
