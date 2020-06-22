from nanapy import Nana

nana = Nana()

print(nana.profile)
print(nana.get_user('8419582'))
nana.follow('8419582')
print(nana.get_post('051a72fc'))
print(nana.get_post('85619452', False))
nana.play('051a72fc')
nana.applause('051a72fc')
nana.comment('051a72fc', 'test')
nana.logout()
