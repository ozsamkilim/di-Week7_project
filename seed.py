from app import db
from app import Table, MenuItem


db.create_all()


def create_tables():
	'''Create 10 Table objects, and commit to database.'''
	for i in range(1,10):
		table = Table()
		db.session.add(table)
	db.session.commit()



def create_menu_items(name,price,image):
	'''Create a few menu items.'''
	menu = MenuItem(
		name = name,
		price = price,
		image = image
		)
	db.session.add(menu)
	db.session.commit()


create_tables()
create_menu_items('late', 6, 'https://upload.wikimedia.org/wikipedia/commons/thumb/3/30/Koffie_verkeerd_cafe_MP_Amsterdam.jpg/1200px-Koffie_verkeerd_cafe_MP_Amsterdam.jpg')
create_menu_items('cappacino', 5, 'https://www.caffesociety.co.uk/assets/recipe-images/latte-small.jpg')
