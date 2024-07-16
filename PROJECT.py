#import flask
from flask import Flask
app=Flask(__name__)
@app.route('/')
def project():
    return "<div style='background:skyblue'><h1>MY ONE PAGE STORY</h1><br><p><h2>The Golden Touch</h2><br><h3>The Greek king Midas did a good deed for a Satyr. This prompted Dionysus, the god of wine, to grant him a wish. Midas asked for everything he touched to turn to gold. Dionysus’ warned him not to do so, but Midas could not be swayed. Midas excitedly started touching everything and turning them into gold. Soon, he became hungry. But he couldn’t eat anything because even his food turned to gold. His beloved daughter saw him in distress and ran to hug him. However, she, too, turned to gold. He realised then the golden touch was not a blessing.</h3><hr>Moral:Greed leads one to downfall.</p></div>"
if __name__=='__main__':
    app.run(debug=True)
