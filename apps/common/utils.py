import os
import hashlib
import random

from django.core.files.storage import FileSystemStorage
from rest_framework import permissions


def storage_factory(root, url):
    return FileSystemStorage(location=root, base_url=url)


def image_path(instance, filename):
    """Generates likely unique image path using md5 hashes"""
    filename, ext = os.path.splitext(filename.lower())
    instance_id_hash = hashlib.md5(str(instance).encode('utf-8')).hexdigest()
    filename_hash = ''.join(random.sample(hashlib.md5(filename.encode('utf-8')).hexdigest(), 8))
    return '{}/{}{}'.format(instance_id_hash, filename_hash, ext)


class IsAuthorOrReadOnly(permissions.BasePermission):
    """
    Custom permission to only allow authors of an object to edit it.
    """

    def has_object_permission(self, request, view, obj):
        # Read permissions are allowed to any request,
        # so we'll always allow GET, HEAD or OPTIONS requests.
        if request.method in permissions.SAFE_METHODS:
            return True

        # Write permissions are only allowed to the owner
        return obj.author == request.user
