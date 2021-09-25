from django import template


register = template.Library()

# برای مسیر تصویر میخواستم از این فیلتر استفاده کنم که دیگه نیازی نیست
@register.filter
def addstr(arg1, arg2):
    """concatenate arg1 & arg2"""
    return arg1 + str(arg2)
