



from flask import Flask, jsonify, request, abort
from songsDAO import songsDAO
#from drinksDAO import drinksDAO
from functools import wraps

app = Flask(__name__, static_url_path='', static_folder='.')

#@app.route('/')
#def index():
 #  return "Hello, World!"

#curl "http://127.0.0.1:5000/songs"

@app.route('/songs')
def getAll():
    #return "in getAll"
    #print("in getall")
    results = songsDAO.getAll()
    return jsonify(results)


#curl "http://127.0.0.1:5000/books/2"
@app.route('/songs/<int:id>')
def findById(id):
    foundsong = songsDAO.findByID(id)

    return jsonify(foundsong)

#curl  -i -H "Content-Type:application/json" -X POST -d "{\"Title\":\"hello\",\"Author\":\"someone\",\"Price\":123}" http://127.0.0.1:5000/books
@app.route('/songs', methods=['POST'])
def create():
    
    if not request.json:
        abort(400)
    # other checking 
    songs = {
        "singer": request.json['singer'],
        "song": request.json['song'],
        
    }
    values =(songs['singer'],songs['song'])
    newId = songsDAO.create(values)
    songs['id'] = newId
    return jsonify(songs)

#curl  -i -H "Content-Type:application/json" -X PUT -d "{\"Title\":\"hello\",\"Author\":\"someone\",\"Price\":123}" http://127.0.0.1:5000/books/1
@app.route('/songs/<int:id>', methods=['PUT'])
def update(id):
    foundsongs = songsDAO.findByID(id)
    if not foundsongs:
        abort(404)
    
    if not request.json:
        abort(400)
    reqJson = request.json
    
    if 'singer' in reqJson:
        foundsongs['singer'] = reqJson['singer']
    if 'song' in reqJson:
        foundsong['song'] = reqJson['song']
  
    values = (foundsongs['singer'],foundsongs['song'],foundsongs['id'])
    songsDAO.update(values)
    return jsonify(foundsongs)
        

    

@app.route('/songs/<int:id>' , methods=['DELETE'])
def delete(id):
    songsDAO.delete(id)
    return jsonify({"done":True})



if __name__ == '__main__' :
    app.run(debug= True)

