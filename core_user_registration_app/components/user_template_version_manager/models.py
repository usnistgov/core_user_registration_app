"""
Template Version Manager model
"""
from django_mongoengine import fields
from mongoengine import errors as mongoengine_errors

from core_main_app.commons import exceptions
from core_main_app.components.version_manager.models import VersionManager


class UserTemplateVersionManager(VersionManager):
    """Manager of templates versions"""

    # TODO: see if better way to find _cls
    class_name = "VersionManager.UserTemplateVersionManager"
    is_default = fields.BooleanField(default=False)

    @staticmethod
    def get_global_version_managers(_cls=True):
        """Return all Template Version Managers with user set to None.

        Returns:
            _cls: if True, restricts to TemplateVersionManager _cls
        """
        queryset = super(
            UserTemplateVersionManager, UserTemplateVersionManager
        ).get_global_version_managers()
        if _cls:
            queryset = queryset.filter(_cls=UserTemplateVersionManager.class_name).all()
        return queryset

    @staticmethod
    def get_active_global_version_manager(_cls=True):
        """Return all active Version Managers with user set to None.

        Returns:

        """
        queryset = super(
            UserTemplateVersionManager, UserTemplateVersionManager
        ).get_active_global_version_manager()
        if _cls:
            queryset = queryset.filter(_cls=UserTemplateVersionManager.class_name).all()
        return queryset

    @staticmethod
    def get_active_version_manager_by_user_id(user_id, _cls=True):
        """Return all active Version Managers with given user id.

        Returns:

        """
        if not user_id:
            return UserTemplateVersionManager.objects.none()
        queryset = super(
            UserTemplateVersionManager, UserTemplateVersionManager
        ).get_active_version_manager_by_user_id(user_id)
        if _cls:
            queryset = queryset.filter(_cls=UserTemplateVersionManager.class_name).all()
        return queryset

    @staticmethod
    def get_by_version_id(version_id):
        """Get the template version manager containing the given version id.

        Args:
            version_id: version id.

        Returns:
            template version manager.

        """
        try:
            return UserTemplateVersionManager.objects.get(versions__contains=version_id)
        except mongoengine_errors.DoesNotExist as e:
            raise exceptions.DoesNotExist(str(e))
        except Exception as ex:
            raise exceptions.ModelError(str(ex))

    @staticmethod
    def get_all_by_version_ids(version_ids):
        """Get all template version managers by a list of version ids.

        Args:
            version_ids: list of version ids.

        Returns:
            List of template version managers.

        """
        return UserTemplateVersionManager.objects(versions__in=version_ids).all()

    @staticmethod
    def get_all_version_manager_except_user_id(user_id, _cls=True):
        """Return all Version Managers of all users except user with given user id.

        Args:
            user_id:
            _cls:

        Returns:

        """
        queryset = super(
            UserTemplateVersionManager, UserTemplateVersionManager
        ).get_all_version_manager_except_user_id(user_id)
        if _cls:
            queryset = queryset.filter(_cls=UserTemplateVersionManager.class_name).all()
        return queryset

    @staticmethod
    def get_all_version_manager_by_user_id(user_id, _cls=True):
        """Return all Version Managers with given user id.

        Args:
            user_id:
            _cls:

        Returns:

        """
        if not user_id:
            return UserTemplateVersionManager.objects.none()
        queryset = super(
            UserTemplateVersionManager, UserTemplateVersionManager
        ).get_all_version_manager_by_user_id(user_id)
        if _cls:
            queryset = queryset.filter(_cls=UserTemplateVersionManager.class_name).all()
        return queryset

    @staticmethod
    def get_all_version_manager_by_title(version_manager_title, _cls=True):
        """Return all Version Managers with given version manager title.

        Args:
            version_manager_title:
            _cls:

        Returns:

        """
        if not version_manager_title:
            return UserTemplateVersionManager.objects.none()
        queryset = super(
            UserTemplateVersionManager, UserTemplateVersionManager
        ).get_all_version_manager_by_title(version_manager_title)
        if _cls:
            queryset = queryset.filter(_cls=UserTemplateVersionManager.class_name).all()
        return queryset

    @staticmethod
    def get_all_version_manager(_cls=True):
        """Return all Version Managers.

        Args:
            _cls:

        Returns:

        """
        queryset = super(
            UserTemplateVersionManager, UserTemplateVersionManager
        ).get_all()
        if _cls:
            queryset = queryset.filter(_cls=UserTemplateVersionManager.class_name).all()
        return queryset

    def save_template_version_manager(self):
        """Custom save.

        Returns:
            Saved Instance.

        """
        return super(UserTemplateVersionManager, self).save_version_manager()

    @staticmethod
    def get_default_version_manager():
        """Return default User Version Manager.

        Returns:

        """
        return UserTemplateVersionManager.objects(is_default=True)
