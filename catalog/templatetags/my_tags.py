from django import template

register = template.Library()


@register.filter()
def media_filter(path):
    if path:
        return f"/media/{path}"
    return "#"


@register.filter(name="is_moderator")
def is_moderator(user):
    return user.groups.filter(name="moderator").exists()
