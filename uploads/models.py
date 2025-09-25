from django.db import models
from django.db.models.signals import post_delete
from django.dispatch import receiver

# Create your models here.
class Upload(models.Model):
    file = models.FileField(upload_to="uploads/")
    model_name = models.CharField(max_length=200)
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.model_name
    


@receiver(post_delete, sender=Upload)
def delete_file_on_instance_delete(sender, instance, **kwargs):
    """Delete file from storage when corresponding `Upload` object is deleted."""
    if instance.file:
        instance.file.delete(save=False)