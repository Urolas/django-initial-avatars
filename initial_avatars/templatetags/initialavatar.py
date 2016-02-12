# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib.auth.models import User
from django import template
from ..generator import AvatarGenerator, GRAVATAR_DEFAULT_SIZE, AVATAR_SHAPE

register = template.Library()


@register.simple_tag(name='get_initial_avatar')
def get_initial_avatar(user_or_email, size=GRAVATAR_DEFAULT_SIZE, shape=AVATAR_SHAPE):
    """ Builds an avatar <img> tag from an user or email """

    if hasattr(user_or_email, 'email'):
        email = user_or_email.email
    else:
        email = user_or_email
    try:
        user = User.objects.get(email=email)
    except User.DoesNotExist:
        return '<img src="" width="{width}" height="{height}"/>'.format(width=size, height=size)
    return AvatarGenerator(user, size=int(size), shape=shape).get_avatar()
