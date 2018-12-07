import psycopg2
class Producto:
    def __init__(self,codigo, nombre, tienda, categoria, url, precio_normal, precio_oferta,precio_tarjeta,precio_x_mayor, descripcion):
        self.codigo = codigo
        self.nombre = nombre
        self.tienda = tienda
        self.categoria = categoria
        self.url = url
        self.precio_normal = precio_normal
        self.precio_oferta = precio_oferta
        self.precio_tarjeta = precio_tarjeta
        self.precio_x_mayor = precio_x_mayor
        self.descripcion = descripcion

    """def __str__(self):
        lines = list()
        lines.append('{} - {} ({})'.format(self.tienda, self.nombre,
                                           self.categoria))
        lines.append(self.url)  
        lines.append(u'Code: {}'.format(self.codigo))    
        lines.append(u'Normal price: {}'.format(self.precio_normal))
        lines.append(u'Offer price: {}'.format(self.precio_oferta))
        lines.append('Description: {}'.format(self.descripcion))

        return '\n'.join(lines)

    def __repr__(self):
        return '{} - {} - {} - {} - {} - {} - {} '.format(self.tienda,self.codigo, self.nombre, self.descripcion, self.categoria, self.precio_normal, self.precio_oferta)

    def serialize(self):
        return {
            'code':self.codigo,
            'name': self.nombre,
            'store': self.tienda,
            'category': self.categoria,
            'url': self.url,
            'normal_price': str(self.precio_normal),
            'offer_price': str(self.precio_oferta),
            'description': self.descripcion,
        }"""

    def guardarProductos(self):
        string_conexion = "dbname='precios_supermercados' user='postgres' host='localhost' password='226264nicolas'"
        db = psycopg2.connect(string_conexion)
        cursor = db.cursor()
        sql= """INSERT INTO lista_productos(codigo_supermercado,codigo_producto, categoria_producto, nombre_producto,descripcion_producto) SELECT * FROM (SELECT %s,%s, %s, %s,%s) AS tmp WHERE NOT EXISTS (SELECT codigo_producto FROM lista_productos WHERE codigo_producto = %s and codigo_supermercado= %s) LIMIT 1;"""
        try:
          cursor.execute(sql,(self.tienda,self.codigo,self.categoria,self.nombre,self.descripcion,self.codigo,self.tienda))
          db.commit()
          #print("Tienda: ",self.tienda," Producto: ",self.codigo," - ",self.nombre," - ",self.precio_normal," - ",self.precio_oferta," - GUARDADO")
        except: 
          db.rollback()

        db.close()
    def guardarPrecios(self):
        string_conexion = "dbname='precios_supermercados' user='postgres' host='localhost' password='226264nicolas'"
        db = psycopg2.connect(string_conexion)
        cursor = db.cursor()
        sql= """INSERT INTO precios_productos(codigo_producto,codigo_supermercado, precio_normal, precio_oferta) VALUES (%s,%s,%s,%s);"""
        try:
          cursor.execute(sql,(self.codigo,self.tienda,self.precio_normal,self.precio_oferta))
          db.commit()
          #print("Tienda: ",self.tienda," Producto: ",self.codigo," - ",self.nombre," - ",self.precio_normal," - ",self.precio_oferta," - GUARDADO")
        except: 
          db.rollback()

        db.close()
