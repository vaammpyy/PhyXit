import discord
def handle_response(message) -> str:
    p_message=' '.join(message).lower().split()
    if p_message[0] == 'hello':
        return ['Hey there! \n>>> \n2 \n3 \n4 \n5', 't']
    if p_message[0] == 'img':
        # while(True):
            # try: 
        # media = ['vid.mp4', '38891d63301e957da6fc19b732a09caf.jpg']
        return [['vid.mp4','38891d63301e957da6fc19b732a09caf.jpg'], 'm']
            # except:
            #     continue
    return "IDK"