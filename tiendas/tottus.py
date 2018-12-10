import urllib
from bs4 import BeautifulSoup
from producto import Producto
from utils import session_with_proxy

class Tottus():
	def categorias():
		return[
			'Conservas',
			'Aceites y Vinagres',
			'Pastas y Salsas',
			'Arroz y Legumbres',
			'Condimentos y Aderezos',
			'Harinas, Puré y Sopas',
			'Alimentos Saludables',
			'Cóctel y Snacks',
			'Leches Líquidas',
			'Leches en Polvo',
			'Cereales',
			'Café y Té',
			'Azúcar/Endulzantes y Mermeladas',
			'Panadería y Pastelería',
			'Galletas/Caramelos y Chocolates',
			'Colaciones y Galletas',
			'Vacuno',
			'Pollo',
			'Pavo',
			'Cerdo',
			'Cordero',
			'Asado',
			'Fiambrería',
			'Quesos',
			'Yoghurt y Postres',
			'Mantequillas y Huevos',
			'Frutas',
			'Verduras',
			'Frutos Secos',
			'Pescado y Mariscos',
			'Vegetales Congelados',
			'Pizzas y Comidas',
			'Helados',
			'Carnes y Pollo Congelados',
			'Hielo',
			'Bebidas',
			'Aguas',
			'Jugos',
			'Cervezas',
			'Licores',
			'Vinos Tintos',
			'Vinos Blancos',
			'Espumantes',
			'Cuidado Mujer',
			'Cuidado Capilar',
			'Higiene Bucal',
			'Jabones y Accesorios',
			'Cuidado Hombre',
			'Salud',
			'Papeles',
			'Limpieza Ropa',
			'Limpieza Casa y Baños',
			'Cocina',
			'Accesorios de Limpieza',
			'Bebés y Niños',
			'Alimento Bebé',
			'Juguetería',
			'Electro',
			'Electrodomésticos',
			'Librería',
			'Hogar y Aire Libre',
			'Accesorios Perro',
			'Accesorios Gato',
			'Otras Mascotas',
			'Alimento Perro',
			'Alimento Gato'

		]
	def url_por_categoria(categoria,extra_args=None):
		base_url="http://www.tottus.cl"
		url_extensions = [	
				['Conservas/118.8','118.8','Conservas'],
				['Aceites-y-Vinagres/118.2','118.2','Aceites y Vinagres'],
				['Pastas-y-Salsas/118.5','118.5','Pastas y Salsas'],
				['Arroz-y-Legumbres/118.3','118.3','Arroz y Legumbres'],
				['Condimentos-y-Aderezos/118.16','118.16','Condimentos y Aderezos'],
				['Harinas,-Puré-y-Sopas/118.6','118.6','Harinas, Puré y Sopas'],
				['Alimentos-Saludables/118.13','118.13','Alimentos Saludables'],
				['Cóctel-y-Snacks/118.1','118.1','Cóctel y Snacks'],
				['Leches-Líquidas/118.10','118.10','Leches Líquidas'],
				['Leche-en-Polvo/cat370016','cat370016','Leches en Polvo'],
				['Cereales/116.6','116.6','Cereales'],
				['Café-y-Té/116.1','116.1','Café y Té'],
				['Azúcar-Endulzantes-y-Mermeladas/116.3','116.3','Azúcar/Endulzantes y Mermeladas'],
				['Panaderia-y-Pasteleria/cat360019','cat360019','Panadería y Pastelería'],
				['Galletas-Caramelos-y-Chocolates/117.5','117.5','Galletas/Caramelos y Chocolates'],
				['Colaciones-y-Galletas/116.7','116.7','Colaciones y Galletas'],
				['Vacuno/127.1','127.1','Vacuno'],
				['Pollo/127.4','127.4','Pollo'],
				['Pavo/127.5','127.5','Pavo'],
				['Cerdo/127.2','127.2','Cerdo'],
				['Cordero/127.3','127.3','Cordero'],
				['Asados/10.3','10.3','Asado'],
				['Fiambrería/113.2','113.2','Fiambrería'],
				['Quesos/112.2','112.2','Quesos'],
				['Yoghurt-y-Postres/112.4','112.4','Yoghurt y Postres'],
				['Mantequillas-y-Huevos/112.1','112.1','Mantequillas y Huevos'],
				['Frutas/128.1','128.1','Frutas'],
				['Verduras/128.2','128.2','Verduras'],
				['Frutos-Secos/cat1420059','cat1420059','Frutos Secos'],
				['Pescado-y-Mariscos/cat360039','cat360039','Pescado y Mariscos'],
				['Vegetales/111.3','111.3','Vegetales Congelados'],
				['Pizzas-y-Comidas/111.5','111.5','Pizzas y Comidas'],
				['Helados/111.4','111.4','Helados'],
				['Carnes-y-pollo/110.1','110.1','Carnes y Pollo Congelados'],
				['Hielo/111.1','111.1','Hielo'],
				['Bebidas/114.2','114.2','Bebidas'],
				['Aguas/114.1','114.1','Aguas'],
				['Jugos/114.4','114.4','Jugos'],
				['Cervezas/115.1','115.1','Cervezas'],
				['Licores/115.2','115.2','Licores'],
				['Vinos-Tintos/115.3','115.3','Vinos Tintos'],
				['Vinos-Blancos/115.4','115.4','Vinos Blancos'],
				['Espumantes/115.5','115.5','Espumantes'],
				['Cuidado-Mujer/120.4','120.4','Cuidado Mujer'],
				['Cuidado-Capilar/120.1','120.1','Cuidado Capilar'],
				['Higiene-Bucal/120.2','120.2','Higiene Bucal'],
				['Jabones-y-Accesorios/120.3','120.3','Jabones y Accesorios'],
				['Cuidado-Hombre/120.5','120.5','Cuidado Hombre'],
				['Salud/120.6','120.6','Salud'],
				['Papeles/41.1','41.1','Papeles'],
				['Limpieza-Ropa/41.2','41.2','Limpieza Ropa'],
				['Limpieza-Casa-y-Baños/41.3','41.3','Limpieza Casa y Baños'],
				['Cocina/cat230046','cat230046','Cocina'],
				['Accesorios-de-Limpieza/cat230047','cat230047','Accesorios de Limpieza'],
				['Bebés-y-Niños/121.1','121.1','Bebés y Niños'],
				['Alimento-Bebé/118.17','118.17','Alimento Bebé'],
				['Juguetería/124.6','124.6','Juguetería'],
				['Electro/34.2','34.2','Electro'],
				['Electrodomésticos/126.2','126.2','Electrodomésticos'],
				['Libreria/cat660015','cat660015','Librería'],
				['Hogar-y-Aire-Libre/10.1','10.1','Hogar y Aire Libre'],
				['Accesorios-Perro/119.2','119.2','Accesorios Perro'],
				['Accesorios-Gato/9.3','9.3','Accesorios Gato'],
				['Otras-Mascotas/cat320049','cat320049','Otras Mascotas'],
				['Alimento-Perro/119.1','119.1','Alimento Perro'],
				['Alimento-Gato/9.2','9.2','Alimento Gato']
				
			]
		product_urls=[]
				
		for extension,id_extension,categoria_local in url_extensions:
			if categoria_local !=categoria:
				continue

			session = session_with_proxy(extra_args)
			pagina = 0
			while True:
				url_categoria = 'http://www.tottus.cl/tottus/productListFragment/{}/{}?No={}' \
								'&Nrpp=&currentCatId={}'.format(extension,id_extension, pagina , id_extension)
				
				try:
					response = session.get(url_categoria,timeout=15)
				except Exception as x:
					try:
						response = session.get(url_categoria,timeout=15)
					except Exception as x:
						break
				
				if not response.text:
					break
				soup = BeautifulSoup(response.text, 'html.parser')
				name_box = soup.findAll('div', attrs={'class': 'caption-bottom-wrapper'})
			
				if not name_box:
					break
				for name_box in name_box:
					product_url = name_box.find('a')['href']
					product_url = base_url + product_url
					product_urls.append(product_url)
					
				pagina += 15
				
				
		return product_urls


	def leer_urls(product_urls,supermercado,categoria,extra_args=None):
		session = session_with_proxy(extra_args)
		
		try:
			response = session.get(product_urls,timeout=15)
		except Exception as x:
			try:
				response = session.get(product_urls,timeout=15)
			except Exception as x:
				return 'no'
		

		if response.text !="":
			soup = BeautifulSoup(response.text, 'html.parser')
		else:
			return 'no'

		form = soup.find('form', attrs={'data-static': '//www.tottus.cl/static/1524a/'})
		if not form:
			return 'no'
		codigo = form.get('data-productid')
		if not codigo:
			return 'no'

		caption = soup.find('div', {'class': 'caption-description'})
		if not caption:
			return 'no'		
		nombre = caption.find('div',{'class':'title'}).h5
		if not nombre:
			return 'no'
		descripcion = "desc: "+nombre.text.strip()
		product = Producto(
				codigo,
           		nombre.text.strip(),
           		supermercado,
           		categoria,
           		product_urls,
           		0,
           		0,
           		0,
           		0,
           		descripcion
       		 )
		return product







