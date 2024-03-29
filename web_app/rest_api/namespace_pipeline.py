import os
from flask_restplus import Resource, Namespace, reqparse
from flask import Flask, jsonify, request, make_response
from werkzeug.datastructures import FileStorage
import json
from io import StringIO

from slack_webhook import Slack



ns_1 = Namespace('test')
upload_parser_1 = reqparse.RequestParser()




@ns_1.route('/')
class test2(Resource):
    def post(self):
        result = jsonify(hello="top page") 
        return result

@ns_1.route('/mssg_posted_in_slack')
class test3(Resource):
    def post(self):
        result = request.get_json(force=True)
        print(result)
        if result["type"]== "url_verification":
            response = make_response({"challenge":result["challenge"]},200)
            response.headers["Content-Type"] = "application/json"       
        else:
            response = make_response({"text":"Hello Sampath"},200)
            response.headers["Content-Type"] = "application/json"
        return response

@ns_1.route('/post_mssg_in_slack')
class test4(Resource):
    def post(self):
        slack = Slack(url='https://hooks.slack.com/services/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')
        return_code = slack.post(blocks=[
            {
            "text": {
                "type": "mrkdwn",
                "text": "\n          🚩 *_Incident detection_*\n\n*Train ticket application*\n*Story 3*\n*Title*:\nts-ticketinfo-service with 4 events\n*Description*:\n_ts-ticketinfo-5XX Internal Server Error_ + 1 alert, 2 log anomalies"
            },
            "type": "section"
            },
            {
            "fields": [
                {
                "type": "mrkdwn",
                "text": "*Status*:\nOpen"
                },
                {
                "type": "mrkdwn",
                "text": "*Severity*:\n3"
                },
                {
                "type": "mrkdwn",
                "text": "*Created*:\n<!date^1594663484^{date_pretty} at {time}|1594663484>\nby <@U011ZLWRGHL>"
                }
            ],
            "type": "section"
            },
            {
            "type": "context",
            "elements": [
                {
                "type": "mrkdwn",
                "text": "Updated <!date^1599369627^{date_pretty} at {time}|1599369627> by <@U011ZLWRGHL>"
                }
            ]
            },
            {
            "type": "divider"
            },
            {
            "text": {
                "type": "mrkdwn",
                "text": "📍 _*<https://localization_url.com|Localization>*_  and  💥 _*<https://blast_radius_url.com|Blast radius>*_"
            },
            "type": "section"
            },
            {
            "type": "context",
            "elements": [
                {
                "type": "mrkdwn",
                "text": "(1), (2), etc. represent distance from localized entities"
                }
            ]
            },
            {
            "fields": [
                {
                "type": "mrkdwn",
                "text": "*Deployment:*\n(1) `ts-ticketinfo-service`"
                },
                {
                "type": "mrkdwn",
                "text": "*Pod:*\n(0) `ts-ticketinfo-service-6d78f6964-w2kn8`\n(1) `ts-basic-service-6cbd4b9bdb-2n6mn`\n(1) `ts-preserve-service-654c875db8-sdtgt`\n(2) `ts-ui-dashboard-674947-kkcwp`"
                }
            ],
            "type": "section"
            },
            {
            "fields": [
                {
                "type": "mrkdwn",
                "text": "*Service:*\n(1) `ts-ticketinfo-service`"
                }
            ],
            "type": "section"
            },
            {
            "type": "actions",
            "elements": [
                {
                "type": "button",
                "text": {
                    "type": "plain_text",
                    "text": "View relationships",
                    "emoji": True
                },
                "action_id": "story_1/5df7d0dc-83f1-11ea-afdb-0242ac1a0009:::viewTopology"
                }
            ]
            },
            {
            "type": "divider"
            },
            {
            "text": {
                "type": "mrkdwn",
                "text": "🔶  _*Relevant events*_"
            },
            "type": "section"
            },
            {
            "type": "context",
            "elements": [
                {
                "type": "plain_text",
                "text": "grouped based on the same resource `tas` within the time window 0:15:00",
                "emoji": True
                }
            ]
            },
            {
            "fields": [
                {
                "type": "mrkdwn",
                "text": "🚨 *Alerts:*\n        2"
                },
                {
                "type": "mrkdwn",
                "text": "📈 *Log anomalies:*\n        2"
                }
            ],
            "type": "section"   
            },
            {
            "type": "actions",
            "elements": [
                {
                "type": "button",
                "text": {
                    "type": "plain_text",
                    "text": "View relevant events",
                    "emoji": True
                },
                "action_id": "story_1/5df7d0dc-83f1-11ea-afdb-0242ac1a0009:::viewEvents"
                },
                {
                "type": "button",
                "text": {
                    "type": "plain_text",
                    "text": "Search recommended actions",
                    "emoji": True
                },
                "action_id": "story_1/5df7d0dc-83f1-11ea-afdb-0242ac1a0009:::searchModal"
                },
                {
                "type": "button",
                "text": {
                    "type": "plain_text",
                    "text": "Edit",
                    "emoji": True
                },
                "action_id": "story_1/5df7d0dc-83f1-11ea-afdb-0242ac1a0009:::startEdit"
                },
                {
                "type": "button",
                "text": {
                    "type": "plain_text",
                    "text": "Dismiss",
                    "emoji": True
                },
                "action_id": "story_1/5df7d0dc-83f1-11ea-afdb-0242ac1a0009:::startDismiss"
                },
                {
                "type": "button",
                "text": {
                    "type": "plain_text",
                    "text": "Acknowledge",
                    "emoji": True
                },
                "action_id": "story_1/5df7d0dc-83f1-11ea-afdb-0242ac1a0009:::startAck",
                "style": "primary"
                }
            ]
            }
        ])
        response = make_response({"status":return_code},200)
        response.headers["Content-Type"] = "application/json"
        return response
       