import requests
import random

withOptions = []


def get_status():
    info = requests.get('http://10.42.0.1:5000/game/kz912/donuts/get_status')
    return info.json()


def login():
    r = requests.post('http://10.42.0.1:5000/login/kz912/donuts')
    print(r.text)


def reset():
    r = requests.post('http://10.42.0.1:5000/game/kz912/donuts/reset')
    print(r.text)


def tick():
    requests.post('http://10.42.0.1:5000/game/kz912/donuts/tick')
    print(get_status())
    if get_status()['number_of_options'] > 1:
        withOptions.append([get_status()['player_position'], get_status()['options']])

        for index in range(len(get_status()['options'])):
            if(get_status()['options'][index].find('Lung') != -1):
                direct(index)
                break

        index = random.randint(0, get_status()['number_of_options']-1)
        direct(index)


def direct(index):
    requests.post('http://10.42.0.1:5000/game/kz912/donuts/select_direction/' + str(index))
    print(get_status())
    tick()


def hold():
    requests.post('http://10.42.0.1:5000/game/kz912/donuts/start_holding')
    print(get_status())


def stop_hold():
    requests.post('http://10.42.0.1:5000/game/kz912/donuts/stop_holding')
    print(get_status())

def seen():
    turns_held = 0
    while turns_held < 7 and get_status()['bot_visible'] == True:
        if get_status()['options'] == get_status()['bot_location']:
            tick()
        if get_status()['player_position'] == get_status()['bot_location']:
            break
        hold()
        tick()
        turns_held += 1




def main():
    reset()
    #login()
    #while get_status()['bot_visible'] != True:
        #tick()
    #seen()
    #print("bye")



if __name__ == "__main__":
    main()
