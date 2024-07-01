import os

from flask import (
    Flask, 
    jsonify,
    app,
    abort,
    Request,
    Response
)

from flask_cors import CORS

from models import setup_db, Plant

app = Flask(__name__)


def create_app(test_config):
    ##Creating a directory for SQLLite
    print ( " inside create_app " )
    print ( " inside test_config  " , test_config)
    app = Flask(__name__, instance_relative_config=True)

    setup_db(app)

    ##CORS Learning
    #   CORS(app) This does some basic setting on CORS
    cors = CORS(app, resources={r"/api/*": {"origins": "*"}})    
    cors_specific = CORS()

    # CORS Headers 
    @app.after_request
    def after_request(Response):
        Response.headers.add('Access-Control-Allow-Headers', 'Content-Type,Authorization,true')
        Response.headers.add('Access-Control-Allow-Methods', 'GET,PATCH,POST,DELETE,OPTIONS')
        return Response

    print("instance_path", app.instance_path)
    print("instance name", app.name)

    app.config.from_mapping(
        SECRET_KEY='dev', 
        DATABASE=os.path.join(app.instance_path, 'flaskr.sqlite')
    )
    
    # if test_config is None:
    # # load the instance config, if it exists, when not testing
    # # app.config.from_pyfile('config.py', silent=True)
    #     print("test_config ",test_config)
    # else:
    #  # load the test config if passed in
    #     print("inside else")
    #     app.config.from_mapping(test_config)
    
    try:
        print ( " inside makedirs " )
        os.makedirs(app.instance_path)
    except OSError:
        pass
    return app

@app.route('/')
def hello_world():
    return 'Hello, World! , Hello , God'
    #return jsonify({'message':'Hello, World!'})
    

@app.route('/smiley')
#@cors_specific(methods=['GET'])
def smiley():
    return ':)'
    
@app.route('/books',methods=['GET','POST','DELETE'])
def books():
    return 'books'
    

@app.route('/plants', methods=['GET','POST'])
#@cross_origin
def get_plants():
        # Implement pagination
    page = Request.args.get('page', 1, type=int)
    start = (page - 1) * 10
    end = start + 10

    plants = Plant.query.all()
    formatted_plants = [plant.format() for plant in plants]
    return jsonify({
        'success': True,
        'plants':formatted_plants[start:end],
        'total_plants':len(formatted_plants)
        })
    
@app.route('/plants/<int:plant_id>')
def get_specific_plant(plant_id):
        plant = Plant.query.filter(Plant.id==plant_id).one_or_none()
        if plant is None:
            abort(404)
        else:   
            return jsonify({
                'success': True,
                'plant': plant.format()
            })

@app.route('/entrees/<int:entree_id>')
def retrieve_entree(entree_id):
    print ('Entree %d' % entree_id)
    return 'Entree' + entree_id
    
##Pagination
@app.route('/entrees', methods=['GET']) 
def get_entrees(): 
    page = Request.args.get('page', 1, type=int)
    print ("argument one from get request" + page)

@app.errorhandler(404)
def not_found(error):
    return jsonify({
        "success": False, 
        "error": 404,
        "message": "Not found"
        }), 404

if __name__ == '__main__':
    print ( " inside main " )
    create_app(None)
    app.run(debug=True)