import webapp2
import plivo

class MainPage(webapp2.RequestHandler):
    def get(self):
        
        p = plivo.RestAPI("XXXXXXXXXX", "XXXXXXXXXXXXXXXXXXXX")

        params = {
            'src': '99999999999',
            'dst': '11111111111',
            'text': 'Hello world'
        }

        response = p.send_message(params)
        self.response.headers['Content-Type'] = 'text/plain'
        self.response.write('Message sent')

app = webapp2.WSGIApplication([
    ('/', MainPage),
], debug=True)