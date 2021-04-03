from flask import Flask

app = Flask("__name__")
userList=['Pradeep','SecondUser', 'User3']
@app.route('/')

def index():
    return "home page"

@app.route('/profile/<profileName>')
def username(profileName):
    if profileName in userList:
        return "<h3>Hello! %s<h3>" % profileName
    else:
        return "there are no users are added to this website named %s" % profileName

@app.route('/id/<int:userID>')
def id(userID):
    return "<h2>userID is %s<h2>" % userID

#changes will be made soon

if __name__ == '__main__':
    app.run(debug=True)