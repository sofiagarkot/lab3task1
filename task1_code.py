import json
import twurl
import ssl
import urllib.request, urllib.parse, urllib.error
def types_of_data(file):
    """ (str) -> None
        Prints keys from given json file
    """
    try:
        with open(file) as json_file:
            data = json.load(json_file)
            for p in data["users"]:
                for el in p.keys():
                    print(el)
                break
    except ValueError:
        print("Error")

def get_name_and_return_file(acct):
    """(str) -> None
    Writes information about friends of acct into json-file 'data.json'
    """
    TWITTER_URL = 'https://api.twitter.com/1.1/friends/list.json'
    ctx = ssl.create_default_context()
    ctx.check_hostname = False
    ctx.verify_mode = ssl.CERT_NONE
    url = twurl.augment(TWITTER_URL,
                        {'screen_name': acct, 'count': '5'})
    connection = urllib.request.urlopen(url, context=ctx)
    data = connection.read().decode()

    js = json.loads(data)
    with open('data.json', 'w') as outfile:
        json.dump(js, outfile)

def command(com,file):
    """ (str, str) -> None
    Prints data about users under given key - com
    """
    with open(file) as json_file:
        data = json.load(json_file)
        for p in data["users"]:
            print(com + " is "+ str(p[com]))
            print(" ")

def com_with_name(com, file):
    """ (str, str) -> None
        Prints names of users
        """
    with open(file) as json_file:
        data = json.load(json_file)
        for p in data["users"]:
            print("Name is " + str(p["name"]))
            print(com + " is " + str(p[com]))
            print(" ")

if __name__ == "__main__":
    acct = input("Username : ")
    get_name_and_return_file(acct)
    print("There are following types of data :")
    types_of_data("data.json")
    print_name = int(input("Press <1> if you want names of friends to be displayed for each user and <0> otherwise : "))
    com = input("Type which data do you want to find out : ")
    if print_name == 1:
        com_with_name(com,"data.json")
    else:
        command(com,"data.json")