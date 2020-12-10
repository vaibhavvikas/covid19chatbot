from typing import Any, Text, Dict, List
import logging, json

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
import requests

logger = logging.getLogger(__name__)


class ActionFaqDistancing(Action):
    def name(self) -> Text:
        return "action_faq_distancing"

    def run(
        self,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any],
    ) -> List[Dict[Text, Any]]:
        intent = tracker.latest_message["intent"].get("name")

        logger.debug("Detected FAQ intent: {}".format(intent))

        if intent in ["faq_distancing"]:
            text = """Social distancing is a public health practice that aims to prevent sick people 
            from coming in close contact with healthy people in order to reduce opportunities for disease transmission. 
            It can include large-scale measures like canceling group events or closing public spaces, as well as individual 
            decisions such as avoiding crowds."""
            message = {
                "type": "image",
                "payload": {
                    "title": "Social Distancing",
                    "src": "https://www.covidoumedicine.com/images/content/covid-19-curves.gif",
                },
            }
            dispatcher.utter_message(text=text, attachment=message)
        return []


class ActionFaqSpread(Action):
    def name(self) -> Text:
        return "action_faq_spread"

    def run(
        self,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any],
    ) -> List[Dict[Text, Any]]:
        intent = tracker.latest_message["intent"].get("name")

        logger.debug("Detected FAQ intent: {}".format(intent))

        if intent in ["faq_spread"]:
            message = {
                "type": "video",
                "payload": {
                    "title": "Steps to Prevent COVID-19",
                    "src": "https://www.youtube.com/embed/1APwq1df6Mw",
                },
            }
            dispatcher.utter_message(
                text="Take steps to lower your risk of getting sick with COVID-19. This is how Covid-19 spreads and here are some things you should do.",
                attachment=message,
            )
        return []


class ActionFaqSymptoms(Action):
    def name(self) -> Text:
        return "action_faq_symptoms"

    def run(
        self,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any],
    ) -> List[Dict[Text, Any]]:
        intent = tracker.latest_message["intent"].get("name")

        logger.debug("Detected FAQ intent: {}".format(intent))

        if intent in ["faq_symptoms"]:
            message = {
                "type": "video",
                "payload": {
                    "title": "COVID-19 Animation: What Happens If You Get Coronavirus?",
                    "src": "https://www.youtube.com/embed/5DGwOJXSxqg",
                },
            }
            dispatcher.utter_message(
                text="People with COVID-19 generally develop signs and symptoms, including mild respiratory symptoms and fever, on an average of 5-6 days after infection (mean incubation period 5-6 days, range 1-14 days). Most people infected with COVID-19 virus have mild disease and recover.",
                attachment=message,
            )
        return []


class ActionFaqStatus(Action):
    def name(self) -> Text:
        return "action_faq_status"

    def run(
        self,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any],
    ) -> List[Dict[Text, Any]]:
        intent = tracker.latest_message["intent"].get("name")

        logger.debug("Detected FAQ intent: {}".format(intent))

        if intent in ["faq_status"]:
            message = {
                "type": "video",
                "payload": {
                    "title": "[LIVE] Coronavirus Pandemic: Real Time Counter, World Map, News",
                    "src": "https://www.youtube.com/embed/NMre6IAAAiU",
                },
            }
            dispatcher.utter_message(attachment=message)
        return []

class ActionDefaultFallback(Action):
    def name(self) -> Text:
        return "action_default_fallback"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        
        text = list(map(str, tracker.latest_message['text'].split()))
        appendedtext = "+".join(text)
        searchtext = "Sorry! I cant understand. Here is a google search [Link](" + "https://www.google.com/search?q=" + appendedtext + ")"
        dispatcher.utter_message(text=searchtext)

        return []


class ActionCovidStateStatus(Action):
    def name(self) -> Text:
        return "action_corona_state_status"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        
        response = requests.get("https://api.covid19india.org/data.json").json()

        entities = tracker.latest_message["entities"]

        state = None
        for e in entities:
            if e['entity'] == 'state':
                state = (e['value']).lower()

        if state == "india": state = "Total"

        message = "Please enter correct state name."

        if state:
            for data in response["statewise"]:
                if data["state"] == state.title():
                    message = "Status of " + state.title() + "\n Active: " + data["active"] + " Confirmed: " + data["confirmed"] + " Recovered: " + data["recovered"]

        dispatcher.utter_message(text=message)

        return []
