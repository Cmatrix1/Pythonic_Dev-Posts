from abstract import ButtonTemplate


class UserProfileMenuButtons(ButtonTemplate):
    VIEW_PROFILE = "👤 View Profile"
    EDIT_PROFILE = "✏️ Edit Profile"
    BACK_TO_MAIN_MENU = "🔙 Back to Main Menu"

    placing = [
        ["VIEW_PROFILE", "EDIT_PROFILE"],
        ["BACK_TO_MAIN_MENU"],
    ]


class AdminPanelMenuButtons(ButtonTemplate):
    VIEW_STATS = "📊 View Stats"
    MANAGE_USERS = "👥 Manage Users"
    MANAGE_PRODUCTS = "📦 Manage Products"
    SETTINGS = "⚙️ Settings"
    BACK_TO_MAIN_MENU = "🔙 Back to Main Menu"


class ShoppingCartMenuButtons(ButtonTemplate):
    VIEW_CART = "🛒 View Cart"
    CHECKOUT = "📝 Checkout"
    CONTINUE_SHOPPING = "🔙 Continue Shopping"


class SettingsMenuButtons(ButtonTemplate):
    NOTIFICATIONS = "🔔 Notifications"
    LANGUAGE_SETTINGS = "🌐 Language Settings"
    BACK_TO_MAIN_MENU = "🔙 Back to Main Menu"

