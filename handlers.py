from db_handlers import insert_member
from telegram import replymarkup
from telegram.ext.conversationhandler import ConversationHandler
from telegram.inline.inlinekeyboardbutton import InlineKeyboardButton
from telegram.inline.inlinekeyboardmarkup import InlineKeyboardMarkup

CPF, NOME, TIPO_QUARTO, ESTADO_PRESENCA = range(4)

def register_member(update,context):
    update.message.reply_text(
        text = 'CPF'
    )

    return CPF

def cpf(update,context):
    global list
    
    list = []
    cpf = update.message.text
    list.append(cpf)

    update.message.reply_text(
        text = 'Nome'
    )

    return NOME

def name(update,context):
    global list

    name = update.message.text
    list.append(name)

    button_individual = InlineKeyboardButton(text='Individual', callback_data='individual')
    button_compartilhado = InlineKeyboardButton(text='Compartilhado', callback_data='compartilhado')
    
    update.message.reply_text(
        text = 'Tipo de Quarto',
        reply_markup = InlineKeyboardMarkup([[button_individual, button_compartilhado]])
    )

    return TIPO_QUARTO

def type_room(update,context):
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

    return ESTADO_PRESENCA

def presence_state(update, context):
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

def cancel_registration(update,context):
    global list

    list = []
    
    update.message.reply_text('Operação cancelada!')

    return ConversationHandler.END

