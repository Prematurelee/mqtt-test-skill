from mycroft import MycroftSkill, intent_file_handler


class MqttTest(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_file_handler('test.mqtt.intent')
    def handle_test_mqtt(self, message):
        self.speak_dialog('test.mqtt')


def create_skill():
    return MqttTest()

