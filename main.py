# written by Mani Raj Yadav
# starting the SpyChat
# importing details from spy_details
#COMMENT ADDED BY MONICA SINGH TO CHECK IF PULL REQUEST WORKS?
from spy_details import spy, friends, Spy, ChatMessage
from steganography.steganography import Steganography
from termcolor import colored

# creating list lists
STATUS = ["Hey there, I am using SpyChat!", "On a secret Mission!", "Tired!!"]

# lets start
print "Let's get started!!"

question = "Do you want to continue as " + spy.salutation + " " + spy.name + "(Y/N)."
answer = raw_input(question)


# function to check validation of name
def check_validity(name):
    # to check whether user has actually entered something and the entered stuff is acceptable as name
    if len(name) > 0 and name.isspace() != True and name.isalpha() == True:
        return True
    else:
        print "Invalid Name!!!"


# function to get and set name of spy
def get_name():
    salutation = ''

    name = raw_input("First Name:")
    last_name = raw_input("Last Name:")

    validity_first = check_validity(name)
    validity_second = check_validity(last_name)

    # if both the entered names are valid then concatenating them
    if validity_first and validity_second:
        name = name + " " + last_name

        # getting the salutation
        print "Select salutation:\n"

        print "1.Mr. \ 2.Mrs. \ 3. Miss"
        sal = int(raw_input("Select the appropriate option."))
        if 0 < sal <= 3:
            if sal == 1:
                salutation = "Mr."
            elif sal == 2:
                salutation = "Mrs."
            elif sal == 3:
                salutation = "Miss"

            # concatenating salutation with the name of the spy
            name = salutation + " " + name
            return name

        else:
            print "You did not choose appropriate option!"

    else:
        print "Type a valid name!!"


# function to select a friend
def select_friend():

    s_no = 1
    # showing the list of friends

    for friend in friends:
        print """Your online friends are:
        %d.%s, age:%d, rating:%f""" % (s_no, friend.name, friend.age, friend.rating)
        s_no += 1

    # accepting the desired choice
    choice = raw_input("Choose from your friends")

    # check whether the entered serial no. of friend is present
    if int(choice) <= len(friends):
        # converting the choice in int and then converting it in the proper index of friend
        choice_index = int(choice) - 1
        # displaying the friend chosen
        print "You chose %s, age:%d, rating:%f" % (
        friends[choice_index].name, friends[choice_index].age, friends[choice_index].rating)
        # returning the index of the chosen friend
        return choice_index

    # if the entered serial no. is not valid
    else:
        print "you did not choose valid friend!"


# function to send message
def send_message():

    # making user choose the friend to send message
    friend_choice = select_friend()

    # implementing steganography encoding message
    original_image = raw_input("What is the name of the image?")
    output_path = raw_input("What name do you want for image your friend receive?")
    text = raw_input("What do you want to say?")
    Steganography.encode(original_image, output_path, text)

    new_chat = ChatMessage(text, True)

    # saving the text message sent by user to corresponding friend
    friends[friend_choice].chats.append(new_chat)

    print "Your secret message image is ready!"


# function to read the messages from a particular friend
def read_message():

    # making user choose the friend to send message
    sender = select_friend()

    # impementing steganography decoding message
    output_path = raw_input("What is the name of the file?")

    secret_text = Steganography.decode(output_path)

    if str(secret_text).isspace():
        print "This image contains no message!!"
    else:
        new_chat = ChatMessage(secret_text, False)
        # saving thereceived message from corresponding friend
        friends[sender].chats.append(new_chat)

        # checking for some specific words in message to generate special prompt
        if 'TTYL' in str(secret_text).upper():
            print colored("Your Spy friend will 'Talk To You Later!'", 'red', attrs=['bold'])
        if 'SOS' in str(secret_text).upper():
            print colored("Your spy friend is in extreme danger!! SAVE!", 'red', attrs=['bold'])
        if 'HELP' in str(secret_text).upper():
            print colored("Your friend needs your HELP!!!", 'red', attrs=['bold'])
        if 'ON A MISSION' in str(secret_text).upper():
            print colored("Your friend is on a Mission!!", 'red', attrs=['bold'])

        print "Your secret message has been saved!"


# function to add status
def add_status(current_status_message):

    # variabe to show updated status
    update_status_message = None

    # checking for current status
    if current_status_message != None:
        print "Your current status message is:", colored( current_status_message, 'blue', attrs=['bold'] )

    else:
        print "You don't have any status message currently \n"

    # asking the user whether they want to upload a new status or choose from older ones
    default = raw_input("Do you want to select from the older status (y/n)?")

    # upload new status
    if default.upper() == "N":
        # taking new status from user
        new_status_message = raw_input("What status message do you want to set? ")
        # saving the new status
        if len(new_status_message) > 0:
            STATUS.append(new_status_message)
            update_status_message = new_status_message

    # select from older status
    elif default.upper() == "Y":
        # showing status list
        for i in STATUS:
            print "%d.%s" % (STATUS.index(i) + 1, i)
        # selecting status from list
        message_selection = int(raw_input("Choose from above message"))
        # checking for valid selection of the status
        if len(STATUS) >= message_selection:
            update_status_message = STATUS[message_selection - 1]
        else:
            print "You have not chosen correct status"

    else:
        print "The option you chose is not valid. Press either y or n."
    # showing updated message

    if update_status_message:

        print "Your updated status message is:", colored(update_status_message, 'blue', attrs=['bold'])

    else:
        print "You did not update your message!"

    return update_status_message


# function to add friend
def add_friend():

    # adding a blank friend
    new_friend = Spy('', '', 0, 0.0)

    print "Fill the details of your friend."
    # getting the name of friend and also checking validation

    new_friend.name = get_name()
    # if valid name succesfully received getting futher details and converting in respective data types
    if new_friend.name:
        new_friend.age = int(raw_input("Whats your friend's age?"))

        # checking for validation of age
        if new_friend.age > 12:
            new_friend.rating = float(raw_input("Whats your friend's spy rating?"))
            if new_friend.rating >= spy.rating:
                # changing the online status of friend
                new_friend.online = True
                # adding and saving the new friend to friend list
                friends.append(new_friend)

                print "Friend Added"

            else:
                print "Your friend's rating is less than yours and hence we cannot add your friend!"
        # if the age of spy is not fit

        else:
            print "Your friend's age is not fit to be a spy."

    # if the name is not valid
    else:
        print "Sorry!!We cannot add your friend as you provided an invalid name."
    # returning number of friends

    return len(friends)


# function to read all chats from a friend
def read_chat_history():

    word = 0
    c = 0

    # letting user choose the friend
    friend_choice = select_friend()

    # displaying chats
    for chat in friends[friend_choice].chats:

        # messages sent by user
        if chat.sent_by_me:
            # printing the message and time in given colored format
            print colored(chat.time.strftime("%d %B %Y"),'blue'),colored('~','blue'),colored('You:','red',attrs=[
                                                                                                            'bold']),chat.message
        # messages received by user
        else:
            # checking for some specific words in message to generate special prompt
            if 'TTYL' in str(chat.message).upper():
                print "Your Spy friend will 'Talk To You Later!'"
            if 'SOS' in str(chat.message).upper():
                print "I'm in extreme danger!! Save me!!"
            if 'HELP' in str(chat.message).upper():
                print "Your friend needs your HELP!!!"
            if 'ON A MISSION' in str(chat.message).upper():
                print "Your friend is on a Mission!!"

            # printing the message the time and the friend in the given color format
            print colored(chat.time.strftime("%d %B %Y"),'blue'),colored('~','blue'), colored(friends[friend_choice].name,'red',attrs=['bold']),':',chat.message
            messg = str(chat.message)
            # triming whitespaces and tabs from both sides of the message
            messg.strip()

            # counting all words
            for i in range(len(messg)):
                if messg[i] == ' ':
                    word += 1
            # counting messages
            c += 1

    # calculating average words from a friend
    if c > 0:

        avg = word + 1 / c
        print "Average no. of words:%d" % avg
        # removing the friend if its average words are greater than 100
        if avg > 100:
            del friends[friend_choice]
            print "Your friend was speaking too much! We have succesfully deleted your friend from your friend list."

    # showing no message if there isnt any message from the chosen friend yet
    else:
        print "You have no messages from %s yet!!" % friends[friend_choice].name


# starting the chat app and showing the main menu
def start_chat(spy):

    current_status_message = None
    # finally displaying spy information on screen
    print "Authentication Complete! Welcome %s, age :%d and spy rating: %2d" % (spy.name, spy.age, spy.rating)

    show_menu = True
    # letting user choose from the menu

    while show_menu:
        menu_choices = "What do you want to do? \n 1. Add a status update \n 2. Add a friend \n 3. Send a secret message \n 4. Read a secret message \n 5. Read Chats from a user \n 6. Close Application \n"
        menu_choice = raw_input(menu_choices)
        if len(menu_choice) > 0:
            menu_choice = int(menu_choice)

            if menu_choice == 1:
                print "You chose to update status!"
                current_status_message = add_status(current_status_message)

            elif menu_choice == 2:
                print "You chose to add friend."
                number_of_friends = add_friend()
                print "You have %d friends" % number_of_friends

            elif menu_choice == 3:
                print "you chose to send a secret message."
                send_message()

            elif menu_choice == 4:
                print "You chose to read a secret message."
                read_message()

            elif menu_choice == 5:
                print "You chose to read chats from a user."
                read_chat_history()

            else:
                show_menu = False


if answer.upper() == 'Y':
    # calling the function to straight-away start chatting
    start_chat(spy)

else:
    # getting the name of the spy
    print "We would like to know you well.Please fill your details."
    spy.name = get_name()
    print "Welcome " + spy.name + " glad to have you back!"
    # initialising the age, rating and status variables
    spy.age = 0
    spy.rating = 0.0
    spy.online = False
    # getting the age from user
    spy.age = int(raw_input("What's your age?"))
    # checking whether the spy age is in the proper range
    if 12 < spy.age < 50:
        # getting the spy ratings from the user
        spy.rating = float(raw_input("enter your spy rating"))
        # checking for the quality of spy with respect to the spy ratings
        if spy.rating > 4.5:
            print("Great ace!!")
        elif 3.5 < spy.rating <= 4.5:
            print "You are one of the Good ones."
        elif 3.5 >= spy.rating > 2.5:
            print "You can always do better."
        else:
            print "We can use somebody to help in the office."
        # changing online status of spy to True
        spy.online = True
        # calling the function to start chatting
        start_chat(spy)
        # when the spy is not of the given age range
    else:
        print "Your age is not fit to be a spy!"
