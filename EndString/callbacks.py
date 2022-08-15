from . import CBQ, Client
from .start import m_id

@Client.on_callback_query()
async def (_, q: CBQ):
    if q.data == "OWN_API":
        await q.answer("Pyrogram string generation", show_alert=True)
        
        
