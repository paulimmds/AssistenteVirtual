from telegram import replymarkup
from db_handlers import insert_member, update_bill, insert_forms
from telegram.ext.conversationhandler import ConversationHandler
from telegram.inline.inlinekeyboardbutton import InlineKeyboardButton
from telegram.inline.inlinekeyboardmarkup import InlineKeyboardMarkup
from datetime import date

CPF_MEMBER, NOME_MEMBER, TIPO_QUARTO_MEMBER, ESTADO_PRESENCA_MEMBER = range(4)
DATA_REFERENCIA_BILL, TIPO_CONTA_BILL, VALOR_BILL = range(3)
CPF_FORMS, TIPO_CONTA_FORMS, DATA_REFERENCIA_FORMS, VALOR_FORMS, DATA_PAGAMENTO_FORMS = range(5)

def member_register(update,context):
    update.message.reply_text(
        text = 'CPF'
    )

    return CPF_MEMBER

def member_cpf(update,context):
    global list
    
    list = []
    cpf = update.message.text
    list.append(cpf)

    update.message.reply_text(
        text = 'Nome'
    )

    return NOME_MEMBER

def member_name(update,context):
    global list

    name = update.message.text
    list.append(name)

    button_individual = InlineKeyboardButton(text='Individual', callback_data='individual')
    button_compartilhado = InlineKeyboardButton(text='Compartilhado', callback_data='compartilhado')
    
    update.message.reply_text(
        text = 'Tipo de Quarto',
        reply_markup = InlineKeyboardMarkup([[button_individual, button_compartilhado]])
    )

    return TIPO_QUARTO_MEMBER

def member_type_room(update,context):
    global list

    query = update.callback_query
    query.answer()

    type_room = query.data

    type_room = 0 if type_room == 'individual' else 1

    list.append(type_room)

    button_in_sanca = InlineKeyboardButton(text='Em Sanca', callback_data='em_sanca')
    button_out_sanca = InlineKeyboardButton(text='Fora de Sanca', callback_data='fora_de_sanca')

    query.edit_message_text(
        text = 'Estado de Presença',
        reply_markup=InlineKeyboardMarkup([[button_in_sanca, button_out_sanca]])
    )

    return ESTADO_PRESENCA_MEMBER

def member_presence_state(update, context):
    global list

    query = update.callback_query
    query.answer()

    presence_state = query.data

    presence_state = 0 if presence_state == 'em_sanca' else 1

    list.append(presence_state)

    insert_member(list)

    query.edit_message_text(
        text = 'Dados salvos com sucesso!'
    )

    return ConversationHandler.END

def bill_register(update,context):
    update.message.reply_text(
        text = 'Data de Referência'
    )

    return DATA_REFERENCIA_BILL

def bill_reference_date(update,context):
    global list

    list = []

    reference_date = update.message.text
    reference_date = [int(i) for i in reference_date.split('/')]
    
    try:
        reference_date = date(reference_date[0], reference_date[1], reference_date[2])
    except:
        reference_date = date(reference_date[2], reference_date[1], reference_date[0])
    finally:
        list.append(reference_date)

    update.message.reply_text(
        text="Tipo de Conta",
        reply_markup=InlineKeyboardMarkup([
            [InlineKeyboardButton(text="Aluguel", callback_data='ALUGUEL')],
            [InlineKeyboardButton(text="Job", callback_data='JOB')],
            [InlineKeyboardButton(text="Caixa", callback_data='CAIXA')],
            [InlineKeyboardButton(text="Água", callback_data='AGUA')],
            [InlineKeyboardButton(text="Energia", callback_data='ENERGIA')],
            [InlineKeyboardButton(text="Gás", callback_data='GAS')],
            [InlineKeyboardButton(text="Mercado", callback_data='MERCADO')],
            [InlineKeyboardButton(text="Vivo", callback_data='VIVO')],
            [InlineKeyboardButton(text="Poupança", callback_data='POUPANÇA')],
            [InlineKeyboardButton(text="Cacau", callback_data='CACAU')],
            [InlineKeyboardButton(text="Outros Gastos", callback_data='OUTROS_GASTOS')],
            [InlineKeyboardButton(text="Descontos", callback_data='DESCONTOS')],
            [InlineKeyboardButton(text='Cancelar', callback_data='cancelar_registro')]
        ])    
    )

    return TIPO_CONTA_BILL

def bill_type(update,context):
    global list

    query = update.callback_query
    query.answer()

    type_bill = query.data

    list.append(type_bill)

    query.edit_message_text(
        text = 'Valor'
    )

    return VALOR_BILL

def bill_value(update, context):
    global list
    
    value = update.message.text
    
    try:
        value = value.replace(',','.')
    finally:
        float(value)

    list.append(value)

    update_bill(list)

    update.message.reply_text(
        text = 'Registro inserido com sucesso.'
    )

    return ConversationHandler.END

def forms_register(update,context):
    update.message.reply_text(
        text = 'CPF'
    )

    return CPF_FORMS

def forms_cpf(update,context):
    global list

    list = []
    cpf = update.message.text
    list.append(cpf)

    update.message.reply_text(
        text = 'Tipo de Conta',
        reply_markup=InlineKeyboardMarkup([
            [InlineKeyboardButton(text="Mercado", callback_data='MERCADO')],
            [InlineKeyboardButton(text="Gas", callback_data='GAS')],
            [InlineKeyboardButton(text="Vivo", callback_data='VIVO')],
            [InlineKeyboardButton(text="Cacau", callback_data='CACAU')],
            [InlineKeyboardButton(text="Gastos", callback_data='GASTOS')],
            [InlineKeyboardButton(text="Aluguel", callback_data='ALUGUEL')]
        ])
    )

    return TIPO_CONTA_FORMS

def forms_type(update,context):
    global list

    query = update.callback_query
    query.answer()

    type_bill = query.data

    list.append(type_bill)

    query.edit_message_text(
        text = 'Data de Referência'
    )

    return DATA_REFERENCIA_FORMS

def forms_reference_date(update,context):
    global list

    reference_date = update.message.text
    reference_date = [int(i) for i in reference_date.split('/')]
    
    try:
        reference_date = date(reference_date[0], reference_date[1], reference_date[2])
    except:
        reference_date = date(reference_date[2], reference_date[1], reference_date[0])
    finally:
        list.append(reference_date)

    update.message.reply_text(
        text = 'Valor'
    )

    return VALOR_FORMS
    
def forms_value(update,context):
    global list
    
    value = update.message.text
    
    try:
        value = value.replace(',','.')
    finally:
        float(value)

    list.append(value)

    update.message.reply_text(
        text = 'Data de Pagamento'
    )

    return DATA_PAGAMENTO_FORMS

def forms_paym_date(update,context):
    global list

    paym_date = update.message.text
    paym_date = [int(i) for i in paym_date.split('/')]
    
    try:
        paym_date = date(paym_date[0], paym_date[1], paym_date[2])
    except:
        paym_date = date(paym_date[2], paym_date[1], paym_date[0])
    finally:
        list.append(paym_date)

    insert_forms(list)

    update.message.reply_text(
        text = 'Registro inserido com sucesso!'
    )

    return ConversationHandler.END

def cancel_registration(update,context):
    global list

    list = []
    
    update.message.reply_text('Operação cancelada!')

    return ConversationHandler.END

