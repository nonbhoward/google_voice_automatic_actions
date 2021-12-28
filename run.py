from googlevoice import Voice
from task.voicemail import VoicemailAction
from task.environment import get_voice_login_details
# initialize voice instance
voice = Voice()
vm_action = VoicemailAction(voice=voice)
login_details = get_voice_login_details()
email = login_details.get('email')
passwd = login_details.get('passwd')
# auth
voice.login(email=email, passwd=passwd)
# perform primary run sequence
