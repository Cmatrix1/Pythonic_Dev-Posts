from pyrogram.types import ReplyKeyboardMarkup, KeyboardButton


def get_main_menu_keyboard():
    keyboard = [
        [
            KeyboardButton("📦 View Products"),
            KeyboardButton("💳 Buy Subscription")
        ],
        [
            KeyboardButton("🛠️ Support"),
            KeyboardButton("📈 Order Status"),
            KeyboardButton("⚙️ Settings"),
        ],
        [
            KeyboardButton("🔙 Exit")
        ],
    ]
    return ReplyKeyboardMarkup(keyboard, resize_keyboard=True)


def get_user_profile_menu_keyboard():
    keyboard = [
        [
            KeyboardButton("👤 View Profile"), 
            KeyboardButton("✏️ Edit Profile")
        ],
        [
            KeyboardButton("🔙 Back to Main Menu")
        ],
    ]
    return ReplyKeyboardMarkup(keyboard, resize_keyboard=True)


def get_admin_panel_menu_keyboard():
    keyboard = [
        [
            KeyboardButton("📊 View Stats"), 
            KeyboardButton("👥 Manage Users")
        ],
        [
            KeyboardButton("📦 Manage Products"), 
            KeyboardButton("⚙️ Settings")
        ],
        [KeyboardButton("🔙 Back to Main Menu")],
    ]
    return ReplyKeyboardMarkup(keyboard, resize_keyboard=True)


def get_settings_menu_keyboard():
    keyboard = [
        [
            KeyboardButton("🔔 Notifications"), 
            KeyboardButton("🌐 Language Settings")
        ],
        [KeyboardButton("🔙 Back to Main Menu")],
    ]
    return ReplyKeyboardMarkup(keyboard, resize_keyboard=True)


