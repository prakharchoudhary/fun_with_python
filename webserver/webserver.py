from BaseHTTPServer import BaseHTTPRequestHandler, HTTPServer
import cgi

#import CRUD operations
from database_setup import Base, Restaurant, MenuItem
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

#create session and connect to DB
engine = create_engine('sqlite:///restaurantmenu.db')
Base.metadata.bind = engine
DBsession = sessionmaker(bind=engine)
session = DBsession()

class WebServerHandler(BaseHTTPRequestHandler):

	def do_GET(self):
		try:
			if self.path.endswith('/restaurants'):
				restaurants = session.query(Restaurant).all()
				self.send_response(200)
				self.send_header('Content-type', 'text/html')
				self.end_headers()
				output = ""
				output += "<htmt><body><center>"
				output += "<a href='/restaurants/new'><h1>Make a new restaurant</h1></a>"
				for restaurant in restaurants:
					output += restaurant.name
					output += "</br>"
					output += "<a href='/restaurant/%s/edit'>Edit</a>"% restaurant.id
					output += "</br>"
					output += "<a href='/restaurant/%s/delete'>Delete</a>"% restaurant.id
					output += "</br></br></br>"
				output += "</center></body></html>"	
				self.wfile.write(output)
				return

			if self.path.endswith('/restaurants/new'):
				self.send_response(200)
				self.send_header('Content-type', 'text/html')
				self.end_headers()
				output = ""
				output += "<html><body>"
				output += "<h1>Make a new restaurant</h1>"
				output += "<form method='POST' enctype='multipart/form-data' action='/restaurants/new'>"
				output += "<input name='newRestaurantName' type='text' placeholder='New Restaurant Name'>"
				output += "<input type='submit' value='create'"
				output += "</body</html>"
				self.wfile.write(output)
				return

			if self.path.endswith('/edit'):
				restaurantIDPath = self.path.split('/')[2]
				myRestaurantQuery = session.query(Restaurant).filter_by(id=restaurantIDPath).one()
				if myRestaurantQuery:
					self.send_response(200)
					self.send_header('Content-type', 'text/html')
					self.end_headers()
					output = ""
					output += "<html><body>"
					output += "<h1>Change restaurant name</h1>"
					output += "<form method='POST' enctype='multipart/form-data' action='/restaurants/%s/edit'>"% restaurantIDPath 
					output += "<input name='newRestaurantName' type='text' placeholder='Edit Restaurant Name'>"
					output += "<input type='submit' value='create'>"
					output += "</body</html>"
					self.wfile.write(output)

			if self.path.endswith('/delete'):
				restaurantIDPath = self.path.split('/')[2]
				myRestaurantQuery = session.query(Restaurant).filter_by(id=restaurantIDPath).one()
				if myRestaurantQuery:
					self.send_response(200)
					self.send_header('Content-type', 'text/html')
					self.end_headers()
					output = ""
					output += "<html><body>"
					output += "<h1>Are you sure you want to delete %s?</h1>"% myRestaurantQuery
					output += "<form method='POST' enctype='multipart/form-data' action='/restaurants/%s/delete'>"% restaurantIDPath 
					output += "<input type='submit' value='delete'>"
					output += "</body</html>"
					self.wfile.write(output)

			if self.path.endswith('/hello'):
				self.send_response(200)
				self.send_header('Content-type', 'text/html')
				self.end_headers()
				output = ""
				output += "<html><body>"
				output += "<h1>Hello!</h1>"
				output += "</body></html>"
				self.wfile.write(output)
				return
		except IOError:
			self.send_error(404, "File not found at port %s" % self.path)

	def do_POST(self):
		if self.path.endswith('/restaurants/new'):
			ctype, pdict = cgi.parse_header(self.headers.getheader('content-type'))
			if ctype == 'multipart/form-data':
				fields=cgi.parse_multipart(self.rfile, pdict)
			messagecontent = fields.get('newRestaurantName')

			newRestaurant = Restaurant(name = messagecontent[0])
			session.add(newRestaurant)
			session.commit()

			self.send_response(301)
			self.send_header('Content-type', 'text/html')
			self.send_header('Location', '/restaurants')	#to redirect back to page /restaurants
			self.end_headers()

		if self.path.endswith('/edit'):
			ctype, pdict = cgi.parse_header(self.headers.getheader('content-type'))
			if ctype == 'multipart/form-data':
				fields=cgi.parse_multipart(self.rfile, pdict)
			messagecontent = fields.get('newRestaurantName')
			restaurantIDPath = self.path.split('/')[2]
			myRestaurantQuery = session.query(Restaurant).filter_by(id=restaurantIDPath).one()
			if myRestaurantQuery != []:
				myRestaurantQuery.name = messagecontent[0]
				session.add(myRestaurantQuery)
				session.commit()

				self.send_response(301)
				self.send_header('Content-type', 'text/html')
				self.send_header('Location', '/restaurants')	#to redirect back to page /restaurants
				self.end_headers()

		if self.path.endswith('/delete'):
			ctype, pdict = cgi.parse_header(self.headers.getheader('content-type'))
			if ctype == 'multipart/form-data':
				fields=cgi.parse_multipart(self.rfile, pdict)
			restaurantIDPath = self.path.split('/')[2]
			myRestaurantQuery = session.query(Restaurant).filter_by(id=restaurantIDPath).one()
			if myRestaurantQuery != []:
				session.delete(myRestaurantQuery)
				session.commit()

				self.send_response(301)
				self.send_header('Content-type', 'text/html')
				self.send_header('Location', '/restaurants')	#to redirect back to page /restaurants
				self.end_headers()


def main():
	try:
		server = HTTPServer(('', 8080), WebServerHandler)
		print 'Web server running....open localhost:8080/hello or /restaurants in browser'
		server.serve_forever()
	except:
		print "^C received, shutting down server"
		server.socket.close()

if __name__ == '__main__':
	main()