from mycroft import MycroftSkill, intent_file_handler


class ConfigureSwitch(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_file_handler('switch.configure.intent')
    def handle_switch_configure(self, message):
        self.speak_dialog('switch.configure')


def create_skill():
    return ConfigureSwitch()

