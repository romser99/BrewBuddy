from django import template

register = template.Library()

@register.filter
def attr(value, arg):
    attrs = {}
    if arg:
        pairs = arg.split(",")
        for pair in pairs:
            if ":" in pair:
                key, value = pair.split(":")
                attrs[key.strip()] = value.strip()
    if isinstance(value, str):
        attrs['value'] = value  # Set the value attribute for string values
        return attrs
    widget = value.field.widget
    if isinstance(widget, (template.Template, template.TemplateDoesNotExist)):
        widget = value.as_widget(attrs={'value': value})  # Pass the value attribute directly
    else:
        attrs['value'] = value.value() if value.value() is not None else ''  # Get the value from the form field
        widget.attrs = attrs
    return widget
