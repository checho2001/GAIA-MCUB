from django.db import models

from django.core.exceptions import ObjectDoesNotExist


class ActionField(models.PositiveSmallIntegerField):
    def __init__(self, *args, **kwargs):
        kwargs["primary_key"] = True
        super().__init__(*args, **kwargs)

    def pre_save(self, model_instance, add):
        if getattr(model_instance, self.attname) is None:
            try:
                obj = self.model.objects.latest(self.attname)
                value = obj.id_user_action + 1
            except ObjectDoesNotExist:
                value = 1
            setattr(model_instance, self.attname, value)
            return value
        else:
            return super().pre_save(model_instance, add)
