import requests
import datetime



class BotHandler:
    def __init__(self, token):
            self.token = token
            self.api_url = "https://api.telegram.org/bot{}/".format(token)

    #url = "https://api.telegram.org/bot<token>/"

    def get_updates(self, offset=0, timeout=30):
        method = 'getUpdates'
        params = {'timeout': timeout, 'offset': offset}
        resp = requests.get(self.api_url + method, params)
        result_json = resp.json()['result']
        return result_json

    def send_message(self, chat_id, text):
        params = {'chat_id': chat_id, 'text': text, 'parse_mode': 'HTML'}
        method = 'sendMessage'
        resp = requests.post(self.api_url + method, params)
        return resp

    def get_first_update(self):
        get_result = self.get_updates()

        if len(get_result) > 0:
            last_update = get_result[0]
        else:
            last_update = None

        return last_update


token = '793364235:AAH9oWWbiA4delfWF09o_4V1po5G4dzxOSA' #Token of your bot
magnito_bot = BotHandler(token) #Your bot's name


i=0
def main():
    new_offset = 0
    print('hi, now launching...')

    while True:
        all_updates=magnito_bot.get_updates(new_offset)

        if len(all_updates) > 0:
            for current_update in all_updates:
                print(current_update)
                first_update_id = current_update['update_id']
                if 'text' not in current_update['message']:
                    first_chat_text='New member'
                else:
                    first_chat_text = current_update['message']['text']
                first_chat_id = current_update['message']['chat']['id']
                if 'first_name' in current_update['message']:
                    first_chat_name = current_update['message']['chat']['first_name']
                elif 'new_chat_member' in current_update['message']:
                    first_chat_name = current_update['message']['new_chat_member']['username']
                elif 'from' in current_update['message']:
                    first_chat_name = current_update['message']['from']['first_name']
                else:
                    first_chat_name = "unknown"

                if first_chat_text == "Hi" or first_chat_text =="hi" or first_chat_text =="Hey" or first_chat_text =="hey" or first_chat_text =="Hello" or first_chat_text =="hello" or first_chat_text =="Sup" or first_chat_text =="sup":

                    magnito_bot.send_message(first_chat_id, "Hey There! " + first_chat_name)
                    new_offset = first_update_id + 1
                elif first_chat_text == "Hmm":

                    magnito_bot.send_message(first_chat_id, "How can I help you ! "+ first_chat_name)
                    new_offset = first_update_id + 1
                elif first_chat_text == "How are you" or first_chat_text == "How's it going" or first_chat_text == "how are you":
                    magnito_bot.send_message(first_chat_id, "Fine 😁 "+"\nWhat is your profession? "+"\n1) Teacher or Lecturer"+"\n2) Businessman"+"\n3) Student")
                    new_offset = first_update_id + 1
                elif first_chat_text == "Teacher" or first_chat_text =="teacher" or first_chat_text =="businessman" or first_chat_text =="Businessman" or first_chat_text =="Student" or first_chat_text =="student":
                    if first_chat_text == "Teacher" or first_chat_text =="teacher" :
                        magnito_bot.send_message(first_chat_id, "You might be a favourite😍 one for your students😏 "+first_chat_name)
                        new_offset = first_update_id +1
                    elif first_chat_text == "Businessman" or first_chat_text =="businessman":
                        magnito_bot.send_message(first_chat_id,"You might the richest🤑 one in the world "+"\nIf not U will surely become one of them.")
                        new_offset = first_update_id +1
                    elif first_chat_text == "Student" or first_chat_text =="student":
                        magnito_bot.send_message(first_chat_id,"Student of which University?")
                        new_offset = first_update_id +1
                elif first_chat_text == "Bennett University":
                    magnito_bot.send_message(first_chat_id,"OH!!!😱 It's one of the top university in India" + "\nWhich branch?")
                    new_offset = first_update_id +1
                elif first_chat_text == "CSE" or first_chat_text == "Cse":
                    magnito_bot.send_message(first_chat_id,"Who's your CSE professor?")
                    new_offset = first_update_id +1
                elif first_chat_text == "Shivani goel":
                    magnito_bot.send_message(first_chat_id,"She teaches Excllent")
                    new_offset = first_update_id +1
                elif first_chat_text == "Really":
                    magnito_bot.send_message(first_chat_id,"Wat else Had your snacks?")
                    new_offset = first_update_id +1
                elif first_chat_text == "Yeah":
                    magnito_bot.send_message(first_chat_id,"I'll also have my snacks🍕🍔🍺"+"I will talk to u later.")
                    new_offset = first_update_id +1
                
                elif first_chat_text == "Ok have your snacks":
                    magnito_bot.send_message(first_chat_id,"Bye "+"Had a great time talking to u")
                    new_offset = first_update_id +1
                elif first_chat_text == "Bye":
                    magnito_bot.send_message(first_chat_id,"Bye")
                    new_offset = first_update_id +1



if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        exit()