import werkzeug
werkzeug.cached_property = werkzeug.utils.cached_property

from flask_restplus import Api

from .namespace_pipeline import ns_1

api = Api(
    title='SlackBot',
    version='1.0',
    description='AIOPs Slack Bot`',
)

api.add_namespace(ns_1)
