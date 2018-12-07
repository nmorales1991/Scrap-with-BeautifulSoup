import urllib
from bs4 import BeautifulSoup
from producto import Producto
from utils import session_with_proxy

class Jumbo():
	def categorias():
		return[
			'Leches Blancas',
			'Leches Cultivadas',
			'Leches Saborizadas',
			'Leches Vegetales',
			'Yoghurt',
			'Postres',
			'Mantequillas y Margarinas',
			'Cremas',
			'Manjar y Dulce de Leche',
			'Huevos',
			'Leche en Polvo',
			'Verduras',
			'Frutas',
			'Frutas y Verduras Orgánicas',
			'Frutos Secos',
			'Frutas Deshidratadas',
			'Hierbas',
			'Aderezos',
			'Ensaladas Listas',
			'Abarrotes',
			'Cóctel',
			'Conservas',
			'Salsas y Condimentos',
			'Comidas Étnicas',
			'Desayuno',
			'Confitería',
			'Postres y Dulces',
			'Quesería',
			'Fiambrería',
			'Fiambrería Jumbo Artesanal',
			'Tablas de Cóctel',
			'Encurtidos',
			'Carnes de Vacuno',
			'Carne de Cerdo',
			'Pollo',
			'Pavo',
			'Pescados',
			'Mariscos',
			'Ahumados',
			'Apanados y Otros',
			'Camarones',
			'Cocktail Pescadería',
			'Hamburguesas',
			'Apanados',
			'Churrascos, Lomitos y Otros',
			'Verduras Congeladas',
			'Comidas Preparadas',
			'Helados y Postres',
			'Frutas Congeladas',
			'Hielo',
			'Pastas Frescas',
			'Pastelería',
			'Panadería Granel',
			'Masas y Tortillas',
			'Panadería Envasada',
			'Empanadas',
			'Pascualinas y Quiches',
			'Ensaladas Preparadas',
			'Postres y Dulces',
			'Pizzas Frescas',
			'Pastas de Cocktail',
			'Sandwich',
			'Bebidas Gaseosas',
			'Aguas Minerales',
			'Jugos',
			'Bebidas Energéticas',
			'Bebidas Isotónicas',
			'Cervezas',
			'Licores',
			'Vinos',
			'Higiene Personal',
			'Cuidado Bucal',
			'Cuidado Capilar',
			'Cuidado Mujer',
			'Cremas',
			'Cuidado Hombre',
			'Incontinencia',
			'Papeles Hogar',
			'Limpieza de Ropa',
			'Baño y Cocina',
			'Pisos y Muebles',
			'Aerosoles y Desinfectantes',
			'Accesorios de Limpieza',
			'Accesorios Médicos',
			'Preservativos y Lubricantes',
			'Suplementos y Vitaminas',
			'Primeros Auxilios',
			'Libre de Gluten',
			'Orgánico',
			'Sin Azúcar',
			'Sin Lactosa',
			'Vegano',
			'Perros',
			'Gatos',
			'Otras Mascotas',
			'Climatización',
			'Electrodomésticos',
			'Cuidado Personal',
			'Línea Blanca',
			'Televisores',
			'Telefonía',
			'Computación',
			'Audio y Video',
			'Juguetería',
			'Útiles Escolares',
			'Aire Libre',
			'Celebraciones',
			'Cuadernos',
			'Mochilas y Accesorios',
			'Menaje Cocina',
			'Menaje Mesa',
			'Organización',
			'Asado',
			'Hogar',
			'Automóvil',
			'Ferretería',
			'Pañales',
			'Toallas Húmedas',
			'Perfumería Infantil',
			'Accesorios de Bebé',
			'Colados, Picados y Otros',
			'Leche y Suplementos Infantiles',
			'Rodados de Bebé'
		]
	def url_por_categoria(categoria,extra_args=None):
		base_url="https://nuevo.jumbo.cl"
		url_extensions = [	
				['C:/1/3/','Leches Blancas'],
				['C:/1/5/','Leches Cultivadas'],
				['C:/1/6/','Leches Saborizadas'],
				['C:/1/7/','Leches Vegetales'],
				['C:/1/8/','Yoghurt'],
				['C:/1/12/','Postres'],
				['C:/1/13/','Mantequillas y Margarinas'],
				['C:/1/17/','Cremas'],
				['C:/1/18/','Manjar y Dulce de Leche'],
				['C:/1/19/','Huevos'],
				['C:/1/459/','Leche en Polvo'],
				['C:/20/21/','Verduras'],
				['C:/20/22/','Frutas'],
				['C:/20/23/','Frutas y Verduras Orgánicas'],
				['C:/20/24/','Frutos Secos'],
				['C:/20/25/','Frutas Deshidratadas'],
				['C:/20/26/','Hierbas'],
				['C:/20/418/','Aderezos'],
				['C:/20/425/','Ensaladas Listas'],
				['C:/27/28/','Abarrotes'],
				['C:/27/35/','Cóctel'],
				['C:/27/42/','Conservas'],
				['C:/27/54/','Salsas y Condimentos'],
				['C:/27/489/','Comidas Étnicas'],
				['C:/61/47/','Desayuno'],
				['C:/61/63/','Confitería'],
				['C:/61/62/','Postres y Dulces'],
				['C:/86/87/','Quesería'],
				['C:/86/88/','Fiambrería'],
				['C:/86/89/','Fiambrería Jumbo Artesanal'],
				['C:/86/90/','Tablas de Cóctel'],
				['C:/86/91/','Encurtidos'],
				['C:/75/76/','Carnes de Vacuno'],
				['C:/75/82/','Carne de Cerdo'],
				['C:/107/108/','Pollo'],
				['C:/107/109/','Pavo'],
				['C:/124/125/','Pescados'],
				['C:/124/126/','Mariscos'],
				['C:/124/144/','Ahumados'],
				['C:/124/142/','Apanados y Otros'],
				['C:/124/143/','Camarones'],
				['C:/124/131/','Cocktail Pescadería'],
				['C:/127/128/','Hamburguesas'],
				['C:/127/129/','Apanados'],
				['C:/127/130/','Churrascos, Lomitos y Otros'],
				['C:/127/132/','Verduras Congeladas'],
				['C:/127/133/','Comidas Preparadas'],
				['C:/127/134/','Helados y Postres'],
				['C:/127/135/','Frutas Congeladas'],
				['C:/127/136/','Hielo'],
				['C:/157/158/','Pastas Frescas'],
				['C:/157/159/','Pastelería'],
				['C:/157/161/','Panadería Granel'],
				['C:/157/162/','Masas y Tortillas'],
				['C:/157/573/','Panadería Envasada'],
				['C:/183/184/','Empanadas'],
				['C:/183/185/','Pascualinas y Quiches'],
				['C:/183/186/','Ensaladas Preparadas'],
				['C:/183/187/','Postres y Dulces'],
				['C:/183/440/','Pizzas Frescas'],
				['C:/183/473/','Pastas de Cocktail'],
				['C:/183/540/','Sandwich'],
				['C:/189/190/','Bebidas Gaseosas'],
				['C:/189/191/','Aguas Minerales'],
				['C:/189/192/','Jugos'],
				['C:/189/195/','Bebidas Energéticas'],
				['C:/189/196/','Bebidas Isotónicas'],
				['C:/204/205/','Cervezas'],
				['C:/204/206/','Licores'],
				['C:/204/207/','Vinos'],
				['C:/230/231/','Higiene Personal'],
				['C:/230/232/','Cuidado Bucal'],
				['C:/230/233/','Cuidado Capilar'],
				['C:/230/234/','Cuidado Mujer'],
				['C:/230/235/','Cremas'],
				['C:/230/236/','Cuidado Hombre'],
				['C:/230/224/','Incontinencia'],
				['C:/261/262/','Papeles Hogar'],
				['C:/261/263/','Limpieza de Ropa'],
				['C:/261/264/','Baño y Cocina'],
				['C:/261/265/','Pisos y Muebles'],
				['C:/261/266/','Aerosoles y Desinfectantes'],
				['C:/261/267/','Accesorios de Limpieza'],
				['C:/222/225/','Accesorios Médicos'],
				['C:/222/227/','Preservativos y Lubricantes'],
				['C:/222/228/','Suplementos y Vitaminas'],
				['C:/222/580/','Primeros Auxilios'],
				['C:/292/293/','Libre de Gluten'],
				['C:/292/294/','Orgánico'],
				['C:/292/295/','Sin Azúcar'],
				['C:/292/296/','Sin Lactosa'],
				['C:/292/460/','Vegano'],
				['C:/400/401/','Perros'],
				['C:/400/402/','Gatos'],
				['C:/400/403/','Otras Mascotas'],
				['C:/316/317/','Climatización'],
				['C:/316/318/','Electrodomésticos'],
				['C:/316/319/','Cuidado Personal'],
				['C:/316/320/','Línea Blanca'],
				['C:/298/299/','Televisores'],
				['C:/298/300/','Telefonía'],
				['C:/298/302/','Computación'],
				['C:/298/303/','Audio y Video'],
				['C:/335/336/','Juguetería'],
				['C:/335/337/','Útiles Escolares'],
				['C:/335/338/','Aire Libre'],
				['C:/335/178/','Celebraciones'],
				['C:/335/519/','Cuadernos'],
				['C:/335/521/','Mochilas y Accesorios'],
				['C:/354/355/','Menaje Cocina'],
				['C:/354/356/','Menaje Mesa'],
				['C:/354/357/','Organización'],
				['C:/354/358/','Asado'],
				['C:/354/359/','Hogar'],
				['C:/354/360/','Automóvil'],
				['C:/354/361/','Ferretería'],
				['C:/393/394/','Pañales'],
				['C:/393/395/','Toallas Húmedas'],
				['C:/393/396/','Perfumería Infantil'],
				['C:/393/397/','Accesorios de Bebé'],
				['C:/393/398/','Colados, Picados y Otros'],
				['C:/393/399/','Leche y Suplementos Infantiles'],
				['C:/393/461/','Rodados de Bebé']
			]

		product_urls=[]
				
		for extension,categoria_local in url_extensions:
			if categoria_local !=categoria:
				continue

			session = session_with_proxy(extra_args)
			pagina = 1
			while True:
				url_categoria = 'https://nuevo.jumbo.cl/buscapagina?fq={}' \
								'&PS=50&sl=3a356ef2-a2d4-4f1b-865f-c79b6fcf0f2a' \
								'&cc=24&sm=0&PageNumber={}'.format(extension, pagina)
				
				try:
					response = session.get(url_categoria,timeout=30)
				except Exception as x:
					try:
						response = session.get(url_categoria,timeout=30)
					except Exception as x:
						break
				
				if not response.text:
					break
				
				soup = BeautifulSoup(response.text, 'html.parser')
				name_box = soup.findAll('a', attrs={'class': 'product-item__image-link'})
				for name_box in name_box:
					product_url = name_box.get('href')
					product_urls.append(product_url)
				pagina += 1
				
				
		return product_urls


	def leer_urls(product_urls,supermercado,categoria,extra_args=None):
		session = session_with_proxy(extra_args)
		
		try:
			response = session.get(product_urls,timeout=20)
		except Exception as x:
			try:
				response = session.get(product_urls,timeout=30)
			except Exception as x:
				return 'no'
		

		if response.text !="":
			soup = BeautifulSoup(response.text, 'html.parser')
		else:
			return 'no'

		try:
			disponible = soup.find('div',{'class':'product-prices__wrapper'}).find('div', {'class': 'plugin-preco'})
		except:
			try:
				disponible = soup.find('div',{'class':'product-prices__wrapper'}).find('div', {'class': 'plugin-preco'})
			except:
				return 'no'

		try:
			codigo = soup.find('div',{'class':'skuReference'}).text.strip()
		except:
			try:
				codigo = soup.find('div',{'class':'skuReference'}).text.strip()
			except:
				return 'no'
		
		try:	
			nombre = soup.find('div', {'class': 'productName'}).text.strip()
		except:
			try:
				nombre = soup.find('div', {'class': 'productName'}).text.strip()
			except:
				return 'no'
		
		try:
			descripcion = soup.find('div', {'class': 'description'}).find('div', {'class': 'productDescriptionShort'}).text.strip()
		except:
			descripcion = "desc: "+nombre
		
		try:
			precio_actual = soup.find('strong', {'class': 'skuBestPrice'}).text.strip().replace("$","").split(",")
			precio_actual = int(precio_actual[0].strip().replace(".",""))	
		except:
			try:
				precio_actual = soup.find('strong', {'class': 'skuBestPrice'}).text.strip().replace("$","").split(",")
				precio_actual = int(precio_actual[0].strip().replace(".",""))
			except:
				return 'no'
			
		
		try:
			precio_normal = soup.find('strong', {'class': 'skuListPrice'}).text.strip().replace("$","").split(",")
			precio_normal = int(precio_normal[0].strip().replace(".",""))
		except:
			try:
				precio_normal = soup.find('strong', {'class': 'skuListPrice'}).text.strip().replace("$","").split(",")
				precio_normal = int(precio_normal[0].strip().replace(".",""))
			except:
				return 'no'

			

		if precio_normal==0:
			precio_normal = precio_actual
		
		product = Producto(
				codigo,
           		nombre,
           		supermercado,
           		categoria,
           		product_urls,
           		precio_normal,
           		precio_actual,
           		precio_actual,
           		precio_actual,
           		descripcion
       		 )
		return product







