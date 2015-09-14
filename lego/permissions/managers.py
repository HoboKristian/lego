# -*- coding: utf8 -*-
from basis.managers import PersistentModelManager


class PublicObjectPermissionsManager(PersistentModelManager):
    def get_queryset(self):
        return super(PublicObjectPermissionsManager, self).get_queryset().filter(
            require_auth=False,
            can_view_groups=None)