
import random, string


def generate_key(length=48):
    '''
    Returns a random sequence of characters of length.
    '''

    chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'

    return ''.join([random.choice(chars) for _ in range(length)])

