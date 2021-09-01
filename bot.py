import logging
from telegram.ext import Updater
from telegram.ext.callbackqueryhandler import CallbackQueryHandler
from telegram.ext.commandhandler import CommandHandler
from telegram.ext.conversationhandler import ConversationHandler
from telegram.ext.filters import Filters
from telegram.ext.messagehandler import MessageHandler
from handlers import register_member, cpf, name, type_room, presence_state, cancel_registration
from handlers import CPF, NOME, TIPO_QUARTO, ESTADO_PRESENCA
from setup import telegram


logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)

logger = logging.getLogger(__name__)

def main():

    updater = Updater(token=telegram['token'])
    dp = updater.dispatcher

    CadastrarMembro = ConversationHandler(
        entry_points=[CommandHandler('cadastrar_membro', register_member)],
        states={
            CPF : [MessageHandler(Filters.text & ~Filters.command, cpf)],
            NOME : [MessageHandler(Filters.text & ~Filters.command, name)],
            TIPO_QUARTO : [
                CallbackQueryHandler(pattern='individual', callback=type_room),
                CallbackQueryHandler(pattern='compartilhado', callback=type_room)
            ],
            ESTADO_PRESENCA : [
                CallbackQueryHandler(pattern='em_sanca', callback=presence_state),
                CallbackQueryHandler(pattern='fora_de_sanca', callback=presence_state)
            ]
            
        },
        fallbacks=[CommandHandler('cancelar_registro', cancel_registration)]
    )

    dp.add_handler(CadastrarMembro)

    updater.start_polling()

    print('Bot em Execução!')

if __name__ == '__main__':
    main()






"""
if membro.tipo_quarto == 0 :
			qt_quartos_indv = cont(membro.tipo_quarto == 1)
			valor_aluguel = conta.aluguel * (qt_quartos_indv * 0.17)
			mens_aluguel = conta.aluguel / cont(membro.id)
		else :
			mens_aluguel = conta.aluguel * 0.17 / cont(membro.id)

		valor_energia = conta.energia * (membro.estado_presenca * 0.7)
		
		if membro.estado_presenca == 0 :
			valor_energia = conta.energia * 0.3
			mens_energia = valor_energia / cont(membro.estado_presenca == 0)
		
		else :
			valor_energia = conta.energia * 0.7
			mens_energia = valor_energia / cont(membro.estado_presenca == 1)
			
		mens_job = conta.job / cont(membro.cpf_membro) 
"""