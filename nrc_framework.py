import requests

withOptions = []


def get_status():
    info = requests.get('http://10.42.0.1:5000/game/kz912/donuts/get_status')
    return info.json()


def login():
    requests.post('http://10.42.0.1:5000/login/kz912/donuts')
    print(get_status())


def reset():
    requests.post('http://10.42.0.1:5000/game/kz912/donuts/reset')
    print(get_status())


def tick():
    requests.post('http://10.42.0.1:5000/game/kz912/donuts/tick')
    print(get_status())
    if len(get_status()['number_of_options']) > 1:
        withOptions.append([get_status()['player_position'], get_status()['options']])
        index = input("Direction? ")
        direct(index)


def direct(index):
    requests.post('http://10.42.0.1:5000/game/kz912/donuts/select_direction/' + str(index))
    print(get_status())


def hold():
    requests.post('http://10.42.0.1:5000/game/kz912/donuts/start_holding')
    print(get_status())


def stop_hold():
    requests.post('http://10.42.0.1:5000/game/kz912/donuts/stop_holding')
    print(get_status())


def main():
    login()
    #while get_status()['bot_visible'] != True and get_status()['rounds_remaining'] > 1000:
        #tick()
    print("bye")
    reset()


if __name__ == "__main__":
    main()
