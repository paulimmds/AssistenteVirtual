# AssistenteVirtual
Assistente Virtual para a Rep Quase 10 - Criado com Python + Telegram API + MySql


## Objetivo :
Administrar de forma centralizada o gerenciamento das contas da casa, formulários de pagamentos e mensalidades.

## Regras de Negócio :
	- O bot será executado no Telegram.
	- O bot usará o MYSQL para armazenamento das informações. 
	
	- Só pode haver um membro cadastrado com o mesmo CPF
	- Não pode haver dois registro de conta com o mesmo mês/ano
	- Um membro paga várias mensalidades
	- Um membro só paga uma mensalidade com a mesma data de referência
	- Um membro cria vários forms
	- Uma conta compõe vários forms
	- Um forms só é composto por uma instância de conta e por uma instância de membro
	- Haverá uma Entidade Variáveis com os valores de PQP e MP que serão usados para o cálculo da mensalidade

## Requisitos do Bot:
	- Manipular Membros
		- Cadastrar Membro
		- Deletar Membro
		- Editar Informações de um Membro
	- Manipular Contas
		- Cadastrar um registro de Conta
		- Deletar registro de Conta
		- Editar registro de Conta
	- Mensalidade
		- Prover Mensalide de um Membro X
		- Pagar Mensalidade
	- Forms
		- Cadastrar um Forms de pagamento
		- Remover um Forms de Pagamento
		- Editar um Forms de Pagamento


## Product Backlog :
	1- Base de Dados ✅ 
	2- Cadastrar Membro ✅ 
	3- Cadastrar um registro de Conta
	4- Cadastrar um Forms
	5- Prover Mensalidade de um Membro X
	6- Pagar Mensalidade
	7- Deletar Membro
	8- Editar informações de um Membro
	9- Deletar registro de Conta
	10- Editar registro de Conta
	11- Remover um Forms de Pagamento
	12- Editar um Forms de Pagamento