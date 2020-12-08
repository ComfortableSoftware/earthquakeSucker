import web
from web import form


from dataStuff import timeDateStuff as TDS

render = web.template.render('templates')  # your templates
vpass = form.regexp(r".{3,20}$", 'must be between 3 and 20 characters')
vemail = form.regexp(r".*@.*", "must be a valid email address")
register_form = form.Form(
	form.Textbox("username", description="Username"),
	form.Textbox("email", vemail, description="E-Mail"),
	form.Password("password", vpass, description="Password"),
	form.Password("password2", description="Repeat password"),
	form.Button("submit", type="submit", description="Register"),
	validators=
	[
		form.Validator("Passwords did't match", lambda i: i.password == i.password2)
	]
)


HTMLurls = (
	"/register", "register",
	"/done", "done",
	"/.*", "defaultUrl",
)


def sendMyHeader(myTitle):
	# web.ctx.env
	# web.header("Expires", ": Fri, 14 Oct 1989 19:30:00 GMT")
	web.header("Expires:", TDS.gmdate)
	web.header("Last-Modified:", TDS.gmdate)
	web.header("cache-control", "no-store, no-cache, must-revalidate")
	web.header("Pragma", "no-cache")
	with open('styles.css', 'r') as content_file:
		content = content_file.read()
	strToReturn = """
<!DOCTYPE html>
<html lang="en">
	<head>
		<title>""" + myTitle + """ </title>
"""
	strToReturn += content + """
	</head>
	<body>
		"""
	return strToReturn


class done:
	def GET(self):
		outStr = """
<html>
	<body>
		<span>you done good</span>
	</body>
</html>
"""
		return outStr


class defaultUrl:
	def GET(self):
		outStr = sendMyHeader("empty link") + """
		<h1>
			try host:8080/quakes 
			host:8080/form 		
		</h1>
		<table>
		<tr>
		<td class="close0r0">close 0 r0</td>
		</tr>
		</table>
	</body>
</html>
		"""
		print(outStr)
		return outStr


class register:
	def GET(self):
		# do $:f.render() in the template
		# theText = sendMyHeader("pageTitle")
		f = register_form()
		return render.register(f, sendMyHeader("my new title"))

	def POST(self):
		f = register_form()
		if not f.validates():
			return render.register(f)
		userData = web.input()
		print(f"f {str(f)}  userData {userData}  username {userData['username']}")
		raise web.seeother("/done")


HTMLapp = web.application(HTMLurls, globals())
if __name__ == "__main__":
	HTMLapp.run()
	print("we made it")
