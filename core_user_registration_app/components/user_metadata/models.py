""" Metadata model
"""

from django_mongoengine import fields
from mongoengine import errors as mongoengine_errors
from mongoengine.queryset.base import NULLIFY
from mongoengine.queryset.visitor import Q

from core_main_app.commons import exceptions
from core_main_app.components.abstract_data.models import AbstractData
from core_main_app.components.template.models import Template
from core_main_app.components.workspace.models import Workspace


class UserMetadata(AbstractData):
    """Metadata object"""

    template = fields.ReferenceField(Template, blank=False)
    user_id = fields.StringField()
    workspace = fields.ReferenceField(
        Workspace, reverse_delete_rule=NULLIFY, blank=True
    )
    meta = {"indexes": ["title", "last_modification_date", "template", "user_id"]}

    @staticmethod
    def get_all(order_by_field):
        """Get all data.

        Args:
            order_by_field: Order by field.

        Returns:

        """
        return UserMetadata.objects.order_by(*order_by_field)

    @staticmethod
    def get_all_except(order_by_field, id_list=None):
        """Get all data except for the ones with ID within the provided list.

        Args:
            id_list:
            order_by_field:

        Returns:
        """
        if id_list is None:
            return UserMetadata.get_all(order_by_field)

        return UserMetadata.objects(pk__nin=id_list).order_by(*order_by_field)

    @staticmethod
    def get_all_by_user_id(user_id, order_by_field):
        """Get all data relative to the given user id

        Args:
            user_id:
            order_by_field: Order by field.

        Returns:

        """
        return UserMetadata.objects(user_id=str(user_id)).order_by(*order_by_field)

    @staticmethod
    def get_all_except_user_id(user_id, order_by_field):
        """Get all data non relative to the given user id

        Args:
            user_id:
            order_by_field:

        Returns:

        """
        return UserMetadata.objects(user_id__nin=str(user_id)).order_by(*order_by_field)

    @staticmethod
    def get_all_by_id_list(list_id, order_by_field):
        """Return the object with the given list id.

        Args:
            list_id:
            order_by_field:

        Returns:
            Object collection
        """
        return UserMetadata.objects(pk__in=list_id).order_by(*order_by_field)

    @staticmethod
    def get_by_id(data_id):
        """Return the object with the given id.

        Args:
            data_id:

        Returns:
            Data (obj): Data object with the given id

        """
        try:
            return UserMetadata.objects.get(pk=str(data_id))
        except mongoengine_errors.DoesNotExist as e:
            raise exceptions.DoesNotExist(str(e))
        except Exception as ex:
            raise exceptions.ModelError(str(ex))

    @staticmethod
    def execute_query(query, order_by_field):
        """Execute a query.

        Args:
            query:
            order_by_field: Order by field.

        Returns:

        """
        return UserMetadata.objects(__raw__=query).order_by(*order_by_field)

    @staticmethod
    def get_all_by_workspace(workspace, order_by_field):
        """Get all data that belong to the workspace.

        Args:
            workspace:
            order_by_field:

        Returns:

        """
        return UserMetadata.objects(workspace=workspace).order_by(*order_by_field)

    @staticmethod
    def get_all_by_list_workspace(list_workspace, order_by_field):
        """Get all data that belong to the list of workspace.

        Args:
            list_workspace:
            order_by_field:

        Returns:

        """
        return UserMetadata.objects(workspace__in=list_workspace).order_by(
            *order_by_field
        )

    @staticmethod
    def get_all_by_list_template(list_template, order_by_field):
        """Get all data that belong to the list of template.

        Args:
            list_template:
            order_by_field:

        Returns:

        """
        return UserMetadata.objects(template__in=list_template).order_by(
            *order_by_field
        )

    @staticmethod
    def get_all_by_user_and_workspace(user_id, list_workspace, order_by_field):
        """Get all data that belong to the list of workspace and owned by a user.

        Args:
            list_workspace:
            user_id:
            order_by_field:

        Returns:

        """
        return UserMetadata.objects(
            Q(workspace__in=list_workspace) | Q(user_id=str(user_id))
        ).order_by(*order_by_field)
