""" Fixtures files for UserMetadata
"""
from core_main_app.components.template.models import Template
from core_main_app.components.workspace import api as workspace_api
from core_main_app.components.workspace.models import Workspace
from core_main_app.utils.integration_tests.fixture_interface import FixtureInterface
from core_user_registration_app.components.user_metadata.models import UserMetadata


class DataFixtures(FixtureInterface):
    """UserMetadata fixtures"""

    data_1 = None
    data_2 = None
    data_3 = None
    template = None
    data_collection = None

    def insert_data(self):
        """Insert a set of UserMetadata.

        Returns:

        """
        # Make a connexion with a mock database
        self.generate_template()
        self.generate_data_collection()

    def generate_data_collection(self):
        """Generate a UserMetadata collection.

        Returns:

        """
        # NOTE: no xml_content to avoid using unsupported GridFS mock
        self.data_1 = UserMetadata(
            template=self.template, user_id="1", dict_content=None, title="title"
        ).save()
        self.data_2 = UserMetadata(
            template=self.template, user_id="2", dict_content=None, title="title2"
        ).save()
        self.data_3 = UserMetadata(
            template=self.template, user_id="1", dict_content=None, title="title3"
        ).save()
        self.data_collection = [self.data_1, self.data_2, self.data_3]

    def generate_template(self):
        """Generate an unique Template.

        Returns:

        """
        template = Template()
        xsd = (
            '<xs:schema xmlns:xs="http://www.w3.org/2001/XMLSchema">'
            '<xs:element name="tag"></xs:element></xs:schema>'
        )
        template.content = xsd
        template.hash = ""
        template.filename = "filename"
        self.template = template.save()


class QueryDataFixtures(DataFixtures):
    """UserMetadata fixtures"""

    def generate_data_collection(self):
        """Generate a UserMetadata collection.

        Returns:

        """
        content_1 = {
            "root": {
                "element": "value",
                "list": [{"element_list_1": 1}, {"element_list_2": 2}],
                "complex": {"child1": "test", "child2": 0},
            }
        }
        content_2 = {"root": {"element": "value2"}}
        # NOTE: no xml_content to avoid using unsupported GridFS mock
        self.data_1 = UserMetadata(
            template=self.template, user_id="1", dict_content=content_1, title="title"
        ).save()
        self.data_2 = UserMetadata(
            template=self.template, user_id="2", dict_content=content_2, title="title2"
        ).save()
        self.data_collection = [self.data_1, self.data_2]


class AccessControlDataFixture(FixtureInterface):
    """Access Control UserMetadata fixture"""

    USER_1_NO_WORKSPACE = 0
    USER_2_NO_WORKSPACE = 1
    USER_1_WORKSPACE_1 = 2
    USER_2_WORKSPACE_2 = 3

    template = None
    workspace_1 = None
    workspace_2 = None
    data_collection = None
    data_1 = None
    data_2 = None
    data_3 = None
    data_4 = None
    data_5 = None

    def insert_data(self):
        """Insert a set of UserMetadata.

        Returns:

        """
        # Make a connexion with a mock database
        self.generate_template()
        self.generate_workspace()
        self.generate_data_collection()

    def generate_data_collection(self):
        """Generate a UserMetadata collection.

        Returns:

        """

        content = {"root": {"element": "value2"}}

        self.data_1 = UserMetadata(
            template=self.template, title="Data 1", user_id="1"
        ).save()
        self.data_2 = UserMetadata(
            template=self.template, title="Data 2", user_id="2"
        ).save()
        self.data_3 = UserMetadata(
            template=self.template,
            title="Data 3",
            user_id="1",
            workspace=self.workspace_1.id,
            dict_content=content,
        ).save()
        self.data_4 = UserMetadata(
            template=self.template,
            title="DataDoubleTitle",
            user_id="2",
            workspace=self.workspace_2.id,
        ).save()
        self.data_5 = UserMetadata(
            template=self.template,
            title="DataDoubleTitle",
            user_id="1",
            workspace=self.workspace_1.id,
        ).save()
        self.data_collection = [
            self.data_1,
            self.data_2,
            self.data_3,
            self.data_4,
            self.data_5,
        ]

    def generate_template(self):
        """Generate an unique Template.

        Returns:

        """
        template = Template()
        xsd = (
            '<xs:schema xmlns:xs="http://www.w3.org/2001/XMLSchema">'
            '<xs:element name="tag"></xs:element></xs:schema>'
        )
        template.content = xsd
        template.hash = ""
        template.filename = "filename"
        self.template = template.save()

    def generate_workspace(self):
        """Generate the workspaces.

        Returns:

        """
        self.workspace_1 = Workspace(
            title="Workspace 1", owner="1", read_perm_id="1", write_perm_id="1"
        ).save()
        self.workspace_2 = Workspace(
            title="Workspace 2", owner="2", read_perm_id="2", write_perm_id="2"
        ).save()

    def generate_workspace_with_perm(self):
        """Generate the workspaces and the perm object.

        Returns:

        """
        try:
            self.workspace_1 = workspace_api.create_and_save("Workspace 1")
            self.workspace_2 = workspace_api.create_and_save("Workspace 2")
            self.data_3.workspace = self.workspace_1
            self.data_4.workspace = self.workspace_2
            self.data_5.workspace = self.workspace_1
        except Exception as e:
            print(str(e))


class DataMigrationFixture(FixtureInterface):
    """UserMetadata Template Fixture"""

    template_1 = None
    template_2 = None
    template_3 = None
    data_collection = None
    data_1 = None
    data_2 = None
    data_3 = None
    data_4 = None
    data_5 = None

    def insert_data(self):
        """Insert a set of UserMetadata.

        Returns:

        """
        # Make a connexion with a mock database
        self.generate_template()
        self.generate_data_collection()

    def generate_data_collection(self):
        """Generate a UserMetadata collection.

        Returns:

        """
        self.data_1 = UserMetadata(
            template=self.template_1, title="UserMetadata 1", user_id="1"
        )
        self.data_1.xml_content = '<root xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"> \
                                    <test>test</test> \
                                  </root>'
        self.data_1.save()

        self.data_2 = UserMetadata(
            template=self.template_1, title="UserMetadata 2", user_id="1"
        )
        self.data_2.xml_content = '<root xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"> \
                                    <test>test</test> \
                                  </root>'
        self.data_2.save()

        self.data_3 = UserMetadata(
            template=self.template_2, title="UserMetadata 3", user_id="1"
        )
        self.data_3.xml_content = '<root xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"> \
                                    <test>test</test> \
                                  </root>'

        self.data_3.save()

        self.data_4 = UserMetadata(template=self.template_3, title="Data4", user_id="1")
        self.data_4.xml_content = '<root xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"> \
                                    <other>test</other> \
                                  </root>'
        self.data_4.save()

        self.data_5 = UserMetadata(template=self.template_3, title="Data5", user_id="1")
        self.data_5.xml_content = '<root xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"> \
                                    <other>test</other> \
                                  </root>'
        self.data_5.save()

        self.data_collection = [
            self.data_1,
            self.data_2,
            self.data_3,
            self.data_4,
            self.data_5,
        ]

    def generate_template(self):
        """Generate an unique Template.

        Returns:

        """
        template1 = Template()
        template2 = Template()
        template3 = Template()
        xsd1 = '<xsd:schema xmlns:xsd="http://www.w3.org/2001/XMLSchema"> \
                <xsd:element name="root" type="simpleString"/> \
                <xsd:complexType name="simpleString"> \
                    <xsd:sequence> \
                    <xsd:element name="test" type="xsd:string"/></xsd:sequence> \
                </xsd:complexType> \
            </xsd:schema>'
        xsd2 = '<xsd:schema xmlns:xsd="http://www.w3.org/2001/XMLSchema"> \
                <xsd:element name="root" type="simpleString"/> \
                <xsd:complexType name="simpleString"> \
                    <xsd:sequence> \
                    <xsd:element name="test" type="xsd:string"/></xsd:sequence> \
                </xsd:complexType> \
            </xsd:schema>'
        xsd3 = '<xsd:schema xmlns:xsd="http://www.w3.org/2001/XMLSchema"> \
                <xsd:element name="root" type="simpleString"/> \
                <xsd:complexType name="simpleString"> \
                    <xsd:sequence> \
                    <xsd:element name="other" type="xsd:string"/></xsd:sequence> \
                </xsd:complexType> \
            </xsd:schema>'
        template1.content = xsd1
        template1.hash = ""
        template1.filename = "filename"
        template2.content = xsd2
        template2.hash = ""
        template2.filename = "filename"
        template3.content = xsd3
        template3.hash = ""
        template3.filename = "filename"
        self.template_1 = template1.save()
        self.template_2 = template2.save()
        self.template_3 = template2.save()
