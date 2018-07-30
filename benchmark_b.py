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
            if (get_status()['options'][index].find('Heart') != -1):
                direct(index)
                return
            elif (get_status()['options'][index].find('Lung') != -1):
                direct(index)
                return

        index = random.randint(0, get_status()['number_of_options'] - 1)
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


def catch():
    """keep going until you see the bot, go to LungC_0 and stop"""
    while get_status()['bot_visible'] == False:
        tick()

    while get_status()['player_position'] != "LungC_0":
        tick()

    hold()  # bot should run into player at this point

    while get_status()['bot_location'] != "LungC_0 " and get_status()["score"] != 1:
        tick()

    stop_hold()

    return


def main():
    reset()
    login()
    catch()
    print("Succeed! Score:", get_status()["score"])
    reset()
    login()
    catch()
    print("Succeed! Score:", get_status()["score"])
    print("bye")


if __name__ == "__main__":
    main()
