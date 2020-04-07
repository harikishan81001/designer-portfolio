import os
import datetime

def get_upload_path(instance, filename, group):
    model_name = instance.__class__.__name__
    slug = getattr(instance, 'slug', None)
    if not slug:
        slug = instance.work_profile.slug
    return os.path.join(model_name, slug, group, filename)