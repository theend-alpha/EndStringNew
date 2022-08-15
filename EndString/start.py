from . import Client, filters, Message, start_markup, IKM

@Client.on_message(filters.command("start") & filters.private)
async def start(_, m):
    ok = await m.reply("""Welcome to String Session Generator.


You can procees with bot's api values if you want , else you can proceed with your api values


Press Button to start generating session!""", reply_markup=IKM(start_markup))
    m_id = ok.message_id
