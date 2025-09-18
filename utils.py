#工具函数，可根据需要扩展
def sanitize_filename(text):
    return "".join(c if c.isalnum() else "_" for c in text)