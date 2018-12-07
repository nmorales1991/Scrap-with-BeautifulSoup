import urllib
from bs4 import BeautifulSoup
from producto import Producto
from utils import session_with_proxy

class Lider():
	def categorias():
		return[
			'Vacuno',
			'Pollo',
			'Cerdo',
			'Pavo',
			'Cordero',
			'Pescados y Mariscos',
			'Frutas y Verduras',
			'Fiambres y Embutidos',
			'Leches',
			'Yogurth',
			'Quesos',
			'Huevos y Mantequillas',
			'Bebidas Vegetales',
			'Cremas',
			'Comida Congelada',
			'Helados',
			'Postres Congelados',
			'Postres Refrigerados',
			'Pastas y Salsas',
			'Harinas y Polvos',
			'Arroz y Legumbres',
			'Salsas',
			'Alimentos Instantaneos',
			'Aceites y Aderezos',
			'Coctel y Snacks',
			'Conservas',
			'Repostería',
			'Alimentos Especiales',
			'Alimentación Bebé',
			'Perfumería Bebé',
			'Pañales Bebé',
			'Higiene Bebé',
			'Entretención Bebé',
			'Perro',
			'Gato',
			'Otras Mascotas',
			'Panadería',
			'Cereales',
			'Café Té y Hierbas',
			'Dulces Mermeladas y Manjar',
			'Galletas y Colaciones',
			'Chocolates y Dulces',
			'Postres para Preparar',
			'Pastelería',
			'Aguas',
			'Jugos',
			'Bebidas',
			'Cervezas',
			'Destilados',
			'Coctel y Licores',
			'Vinos y Espumantes',
			'Detergentes',
			'Baño y Cocina',
			'Pisos y Muebles',
			'Papeles',
			'Aerosoles y Desinfectantes',
			'Accesorios Aseo',
			'Cuidado Facial Corporal',
			'Cuidado Capilar',
			'Cuidado Personal',
			'Cuidado Bucal',
			'Cuidado Hombre',
			'Cuidado Mujer',
			'Cuidado Adulto Mayor',
			'Belleza',
			'Salud',
			'Librería',
			'Ferretería y Automóvil',
			'Celebraciones',
			'Aire Libre',
			'Cocina y Hogar',
			'Precios Especiales',
			'Marcas Propias'
		]
	def url_por_categoria(categoria,extra_args=None):
		base_url="https://www.lider.cl"
		url_extensions = [	
				['Carnes-y-Pescados/Vacuno/_/N-1gleruj','Vacuno'],
				['Carnes-y-Pescados/Pollo/_/N-8fisy4','Pollo'],
				['Carnes-y-Pescados/Cerdo/_/N-smtdkg','Cerdo'],
				['Carnes-y-Pescados/Pavo/_/N-k2c2mu','Pavo'],
				['Carnes-y-Pescados/Cordero/_/N-1iidz0s','Cordero'],
				['Congelados-/Pescados-y-Mariscos/_/N-qnjyef','Pescados y Mariscos'],
				['Frescos-Lácteos/Frutas-y-verduras/_/N-1rh1dk8','Frutas y Verduras'],
				['Frescos-Lácteos/Fiambres-y-Embutidos/_/N-gqb8d6','Fiambres y Embutidos'],
				['Frescos-Lácteos/Leches/_/N-1syzw6g','Leches'],
				['Frescos-Lácteos/Yoghurt/_/N-1ywlmf4','Yogurth'],
				['Frescos-Lácteos/Quesos/_/N-3j7e1l','Quesos'],
				['Frescos-Lácteos/Huevos-y-Mantequillas/_/N-squyhq','Huevos y Mantequillas'],
				['Frescos-Lácteos/Bebidas-Vegetales/_/N-xj3z08','Bebidas Vegetales'],
				['Frescos-Lácteos/Cremas/_/N-1ozxmgv','Cremas'],
				['Congelados-/Comidas-Congeladas/Comida-Congelada/_/N-qihlyk','Comida Congelada'],
				['Congelados-/Helados/_/N-ovueji','Helados'],
				['Congelados/Postres/Postres-Congelados/_/N-124opyy','Postres Congelados'],
				['Congelados/Postres/Postres-Refrigerados/_/N-seh8t7','Postres Refrigerados'],
				['Despensa/Pastas-y-Salsas/_/N-pgxorj','Pastas y Salsas'],
				['Despensa/Harinas-y-Polvos/_/N-1w5ocqy','Harinas y Polvos'],
				['Despensa/Arroz-y-Legumbres/_/N-13kg7b2','Arroz y Legumbres'],
				['Despensa/Salsas/_/N-1188opy','Salsas'],
				['Despensa/Alimentos-Instantáneos/_/N-gm6h78','Alimentos Instantaneos'],
				['Despensa/Aceites-y-Aderezos/_/N-qskffs','Aceites y Aderezos'],
				['Despensa/Cóctel-y-Snack/_/N-1o5ibif','Coctel y Snacks'],
				['Despensa/Conservas/_/N-98vkeb','Conservas'],
				['Despensa/Repostería/_/N-1e3xmac','Repostería'],
				['Despensa/Alimentos-Especiales/_/N-1i0ni5w','Alimentos Especiales'],
				['Mundo-Bebe/Alimentacion/_/N-1we5k8g','Alimentación Bebé'],
				['Mundo-Bebe/Perfumeria/_/N-1yt9ipw','Perfumería Bebé'],
				['Mundo-Bebe/Pañales/_/N-m0dwac','Pañales Bebé'],
				['Mundo-Bebe/Accesorios-de-Higiene/_/N-1jkijoc','Higiene Bebé'],
				['Mundo-Bebe/Entretencion/_/N-1pkr8qg','Entretención Bebé'],
				['Mascotas/Perro/_/N-12dc08k','Perro'],
				['Mascotas/Gato/_/N-14sisva','Gato'],
				['Otras-Mascotas/_/N-1gc6ake','Otras Mascotas'],
				['Pan-Frutas-y-Verduras/Panadería/_/N-5fhq6y','Panadería'],
				['Desayunos-y-Panadería/Cereales/Cereales/_/N-e00l8z','Cereales'],
				['Desayunos-y-Panadería/Café-Té-y-Hierbas/_/N-wauza0','Café Té y Hierbas'],
				['Desayunos-y-Panadería/Dulces-Mermeladas-y-Manjar/_/N-1j5bt7c','Dulces Mermeladas y Manjar'],
				['Desayunos-y-Panadería/Galletas-y-Colaciones-Dulces/_/N-pbmgle','Galletas y Colaciones'],
				['Desayunos-y-Panadería/Chocolates-y-Candy/_/N-1juh1iq','Chocolates y Dulces'],
				['Desayunos-y-Panadería/Postres-para-Preparar/_/N-6vmfx7','Postres para Preparar'],
				['Desayunos-y-Panadería/Pastelería/_/N-qg627','Pastelería'],
				['Bebidas-Licores/Aguas/_/N-1227rw1','Aguas'],
				['Bebidas-Licores/Jugos/_/N-oz9aq9','Jugos'],
				['Bebidas-Licores/Bebidas/_/N-o65v3z','Bebidas'],
				['Bebidas-Licores/Cervezas/_/N-1mi8n3m','Cervezas'],
				['Bebidas-Licores/Destilados/_/N-7n2dag','Destilados'],
				['Bebidas-Licores/Coctel-y-Licores/_/N-8rxdu7','Coctel y Licores'],
				['Bebidas-Licores/Vinos-y-Espumantes/_/N-she0ig','Vinos y Espumantes'],
				['Limpieza-Aseo/Detergentes/_/N-f3yzpu','Detergentes'],
				['Limpieza-Aseo/Baño-y-Cocina/_/N-mfbfi0','Baño y Cocina'],
				['Limpieza-Aseo/Pisos-y-Muebles/_/N-fotifz','Pisos y Muebles'],
				['Limpieza-Aseo/Papeles/_/N-ncfsxl','Papeles'],
				['Limpieza-Aseo/Aerosoles-y-Desinfectantes/_/N-qr95di','Aerosoles y Desinfectantes'],
				['Limpieza-Aseo/Accesorios-Aseo/_/N-g6eqjj','Accesorios Aseo'],
				['Perfumería-Salud/Cuidado-Facial-Corporal/_/N-1c23u66','Cuidado Facial Corporal'],
				['Perfumería-Salud/Cuidado-Capilar/_/N-u3y2c4','Cuidado Capilar'],
				['Perfumería-Salud/Cuidado-Personal/_/N-1nln3mi','Cuidado Personal'],
				['Perfumería-Salud/Cuidado-Bucal/_/N-hux3cg','Cuidado Bucal'],
				['Perfumería-Salud/Cuidado-Hombre/_/N-1o9q315','Cuidado Hombre'],
				['Perfumería-Salud/Cuidado-Mujer/_/N-1atuxia','Cuidado Mujer'],
				['Perfumería-Salud/Cuidado-Adulto-Mayor/_/N-kl3eff','Cuidado Adulto Mayor'],
				['Perfumería-Salud/Belleza/_/N-u9xnwa','Belleza'],
				['Perfumería-Salud/Salud/_/N-7nnagl','Salud'],
				['Hogar-y-Bazar/Librería/_/N-1tyynyq','Librería'],
				['Hogar-y-Bazar/Ferretería-y-Automóvil/_/N-vzvlz0','Ferretería y Automóvil'],
				['Hogar-y-Bazar/Celebraciones/_/N-19id83g','Celebraciones'],
				['Hogar-y-Bazar/Aire-Libre/_/N-1rlyyc8','Aire Libre'],
				['Hogar-y-Bazar/Cocina-y-Hogar/_/N-77oobg','Cocina y Hogar'],
				['Especiales/Precios-Especiales/_/N-koawk5','Precios Especiales'],
				['Especiales/Marcas-Propias/_/N-tkgbm8','Marcas Propias']
				
			]
		product_urls=[]
		session = session_with_proxy(extra_args)
		
		for extension,categoria_local in url_extensions:
			if categoria_local !=categoria:
				continue

			url_categoria = 'https://www.lider.cl/supermercado/category/' \
                           	'{}?Nrpp=1500'.format(urllib.parse.quote(extension))
						
			try:
				response = session.get(url_categoria,timeout=15)
			except Exception as x:
				#print("entró y lo intenta de nuevo")
				try:
					response = session.get(url_categoria,timeout=15)
				except Exception as x:
					continue
				

			if response.text !="":
				soup = BeautifulSoup(response.text, 'html.parser')
			else:
				continue
			
			name_box = soup.findAll('div', attrs={'class': 'product-details'})
			for name_box in name_box:
				product_url = name_box.find('a')['href']
				if 'https' not in product_url:
					product_url = base_url + urllib.parse.quote(product_url)
				else:
					product_url = urllib.parse.quote(product_url)
				product_urls.append(product_url)
				
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

		codigo = soup.find('span',{'itemprop':'productID'})
		if not codigo:
			return 'no'
			
		nombre = soup.find('span', {'itemprop': 'brand'})
		if not nombre:
			return 'no'
			
		descripcion = soup.find('span', {'itemprop': 'name'})
		if not descripcion:
			return 'no'
			

		precio_actual = soup.find('p', {'itemprop': 'lowPrice'}).get('content')
		if not precio_actual:
			return 'no'
		
		if not soup.find('p', {'itemprop': 'highPrice'}):
			precio_normal = precio_actual
		else:
			precio_normal = soup.find('p', {'itemprop': 'highPrice'}).get('content')

		product = Producto(
				codigo.text.strip(),
           		nombre.text.strip(),
           		supermercado,
           		categoria,
           		product_urls,
           		precio_normal,
           		precio_actual,
           		precio_actual,
           		precio_actual,
           		descripcion.text.strip()
       		 )
		return product







