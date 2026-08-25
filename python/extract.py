from anthropic.types import Message, TextBlock


def extract_text_from_message(message: Message):
    """从 Anthropic 响应中提取第一个 TextBlock 的文本"""
    text_blocks = [
        block.text for block in message.content if isinstance(block, TextBlock)
    ]
    return text_blocks[0] if text_blocks else ""
