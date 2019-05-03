import vk_api

file = open('C:\\Users\\denis\\Desktop\\Python 3\\vk_mes_bot\\accounts.txt','r')

a = file.readlines() # we have array of arrays [[l:p],[l2:p2]]
choose = input("What do you want to like? \n(post, photo, video)? ")
link = input("Enter your link here: ")

_item_id = []
_owner_id = []

if choose == "post":
	y = link.find("=")
	indx = 5

	while link[y+indx] != '_':
		_owner_id.append(link[y+indx])
		indx += 1

	_item_id = link[y+indx+1:]
		
elif choose == "photo":
	y = link.find("=")
	indx = 6

	while link[y+indx] != '_':
		_owner_id.append(link[y+indx])
		indx += 1

	while link[y+indx+1] != '%':
		_item_id.append(link[y+indx+1])
		indx += 1

elif choose == "video":
	y = link.find("z")
	indx = 7
	
	while link[y+indx] != '_':
		_owner_id.append(link[y+indx])
		indx += 1

	while link[y+indx+1] != '%':
		_item_id.append(link[y+indx+1])
		indx += 1

for x in a:

	buff = x.split(":") # separating array
	login = buff[0]
	password = buff[1].replace("\n", "")

	vk_session = vk_api.VkApi(login, password)
	
	try:
		vk_session.auth(token_only=True)
	except vk_api.AuthError as error_msg:
		print(error_msg)

	vk = vk_session.get_api()
	print("_owner_id =" +"".join(_owner_id) +". And _item_id =" +"".join(_item_id))
	print(vk.likes.add(type = choose, owner_id = "".join(_owner_id), item_id = "".join(_item_id)))