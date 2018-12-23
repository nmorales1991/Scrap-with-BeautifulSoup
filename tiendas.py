from utils import get_store_class_by_name
from listado_tiendas import Listado

def get_producto_categoria(tienda):
	
	for categoria in store.categorias():
			get_producto_url(categoria,tienda)
			
def get_producto_url(categoria,tienda):
	print(categoria)
	for url in store.url_por_categoria(categoria):
		#print(store.leer_urls(url,tienda,categoria))
		producto = store.leer_urls(url,tienda,categoria)
		#print(producto)
		if producto!="no":
			producto.guardarProductos()
			producto.guardarPrecios()

for nombre,tienda in Listado.tiendas():
	store = get_store_class_by_name(nombre)
	get_producto_categoria(tienda)


