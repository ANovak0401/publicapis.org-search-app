import sys
import requests
import json
from urllib.parse import urlencode

url_dict = {}


def startup():
    """when program is first started play this message"""
    print("Welcome to the Public Apis Project")
    user_menu()


def user_menu():
    """the main menu for the program"""
    if len(url_dict) > 0:
        print('\ncurrent search criteria: {}'.format(url_dict))
    print("\nMenu:"
          "\n\t1. title keyword search"
          "\n\t2. description keyword search"
          "\n\t3. authorisation required"
          "\n\t4. https protocol"
          "\n\t5. CORS support"
          "\n\t6. category select"
          "\n\t7. search with current criteria"
          "\n\t8. reset search terms and start over"
          "\n\t9. remove search term by key entry"
          "\n\tq. quit")
    user_choice = input('\nPlease enter a number for selection: ')
    choices = ['1', '2', '3', '4', '5', '6', '7', '8', 'q']
    if user_choice == '1':
        k_word_search()
    if user_choice == '2':
        descript_search()
    if user_choice == '3':
        auth_req()
    if user_choice == '4':
        https_req()
    if user_choice == '5':
        cors_supp()
    if user_choice == '6':
        category_select()
    if user_choice == '7':
        url_creator(url_dict)
    if user_choice == '8':
        new_search()
    if user_choice == '9':
        remove_by_index()
    if user_choice == 'q':
        print('\n\nGoodbye')
        sys.exit()
    if user_choice not in choices:
        print("that is not a valid selection, please try again")
        user_menu()


def url_creator(url_dict):
    """create url from url dictionary"""
    base_url = 'https://api.publicapis.org/entries?'
    final_url = f'{base_url}{urlencode(url_dict)}'
    print(f"\nUrl call to api: {final_url}")
    get_dictionary(final_url)


def get_dictionary(url):
    """make call, store response, and print the status code"""
    r = requests.get(url)
    print(f"Status code: {r.status_code}")

    # save response dictionary to a json file
    response_dict = r.json()
    readable_file = 'temp_dict_file.json'
    with open(readable_file, 'w') as f:
        json.dump(response_dict, f, indent=4)

    with open(readable_file) as f:
        print(f.read())
    new_search()


def new_search():
    """asks user if they want to perform a new search"""
    user_choice = input('would you like to perform a new search? y/n: ')
    choices = ['y', 'n']
    if user_choice == 'y':
        url_dict.clear()
        user_menu()
    if user_choice == 'n':
        print('Goodbye')
        sys.exit()
    if user_choice not in choices:
        print('That is not a valid selection')
        new_search()


def remove_by_index():
    """remove entries from url dict via user input"""
    if url_dict:
        print(url_dict)
        user_choice = input('please enter key of entry to be removed: ')
        if user_choice not in url_dict:
            print('that is not a valid entry, please try again.')
            remove_by_index()
        else:
            del url_dict[user_choice]
            user_choice = input('would you like to remove another search term? \ny/n: ')
            choices = ['y', 'n']
            if user_choice == 'y':
                remove_by_index()
            if user_choice == 'n':
                user_menu()
            if user_choice not in choices:
                print('That is not a valid selection')
                remove_by_index()
    else:
        print("\nurl dictionary is empty. returning to main menu")
        user_menu()
                # code breaks if you try to delete an entry from an empty dictionary


def k_word_search():
    """create entry for keyword search"""
    search_keyword = input('please enter search term: ')
    url_dict['title'] = search_keyword
    user_menu()


def descript_search():
    """create entry for keyword in description search"""
    description_keyword = input('please enter search term: ')
    url_dict['description'] = description_keyword
    user_menu()


def auth_req():
    """ create entry for api authorisation search"""
    print('Authorisation protocol menu: \n\t1. all \n\t2. apiKey \n\t3. OAuth \n\t4. X-Mashape-Key \n\t5. No')
    auth_choice = input("please make numerical selection: ")
    choices = ['1', '2', '3', '4', '5']
    if auth_choice == '1':
        url_dict['auth'] = ''
    if auth_choice == '2':
        url_dict['auth'] = 'apiKey'
    if auth_choice == '3':
        url_dict['auth'] = 'OAuth'
    if auth_choice == '4':
        url_dict['auth'] = 'X-Mashape-Key'
    if auth_choice == '5':
        url_dict['auth'] = 'No'
    if auth_choice not in choices:
        print("That is not a valid entry")
        auth_req()
    else:
        user_menu()


def https_req():
    """create entry for https protocol support"""
    print('Require https support?')
    user_choice = input('y/n:')
    choices = ['y', 'n']
    if user_choice == 'y':
        url_dict['https'] = 'true'
    if user_choice == 'n':
        url_dict['https'] = 'false'
    if user_choice not in choices:
        print("that is not a valid entry, please try again.")
        https_req()
    else:
        user_menu()


def cors_supp():
    """create entry for CORS support"""
    print('CORS support for entry?')
    choices = ['1', '2', '3']
    user_choice = input('\n\t1. yes\n\t2. no\n\t3. unknown')
    if user_choice == '1':
        url_dict['cors'] = 'yes'
    if user_choice == '2':
        url_dict['cors'] = 'no'
    if user_choice == '3':
        url_dict['cors'] = 'unknown'
    if user_choice not in choices:
        print("that is not a valid entry, please try again.")
        cors_supp()
    else:
        user_menu()


def category_select():
    print("available categories:"
          "\n\tAnimals",
          "\n\tAnime",
          "\n\tAnti-Malware",
          "\n\tArt & Design",
          "\n\tBooks",
          "\n\tBusiness",
          "\n\tCalendar",
          "\n\tCloud Storage & File Sharing",
          "\n\tContinuous Integration",
          "\n\tCryptocurrency",
          "\n\tCurrency Exchange",
          "\n\tData Validation",
          "\n\tDevelopment",
          "\n\tDictionaries",
          "\n\tDocuments & Productivity",
          "\n\tEnvironment",
          "\n\tEvents",
          "\n\tFinance",
          "\n\tFood & Drink",
          "\n\tGames & Comics",
          "\n\tGeocoding",
          "\n\tGovernment",
          "\n\tHealth",
          "\n\tJobs",
          "\n\tMachine Learning",
          "\n\tMusic",
          "\n\tNews",
          "\n\tOpen Data",
          "\n\tOpen Source Projects",
          "\n\tPatent",
          "\n\tPersonality",
          "\n\tPhotography",
          "\n\tScience",
          "\n\tSecurity",
          "\n\tShopping",
          "\n\tSocial",
          "\n\tSports & Fitness",
          "\n\tTest Data",
          "\n\tText Analysis",
          "\n\tTracking",
          "\n\tTransportation",
          "\n\tURL Shorteners",
          "\n\tVehicle",
          "\n\tVideo",
          "\n\tWeather")
    user_choice = input('please enter a selection: ')
    url_dict['category'] = user_choice
    user_menu()
    # rebuild this functon to call the api and return a dictionary of categories so user can select from live list.
    # then no need to update.


startup()
