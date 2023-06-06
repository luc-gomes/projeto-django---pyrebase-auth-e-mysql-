

show databases;
use conteudo_site;

select * from autores;
select * from conteudos;

SELECT c.codigo_pb, c.titulo, c.subtitulo, c.texto, c.visibilidade, a.nome, a.sobrenome, a.email
FROM conteudos c
INNER JOIN autores a
ON c.codigo_autor = a.codigo_autor;