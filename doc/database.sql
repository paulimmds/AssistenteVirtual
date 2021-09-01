# Script para criação do BD e suas tabelas

create database QDEZ ;

use QDEZ;

create table MEMBRO (
CPF_Membro Varchar(12) Primary Key Not Null,
Nome Varchar(32) Not Null,
Tipo_Quarto Boolean Not Null, 
Estado_Presenca Boolean Not Null
);

create table CONTA (
ID_Conta smallInt Primary Key Not Null Auto_Increment,
Data_Referencia Date Not Null,
Aluguel Decimal(6,2),
Job Decimal(6,2),
Caixa   Decimal(6,2) ,
Agua   Decimal(6,2) ,
Energia   Decimal(6,2) ,
Gas   Decimal(6,2) ,
Vivo   Decimal(6,2) ,
Poupanca   Decimal(6,2) ,
Cacau   Decimal(6,2) ,
Descontos  Decimal(6,2) 
);

create table MERCADO (
ID_Mercado  SmallInt Primary Key Not Null Auto_Increment ,
ID_Conta smallInt Not Null ,
Descricao  Varchar(100) ,
Valor  Decimal (6,2) Not Null,

Foreign Key (ID_Conta) References CONTA(ID_Conta)
);

create table OUTROS_GASTOS (
ID_OutrosGastos  SmallInt Primary Key Not Null Auto_Increment ,
ID_Conta  smallInt Not Null ,
Valor  Decimal (6,2) ,
Descricao  Varchar(100),

Foreign Key (ID_Conta) references CONTA(ID_Conta)
);

create table DESCONTOS (
ID_Desconto  SmallInt Primary Key Not Null Auto_Increment ,
ID_Conta  smallInt Not Null ,
Valor  Decimal (6,2) Not Null,
Descricao  Varchar(100),

foreign key (ID_Conta) references CONTA(ID_Conta)
);

create table MENSALIDADE(
ID_Mensalidade  smallInt Primary Key Not Null Auto_Increment ,
ID_Conta  smallInt Not Null ,
CPF_Membro  varchar(12) Not Null ,
Data_Pagamento  Date Not Null ,
Valor  Decimal(6,2) Not Null ,
Observacao  varChar(100),

foreign key (ID_Conta) references CONTA(ID_Conta),
foreign key (CPF_Membro) references MEMBRO(CPF_Membro)
);

create table TIPO_FORMS (
ID_Tipo smallint Primary Key Not Null auto_increment,
Tipo Varchar(12)
);

create table FORMS (
ID_Forms  smallInt Primary Key Not Null Auto_Increment ,
CPF_Membro  Varchar(12) ,
ID_Tipo  smallInt  ,
ID_Conta  smallInt ,
Data_Pagamento  Date ,
Valor  Decimal(6,2) ,

foreign key (CPF_Membro) references MEMBRO(CPF_Membro),
foreign key (ID_Tipo) references TIPO_FORMS(ID_Tipo),
foreign key (ID_Conta) references CONTA(ID_Conta)
);

create table VARIAVEL (
ID_Variavel smallInt Primary Key Not Null Auto_Increment ,
PQP_IND Decimal(3,2),
PQP_COMP Decimal(3,2),
MP_Aluguel Decimal(3,2),
MP_Job Decimal(3,2),
MP_Caixa Decimal(3,2),
MP_Agua Decimal(3,2),
MP_Energia Decimal(3,2),
MP_Gas Decimal(3,2),
MP_Mercado Decimal(3,2),
MP_Vivo Decimal(3,2),
MP_Poupanca Decimal(3,2),
MP_Cacau Decimal(3,2),
MP_OutrosGastos Decimal(3,2)
);