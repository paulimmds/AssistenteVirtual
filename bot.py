import logging
from telegram.ext import Updater
from telegram.ext.callbackqueryhandler import CallbackQueryHandler
from telegram.ext.commandhandler import CommandHandler
from telegram.ext.conversationhandler import ConversationHandler
from telegram.ext.filters import Filters
from telegram.ext.messagehandler import MessageHandler
from handlers import member_register, member_cpf, member_name, member_type_room, member_presence_state 
from handlers import bill_register, bill_reference_date, bill_type, bill_value
from handlers import forms_register, forms_cpf, forms_type, forms_reference_date, forms_value, forms_paym_date
from handlers import cancel_registration
from handlers import CPF_MEMBER, NOME_MEMBER, TIPO_QUARTO_MEMBER, ESTADO_PRESENCA_MEMBER
from handlers import DATA_REFERENCIA_BILL, TIPO_CONTA_BILL, VALOR_BILL
from handlers import CPF_FORMS, TIPO_CONTA_FORMS, DATA_REFERENCIA_FORMS, VALOR_FORMS, DATA_PAGAMENTO_FORMS
from setup import telegram


logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)

logger = logging.getLogger(__name__)

def main():

    updater = Updater(token=telegram['token'])
    dp = updater.dispatcher

    CadastrarMembro = ConversationHandler(
        entry_points=[CommandHandler('cadastrar_membro', member_register)],
        states={
            CPF_MEMBER : [MessageHandler(Filters.text & ~Filters.command, member_cpf)],
            NOME_MEMBER : [MessageHandler(Filters.text & ~Filters.command, member_name)],
            TIPO_QUARTO_MEMBER : [
                CallbackQueryHandler(pattern='individual', callback=member_type_room),
                CallbackQueryHandler(pattern='compartilhado', callback=member_type_room)
            ],
            ESTADO_PRESENCA_MEMBER : [
                CallbackQueryHandler(pattern='em_sanca', callback=member_presence_state),
                CallbackQueryHandler(pattern='fora_de_sanca', callback=member_presence_state)
            ]
            
        },
        fallbacks=[CommandHandler('cancelar_registro', cancel_registration)]
    )

    CadastrarRegistro = ConversationHandler(
        entry_points=[CommandHandler('registrar_conta', bill_register)],
        states = {
            DATA_REFERENCIA_BILL : [MessageHandler(Filters.text & ~Filters.command, bill_reference_date)],
            TIPO_CONTA_BILL : [
                CallbackQueryHandler(pattern='ALUGUEL', callback=bill_type),
                CallbackQueryHandler(pattern='JOB', callback=bill_type),
                CallbackQueryHandler(pattern='CAIXA', callback=bill_type),
                CallbackQueryHandler(pattern='AGUA', callback=bill_type),
                CallbackQueryHandler(pattern='ENERGIA', callback=bill_type),
                CallbackQueryHandler(pattern='GAS', callback=bill_type),
                CallbackQueryHandler(pattern='MERCADO', callback=bill_type),
                CallbackQueryHandler(pattern='VIVO', callback=bill_type),
                CallbackQueryHandler(pattern='POUPANÇA', callback=bill_type),
                CallbackQueryHandler(pattern='CACAU', callback=bill_type),
                CallbackQueryHandler(pattern='OUTROS_GASTOS', callback=bill_type),
                CallbackQueryHandler(pattern='DESCONTOS', callback=bill_type)
            ],
            VALOR_BILL : [MessageHandler(Filters.text & ~Filters.command, bill_value)]     
        },
        fallbacks = [CommandHandler('cancelar_registro', cancel_registration),
                     CallbackQueryHandler(pattern='cancelar_registro', callback=cancel_registration)]
    )

    CadastrarForms = ConversationHandler(
        entry_points=[CommandHandler('registrar_forms', forms_register)],
        states={
            CPF_FORMS: [MessageHandler(Filters.text & ~Filters.command, forms_cpf)],
            TIPO_CONTA_FORMS: [
                CallbackQueryHandler(pattern='MERCADO', callback=forms_type),
                CallbackQueryHandler(pattern='GAS', callback=forms_type),
                CallbackQueryHandler(pattern='VIVO', callback=forms_type),
                CallbackQueryHandler(pattern='CACAU', callback=forms_type),
                CallbackQueryHandler(pattern='GASTOS', callback=forms_type),
                CallbackQueryHandler(pattern='ALUGUEL', callback=forms_type),
            ],
            DATA_REFERENCIA_FORMS:[MessageHandler(Filters.text & ~Filters.command, forms_reference_date)],
            VALOR_FORMS: [MessageHandler(Filters.text & ~Filters.command, forms_value)],
            DATA_PAGAMENTO_FORMS: [MessageHandler(Filters.text & ~Filters.command, forms_paym_date)]
        },
        fallbacks=[CommandHandler('cancelar_registro',cancel_registration)]
    )

    dp.add_handler(CadastrarMembro)
    dp.add_handler(CadastrarRegistro)
    dp.add_handler(CadastrarForms)

    updater.start_polling()

    print('Bot em Execução!')

if __name__ == '__main__':
    main()
