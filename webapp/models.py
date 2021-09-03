from django.db import models
import json
from django.utils.text import slugify
from django.db.models.signals import post_delete, pre_save
from django.dispatch import receiver

class pizza(models.Model):
    title = models.CharField(max_length = 100, null = False, default = 'EMPTY TITLE')
    type = models.CharField(max_length = 10) 
    size = models.CharField(max_length = 25)
    toppings = models.CharField(max_length = 200) 
    slug = models.SlugField(blank = True, unique = True)

    def __str__(self):
	    return self.title
    def set_top(self, x):
        self.toppings = json.dumps(x)
    def get_top(self):
        return json.loads(self.toppings)
    def sz(self):
        return self.size
    def tp(self):
        return self.type 


@receiver(post_delete, sender = pizza)
def pre_save_pizza_receiever(sender, instance, *args, **kwargs):
	if not instance.slug:
		instance.slug = slugify(instance.title + "-" + instance.type)

pre_save.connect(pre_save_pizza_receiever, sender = pizza)
