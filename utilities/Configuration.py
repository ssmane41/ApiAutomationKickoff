import configparser


def getConfig():
    config = configparser.ConfigParser()
    config.read('/Users/shubhamsureshmane/PycharmProjects/APIAutomationKickoff/utilities/properties.ini')
    return config


def getPass():
    return 'Jaishrikrishna108!'
