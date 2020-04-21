from flask import Flask, request
from cassandra.cluster import Cluster

clustler = Cluster(contact_points=['172.17.0.2'],port=9042)
session = cluster.connect()
app = Flask(__name__)

@app.route('/')
def hello():
    name = request.args.get("artist","ABBA")
    return('<h1>Hello, {}!</h1>'.format(artist))

@app.route('/songdata/<artist>')
def profile(artist):
    rows = session.execute( """Select * From songdata.stats
                            where artist = '{}'""".format(artist))
    for artist in rows:
        return('<h1>{} has {} song</h1>'.format(artist,song))

    return('<h1>This is the link to the lyrics</h1>')

@app.route('/artist/song/<link>/', methods=['GET'])
 def get_link(song):
         response={link:'Not Found!'}
         for item in artist:
                  if item["artist"]==song:
                          response = ["link"]  break
          return jsonify(response)

@app.route('/link', methods=['POST'])
def create_a_link():
   new_link = {
       'artist': request.json['artist'],
       'song': request.json.get('song')
 }
 all_link.append(new_record)
  return jsonify({'message': 'created: /link/{}'.format(new_link)}), 201

@app.route('/artist/<song>', methods=['DELETE'])
def delete_a_song(song):
matching_link = [song for song in all_links if song[artist]== ABBA]
 all_link.remove(matching_link[0])
 return jsonify({'success': True})

if __name__ == '__main__': app.run(host='0.0.0.80')
