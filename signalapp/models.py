from django.db import models
from django.db.models.signals import post_init,pre_save,pre_delete,post_delete,post_save,pre_init
from django.dispatch import receiver
# Create your models here.

class Product(models.Model):
    name = models.CharField(max_length=20)
    category = models.CharField(max_length=20)
    price = models.IntegerField()

    class Meta:
        db_table = 'productinfo'

@receiver(pre_init,sender=Product)
def prod_preinit(sender,*args,**kwargs):
    print('pre-init invoked {}'.format(sender))

@receiver(post_init,sender=Product)
def prod_postinit(sender,instance,**kwargs):
    print('post-init invoked {}{}'.format(sender,instance))

@receiver(pre_save,sender=Product)
def prod_presave(sender,instance,update_fields,raw,**kwargs):
    print('pre-save invoked {}{}{}{}'.format(sender,instance,update_fields,raw))

@receiver(post_save,sender=Product)
def prod_postsave(sender,instance,using,created,raw,update_fields,**kwargs):
    print('post-save invoked {}{}{}{}{}'.format(sender,instance,using,raw,update_fields))

@receiver(pre_delete,sender=Product)
def prod_predelete(sender,instance,using,**kwargs):
    print('pre-delete invoked {}{}{}'.format(sender,instance,using))

@receiver(post_delete,sender=Product)
def prod_postdelete(sender,instance,using,**kwargs):
    print('post-delete invoked {}{}{}'.format(sender,instance,using))

