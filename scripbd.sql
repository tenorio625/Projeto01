create database agendamento;

create table consulta (
id int NOT NULL AUTO_INCREMENT,
paciente varchar (50) NOT NULL,
dia varchar(20),
horario varchar(10),
PRIMARY KEY(id)
);

create table paciente (
id int NOT NULL AUTO_INCREMENT,
nome varchar (50) NOT NULL,
endereço varchar (60),
cpf varchar(12),
contato varchar (12),
PRIMARY KEY(id)
);

insert into paciente(nome,endereço,cpf,contato)
values ('jonas','rua migual, numero 1340','00000000000','69987524612');

insert into consulta(paciente,dia,horario)
values ('jonas','20/03/2020','12:00');

select * from consulta order by id;
select * from paciente;

select distinct * from consulta;

delete from consulta where paciente='pedro';

delete p1 from consulta as p1, consulta as p2 where p1.id>p2.id and p1.paciente=p2.paciente;

delete p1 from paciente as p1, paciente as p2 where p1.id>p2.id and p1.nome=p2.nome;

delete from consulta;
delete from paciente;

ALTER TABLE consulta AUTO_INCREMENT = 1;  
ALTER TABLE paciente AUTO_INCREMENT = 1; 
