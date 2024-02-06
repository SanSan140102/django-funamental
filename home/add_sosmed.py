

from home.models import SosialMedia

def add_social_media(name, link):
    social_media = SosialMedia(name=name,link=link)
    social_media.save()

# Example usage:
add_social_media('Instagram', 'https://www.instagram.com/mhd_.ihsan?igsh=cTVqcDBjeGdneGx3')
add_social_media('Twitter', 'https://twitter.com/angkusans?t=dFUhW-W5nI3HyWhyQ5xFAw&s=08')

