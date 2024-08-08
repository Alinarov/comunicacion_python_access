import pyodbc

class DatabaseConnector(object):
	def __init__(self):
		"""
		Inicializa la clase con la ruta al archivo de base de datos Access.
		:param db_file: Ruta al archivo .accdb de Access.
		"""
		self.db_file = r'databases/grafito_ventas.accdb'

		self.connection = None
		self.cursor = None


	def connect(self):
		"""
		Establece la conexión con la base de datos Access.
		"""
		connection_string = f'DRIVER={{Microsoft Access Driver (*.mdb, *.accdb)}};DBQ={self.db_file};'
		try:
			self.connection = pyodbc.connect(connection_string)
			self.cursor = self.connection.cursor()
			print("Conexión establecida con éxito.")
		except pyodbc.Error as e:
			print(f"Error al conectar a la base de datos: {e}")

	def execute_query(self, query):
		"""
		Ejecuta una consulta SQL y devuelve los resultados.
		:param query: Consulta SQL para ejecutar.
		:return: Resultados de la consulta.
		"""
		if self.cursor is None:
			print("No hay conexión establecida. Por favor, conéctese primero.")
			return None
		
		try:
			self.cursor.execute(query)
			results = self.cursor.fetchall()
			return results
		except pyodbc.Error as e:
			print(f"Error al ejecutar la consulta: {e}")
			return None

	def close(self):
		"""
		Cierra la conexión con la base de datos.
		"""
		if self.connection:
			self.connection.close()
			self.cursor = None
			self.connection = None
			print("Conexión cerrada.")


def verificador(usuario):
	con = DatabaseConnector()
	con.connect()

	query = f"SELECT COUNT(*) FROM usuarios WHERE usuario = '{usuario}';"



if __name__ == '__main__':
	# Crear una instancia de la clase Comunicacion con la ruta al archivo Access
	
	comunicacion = DatabaseConnector()
	
	# Conectar a la base de datos
	comunicacion.connect()
	
	# Ejecutar una consultas
	query = """INSERT INTO precios (valor) VALUES  (0.10),(0.20),(0.25),(0.30),(0.50),(0.60),(0.75),(1.00),(1.20),(1.50),(1.75),(2.00),(2.50),(2.75),(3.00),(3.20),(3.50),(3.75),(4.00),(4.50),(4.80),(5.00),(5.20),(5.50),(5.75),(6.00),(6.50),(6.80),(7.00),(7.50),(8.00),(8.20),(8.50),(8.70),(9.00),(10.50),(11.50),(14.50),(16.00),(18.00),(32.00),(35.00),(64.00)"""
	results = comunicacion.execute_query(query)
	
	if results:
		# Imprimir los resultados
		for row in results:
			print(row)
	
	# Cerrar la conexión
	comunicacion.close()
