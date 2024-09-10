from enum import Enum
from pyrogram.types import ReplyKeyboardMarkup, KeyboardButton

class ButtonTemplate(Enum):
    """
    This class provides a way to define and manage button layouts using the `Enum` members as button texts. It supports two modes of button arrangement:

    1. **Custom Layout with `placing` Attribute**:
        - If the `placing` attribute is defined in the subclass, it should be a list of lists, where each inner list represents a row of buttons.
        - The `get_keyboard` method will use this attribute to arrange the buttons according to the specified rows.

    2. **Default Layout without `placing` Attribute**:
        - If the `placing` attribute is not defined, the method will arrange all buttons with a default layout of 2 buttons per row.
        - This default layout is automatically created based on the enumeration members.
    """
    
    @classmethod
    def get_keyboard(cls) -> ReplyKeyboardMarkup:
        """
        Returns a ReplyKeyboardMarkup object based on button texts and their placement.
        If `placing` is not defined, arranges buttons with 2 per row.
        """
        if getattr(cls, 'placing', None):
            keyboard = []
            for row in cls.placing.value:
                keyboard.append([KeyboardButton(getattr(cls, btn).value) for btn in row])
        else:
            button_texts = [btn.value for btn in cls]
            keyboard = [button_texts[i:i+2] for i in range(0, len(button_texts), 2)]
            keyboard = [[KeyboardButton(text) for text in row] for row in keyboard]

        return ReplyKeyboardMarkup(keyboard, resize_keyboard=True)

