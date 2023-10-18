from django.db import models


class File_upload(models.Model):
    file_upload = models.FileField(upload_to="docsfile")
