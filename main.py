import telebot
bot = telebot.TeleBot("5036901574:AAHr80p-rd6BbjXT6h40YsOLybZjxeJ3gM4", parse_mode=None)


@bot.message_handler(content_types=['text'])
def check(message):
    print(f'Chat title: {message.chat.title}\nChat id: {message.chat.id}\n')


@bot.message_handler(content_types=['text'])
def forward_text(message):
    if str(message.chat.id == '-1001697120368') and str(message.text).lower() == 'да':
        bot.reply_to(message, "Провода")
    if str(message.chat.id) == '-783236302':
        if 'с4' in str(message.text).lower() or 'c4' in str(message.text).lower():
            bot.forward_message('-747350870', '-783236302', message.id)
        elif 'с2' in str(message.text).lower() or 'c2' in str(message.text).lower():
            bot.forward_message('-757448895', '-783236302', message.id)
        elif '1111' in str(message.text):
            bot.forward_message('-763688879', '-783236302', message.id)


# media_group_id for media group
@bot.message_handler(content_types=['photo'])
def forward_text(message):
    if str(message.chat.id) == '-1001697120368' and str(message.media_group_id) == 'None':
        if 'с4' in str(message.caption).lower() or 'c4' in str(message.caption).lower():
            bot.forward_message('-1001793220760', '-1001697120368', message.id)
        elif 'с2' in str(message.caption).lower() or 'c2' in str(message.caption).lower():
            bot.forward_message('-1001572181895', '-1001697120368', message.id)
        elif '1111' in str(message.caption):
            bot.forward_message('-608096809', '-1001697120368', message.id)
        print('This is not media group!\n')

    # For media group
    if str(message.chat.id) == '-783236302' and str(message.media_group_id) != 'None':
        # Forward the 1st photo to the specified chat
        if 'с4' in str(message.caption).lower() or 'c4' in str(message.caption).lower():
            bot.forward_message('-1001793220760', '-1001697120368', message.id)
        elif 'с2' in str(message.caption).lower() or 'c2' in str(message.caption).lower():
            bot.forward_message('-1001572181895', '-1001697120368', message.id)
        elif '1111' in str(message.caption):
            bot.forward_message('-608096809', '-1001697120368', message.id)


bot.infinity_polling()
