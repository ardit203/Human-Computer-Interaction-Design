from django.db.models.signals import pre_save, pre_delete, post_save, post_delete
from django.dispatch import receiver

from .models import *


@receiver(pre_save, sender=Property)
def save_property(sender, instance, **kwargs):
    old_instance = Property.objects.filter(id=instance.id).first()
    if old_instance and old_instance.sold != instance.sold:
        property_agents = PropertyAgent.objects.filter(property=old_instance).all()
        for pa in property_agents:
            print("-----------", pa, "-----------------------")
            agent = pa.agent
            agent.completed_sales += 1
            agent.save()
            print(pa.agent.completed_sales)


@receiver([post_save, post_delete], sender=PropertyFeature)
def handle_features(sender, instance, **kwargs):
    property_features = sender.objects.filter(property=instance.property)

    if property_features:
        prop = instance.property
        prop.feature = ', '.join(f.feature.name for f in property_features)
        prop.save()
