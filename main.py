import telebot
files_ids = []
bot = telebot.TeleBot("5036901574:AAHr80p-rd6BbjXT6h40YsOLybZjxeJ3gM4", parse_mode=None)
# 1111 - -763688879
# main - -783236302
# C2 - -757448895
# C4 - -747350870


@bot.message_handler(content_types=['text'])
def forward_text(message):
    if str(message.chat.id) == '-783236302':
        if 'с4' in str(message.text).lower() or 'c4' in str(message.text).lower():
            print(message)
            bot.forward_message('-747350870', '-783236302', message.id)
        elif 'с2' in str(message.text).lower() or 'c2' in str(message.text).lower():
            bot.forward_message('-757448895', '-783236302', message.id)
        elif '1111' in str(message.text):
            bot.forward_message('-763688879', '-783236302', message.id)


# media_group_id for media group
@bot.message_handler(content_types=['photo'])
def forward_text(message):
    print(message)
    if str(message.chat.id) == '-783236302' and str(message.media_group_id) == 'None':
        if 'с4' in str(message.caption).lower() or 'c4' in str(message.caption).lower():
            bot.forward_message('-747350870', '-783236302', message.id)
        elif 'с2' in str(message.caption).lower() or 'c2' in str(message.caption).lower():
            bot.forward_message('-757448895', '-783236302', message.id)
        elif '1111' in str(message.caption):
            bot.forward_message('-763688879', '-783236302', message.id)
        print('This is not media group!')

    # For media group
    print(message.photo[-1].file_id) # get photo id
    #
    if str(message.chat.id) == '-783236302' and str(message.media_group_id) != 'None':
        print()
        files_ids.append(str(message.photo[-1].file_id))
        if str(message.photo[-1].file_id) not in files_ids:
            print('OK')

    print(files_ids)
    # if 'с4' in str(message.caption).lower() or 'c4' in str(message.caption).lower():
    #     bot.forward_message('-747350870', '-783236302', message.id)
    print('This is media group!')

print('s')
bot.infinity_polling()