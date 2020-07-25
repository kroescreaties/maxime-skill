from mycroft import MycroftSkill, intent_file_handler


class Maxime(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_file_handler('maxime.intent')
    def handle_maxime(self, message):
        self.speak_dialog('maxime')


def create_skill():
    return Maxime()

