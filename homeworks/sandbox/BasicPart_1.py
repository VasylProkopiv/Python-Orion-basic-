import sys
import datetime

print('Twinkle, twinkle, little star,\n\t How I wonder what you are!\n\t\t Up above the world so high,\n\t\t '
      'Like a diamond in the sky. \nTwinkle, twinkle, little star, \n\t How I wonder what you are')
print(sys.version_info)
now = datetime.datetime.now()
print(now.strftime('%Y-%m-%d %H:%M:%S'))
a = 'hello'
a = a.upper()
print(a)
name = 'World'


def rating(movie, rating):
    result = f'{movie}, {rating}'
    return result



print(rating('lion', 100))
