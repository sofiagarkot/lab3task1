This module is created for work with json-files.
User can easily manage the file by just choosing the parameters he or she wants to find out 
about friends of another user. The current user will be asked to type the nickname, whose friends he or she wants to get.
Then there will be displayed possible keys. To find out values for some key a user should type it. 

List of functions:
types_of_data(file):
    """ 
    (str) -> None
    Prints keys from given json file
    """

get_name_and_return_file(acct):
    """(str) -> None
    Writes information about friends of acct into json-file 'data.json'
    """

command(com,file):
    """ (str, str) -> None
        Prints data about users under given key - com
    """
   

com_with_name(com, file):
    """ (str, str) -> None
        Prints names of user's friends
    """

Example of usage:

Username : elonmusk
There are following types of data :
id
id_str
name
screen_name
location
description
url
entities
protected
followers_count
friends_count
listed_count
created_at
favourites_count
utc_offset
time_zone
geo_enabled
verified
statuses_count
lang
status
contributors_enabled
is_translator
is_translation_enabled
profile_background_color
profile_background_image_url
profile_background_image_url_https
profile_background_tile
profile_image_url
profile_image_url_https
profile_banner_url
profile_link_color
profile_sidebar_border_color
profile_sidebar_fill_color
profile_text_color
profile_use_background_image
has_extended_profile
default_profile
default_profile_image
following
live_following
follow_request_sent
notifications
muting
blocking
blocked_by
translator_type
Press <1> if you want name to be displayed for each user and <0> otherwise : 1
Type which data do you want to find out : lang
Name is The Onion
lang is en
 
Name is Nautilus
lang is en
 
Name is BBC Science News
lang is en
 
Name is Science Magazine
lang is en
 
Name is Nature News & Comment
lang is en
