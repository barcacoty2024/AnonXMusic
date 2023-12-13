from pyrogram.types import InlineKeyboardButton

import config
from AnonXMusic import app


def start_panel(_):
    buttons = [
        [
            InlineKeyboardButton(
                text=_["S_B_1"], url=f"https://t.me/{app.username}?startgroup=true"
            ),
            InlineKeyboardButton(text=_["S_B_2"], url=config.SUPPORT_CHAT),
        ],
    ]
    return buttons


def private_panel(_):
    buttons = [
        [
            InlineKeyboardButton(
                text=_["S_B_3"],
                url=f"https://t.me/{app.username}?startgroup=true",
            )
        ],
        [InlineKeyboardButton(text=_["S_B_4"], callback_data="settings_back_helper")],
        [
            InlineKeyboardButton(text=_["S_B_5"], user_id=6851974966),
            InlineKeyboardButton(text=_["S_B_2"], url=f"htts://t.me/Berlinsupportmanage"),
        ],
        [
            InlineKeyboardButton(text=_["S_B_6"], url=f"https://t.me/Asupan_bokepviral"),
            InlineKeyboardButton(text=_["S_B_7"], url=f"https://xnxx.com"),
        ],
    ]
    return buttons
