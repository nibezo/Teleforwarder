import telebot

media_group_id = []
message_id = []
date = []
bot = telebot.TeleBot("5036901574:AAHr80p-rd6BbjXT6h40YsOLybZjxeJ3gM4", parse_mode=None)
x = 0


def all_the_same(elements):
    # return True if all elements the same
    return len(elements) < 1 or len(elements) == elements.count(elements[0])
# 1111 - -763688879
# main - -783236302
# C2 - -757448895
# C4 - -747350870


@bot.message_handler(content_types=['text'])
def forward_text(message):
    print(message.chat.id, '\n')
    print(message.chat.title)
    print(message.text)
    if str(message.chat.id == '-1001697120368') and str(message.text).lower() == 'да':
        bot.reply_to(message, "Провода")
    if str(message.chat.id) == '-783236302':
        if 'с4' in str(message.text).lower() or 'c4' in str(message.text).lower():
            print(message)
            bot.forward_message('-747350870', '-783236302', message.id)
        elif 'с2' in str(message.text).lower() or 'c2' in str(message.text).lower():
            bot.forward_message('-757448895', '-783236302', message.id)
        elif '1111' in str(message.text):
            bot.forward_message('-763688879', '-783236302', message.id)


'''
1. Check message_group_id and member it
2. Append to files_ids ids of the files
'''


# media_group_id for media group
@bot.message_handler(content_types=['photo'])
def forward_text(message):
    if str(message.chat.id) == '-783236302' and str(message.media_group_id) == 'None':
        if 'с4' in str(message.caption).lower() or 'c4' in str(message.caption).lower():
            bot.forward_message('-747350870', '-783236302', message.id)
        elif 'с2' in str(message.caption).lower() or 'c2' in str(message.caption).lower():
            bot.forward_message('-757448895', '-783236302', message.id)
        elif '1111' in str(message.caption):
            bot.forward_message('-763688879', '-783236302', message.id)
        print('This is not media group!\n')

    # For media group
    # print(message.photo[-1].file_id)  # get photo id
    #
    # if str(message.chat.id) == '-783236302' and str(message.media_group_id) != 'None':
    #     print(message.photo[-1].file_id)
    #     print(message.photo[-1])
    #     print(message.photo)
    #     print(len(message.photo))
    #     files_ids.append(str(message.photo[-1].file_id))
    # if str(message.photo[-1].file_id) not in files_ids:
    #     print('OK')

    # print(files_ids)
    # if 'с4' in str(message.caption).lower() or 'c4' in str(message.caption).lower():
    #     bot.forward_message('-747350870', '-783236302', message.id)
    if str(message.chat.id) == '-783236302' and str(message.media_group_id) != 'None':
        # print(message.media_group_id, '\n')
        # print('This is media group!\n')
        media_group_id.append(str(message.media_group_id))
        message_id.append(str(message.id))
        date.append(str(message.date))

        # Forward the 1st photo to the specified chat
        if 'с4' in str(message.caption).lower() or 'c4' in str(message.caption).lower():
            bot.forward_message('-747350870', '-783236302', message.id)
        elif 'с2' in str(message.caption).lower() or 'c2' in str(message.caption).lower():
            bot.forward_message('-757448895', '-783236302', message.id)
        elif '1111' in str(message.caption):
            bot.forward_message('-763688879', '-783236302', message.id)
        elif '' in str(message.caption):
            print('NEXT PHOTO(S)\n')
            print(media_group_id, '\n')
            print(date, '\n')
            print(message_id, '\n')
            print(all_the_same(date))


bot.infinity_polling()
