show databases;

use conteudo_site;

show tables;
describe conteudos;
describe autores;

--populando banco de dados

insert into autores(codigo_autor, nome,sobrenome,email) values
(1, 'Lucas', 'Silva', 'lucas@gmail.com');
insert into autores(codigo_autor, nome,sobrenome,email) values
(2, 'Lucas', 'gomes', 'lucas1@gmail.com');

select* from conteudos;

insert into conteudos(codigo_pb,titulo, subtitulo, texto, visibilidade, codigo_autor)
values(1,'teste','teste','teste, teste, teste', true, 1);
insert into conteudos(codigo_pb,titulo, subtitulo, texto, visibilidade, codigo_autor)
values(2,'ANÁLISE E DESENVOLVIMENTO DE SISTEMAS','curso de ti','A matemática, em especial raciocínio lógico e cálculo,a para que o aluno aprenda a otimizar computadores e a desenvolver softwareses sobre Bancos de Dados, sistemas baseados em web (como serviços bancários pela internet) e programação distribuída, que conecta computadores em rede para que funcionem como se fossem um só computador.Administração, contabilidade, economia, estatística e inglês também fazem parte do currículo. Além disso, habilidades para leitura e interpretação de textos são fundamentais para o aprendizado durante o curso. Hoje, o mercado não aceita mais profissionais que se isolam na frente do computador. As empresas exigem pessoas versáteis, dinâmicas, que saibam trabalhar em equipe e possam ter contato com o usuário final do sistema.', true, 1);
insert into conteudos(codigo_pb,titulo, subtitulo, texto, visibilidade, codigo_autor)
values(3,'Engenharia de Software III','manha','Conceitos, evolução e importância de arquitetura de software Padrões de Arquitetura. Padrões de Distribuição. Camadas no desenvolvimento de souitetura de Software. Visões na arquire. Modelo de Análise e Projetos. Formas de representação. O processo de desenvolvimento. Mapeamento para implementação. Integração do sistema. Testes: planejamento e tipos. Manutenção. Documentação.', true, 1);
insert into conteudos(codigo_pb, titulo, subtitulo, texto, visibilidade, codigo_autor)
values(4,'DISCIPLINA: GESTÃO E GOVERNANÇA DE TECNOLOGIA DA INFORMAÇÃO (4 AULAS SEMANAIS)','manha','Conhecer as técnicas e ferramentas para desenvolvimento de Gestão de TI.', true, 1);
insert into conteudos(codigo_pb, titulo, subtitulo, texto, visibilidade, codigo_autor)
values(5,'DISCIPLINA: INTERAÇÃO HUMANO COMPUTADOR ','ihc','Aplicar os conceitos de usabilidade de software', true, 1);
insert into conteudos(codigo_pb,titulo, subtitulo, texto, visibilidade, codigo_autor)
values(7,'ALGORITMOS E LÓGICA DE PROGRAMAÇÃO','logica','Analisar problemas computacionais e projetar soluções por meio da construção de algoritmos', true, 1);
insert into conteudos(codigo_pb,titulo, subtitulo, texto, visibilidade, codigo_autor)
values(8,'DISCIPLINA: GESTÃO DE EQUIPES (2 AULAS SEMANAIS)','teste','Entender os aspectos de gerência de pessoas em equipes de trabalho com foco em resultados.', true, 1);
insert into conteudos(codigo_pb,titulo, subtitulo, texto, visibilidade, codigo_autor)
values (9,'Introdução à Linguagem C','teste','Um programa em C é composto por um conjunto de Funções. A função pela qual o programa começa a ser executado chama-se main. Após cada cada comando em C deve-se colocar um ; (ponto-e-vírgula). Um programa em C deve ser Identado para que possa ser lido com mais facilidade.', true, 1);
insert into conteudos(codigo_pb,titulo, subtitulo, texto, visibilidade, codigo_autor)
values(10,'As tendências da ficção contemporânea no Brasil e no mundo','teste','Zé foi ao mercado comprar pão, mas esqueceu o dinheiro em casa. Ele tentou pagar com um abraço, mas o padeiro não aceitou. Então, ele pegou o pão e saiu correndo. O padeiro ficou furioso e gritou: "Volte aqui, seu ladrão de pão!" Mas Zé já estava longe, comendo o pão e rindo da situação. Ele pensou: "Que sorte que eu tenho! Consegui um pão de graça e ainda dei um abraço no padeiro!" Mas ele não sabia que o pão estava estragado e que ele ia passar mal depois.', true, 1);
insert into conteudos(codigo_pb,titulo, subtitulo, texto, visibilidade, codigo_autor)
values(11,'Ficção versus não-ficção: como diferenciar e apr','teste','Zé foi ao mercado comprar pão, mas esqueceu o dinheiro em casa. Ele tentou pagar com um abraço, mas o padeiro não aceitou. Então, ele pegou o pão e saiu correndo. O padeiro ficou furioso e gritou: "Volte aqui, seu ladrão de pão!" Mas Zé já estava longe, comendo o pão e rindo da situação. Ele pensou: "Que sorte que eu tenho! Consegui um pão de graça e ainda dei um abraço no padeiro!" Mas ele não sabia que o pão estava estragado e que ele ia passar mal depois.', true, 1);
insert into conteudos(codigo_pb,titulo, subtitulo, texto, visibilidade, codigo_autor)
values(12,'Ficção interativa: como participar da criação de umva','teste','Zé foi ao mercado comprar pão, mas esqueceu o dinheiro em casa. Ele tentou pagar com um abraço, mas o padeiro não aceitou. Então, ele pegou o pão e saiu correndo. O padeiro ficou furioso e gritou: "Volte aqui, seu ladrão de pão!" Mas Zé já estava longe, comendo o pão e rindo da situação. Ele pensou: "Que sorte que eu tenho! Consegui um pão de graça e ainda dei um abraço no padeiro!" Mas ele não sabia que o pão estava estragado e que ele ia passar mal depois.', true, 1);
insert into conteudos(codigo_pb,titulo, subtitulo, texto, visibilidade, codigo_autor)
values(13,'As principais características da ficção literária','teste','Zé foi ao mercado comprar pão, mas esqueceu o dinheiro em casa. Ele tentou pagar com um abraço, mas o padeiro não aceitou. Então, ele pegou o pão e saiu correndo. O padeiro ficou furioso e gritou: "Volte aqui, seu ladrão de pão!" Mas Zé já estava longe, comendo o pão e rindo da situação. Ele pensou: "Que sorte que eu tenho! Consegui um pão de graça e ainda dei um abraço no padeiro!" Mas ele não sabia que o pão estava estragado e que ele ia passar mal depois.', true, 1);
insert into conteudos(codigo_pb,titulo, subtitulo, texto, visibilidade, codigo_autor)
values(14,'Ficção histórica: como misturar fatos e imaginação','teste','Zé foi ao mercado comprar pão, mas esqueceu o dinheiro em casa. Ele tentou pagar com um abraço, mas o padeiro não aceitou. Então, ele pegou o pão e saiu correndo. O padeiro ficou furioso e gritou: "Volte aqui, seu ladrão de pão!" Mas Zé já estava longe, comendo o pão e rindo da situação. Ele pensou: "Que sorte que eu tenho! Consegui um pão de graça e ainda dei um abraço no padeiro!" Mas ele não sabia que o pão estava estragado e que ele ia passar mal depois.', true, 1);
insert into conteudos(codigo_pb,titulo, subtitulo, texto, visibilidade, codigo_autor)
values(15,'Ficção científica, fantasia ou realismo mágico: qual é o seu gênero preferido?','teste','Zé foi ao mercado comprar pão, mas esqueceu o dinheiro em casa. Ele tentou pagar com um abraço, mas o padeiro não aceitou. Então, ele pegou o pão e saiu correndo. O padeiro ficou furioso e gritou: "Volte aqui, seu ladrão de pão!" Mas Zé já estava longe, comendo o pão e rindo da situação. Ele pensou: "Que sorte que eu tenho! Consegui um pão de graça e ainda dei um abraço no padeiro!" Mas ele não sabia que o pão estava estragado e que ele ia passar mal depois.', true, 1);
insert into conteudos(codigo_pb,titulo, subtitulo, texto, visibilidade, codigo_autor)
values(16,'Os melhores livros de ficção de todos os tempos','teste','Zé foi ao mercado comprar pão, mas esqueceu o dinheiro em casa. Ele tentou pagar com um abraço, mas o padeiro não aceitou. Então, ele pegou o pão e saiu correndo. O padeiro ficou furioso e gritou: "Volte aqui, seu ladrão de pão!" Mas Zé já estava longe, comendo o pão e rindo da situação. Ele pensou: "Que sorte que eu tenho! Consegui um pão de graça e ainda dei um abraço no padeiro!" Mas ele não sabia que o pão estava estragado e que ele ia passar mal depois.', true, 1);
