import flask
import pickle

from sklearn.linear_model import LogisticRegression
from sklearn.pipeline import make_pipeline
from sklearn.feature_extraction.text import TfidfVectorizer

app = flask.Flask(__name__)

subject_model = pickle.load(open('subject_model.p', 'rb'))

top_subjects = ['armed conflicts', 'art and culture', 'business', 'disasters', 'international relations',
 'law', 'politics', 'science', 'sports']

# year_model = pickle.load('year_model.p')

@app.route("/", methods=["GET","POST"])
def predict():
    data = {'success': False}

    params = flask.request.json

    if params is None:
        params = flask.request.args

    
    if 'headline' in params.keys():
        
        try:
            
            data['subject'] = str(subject_model.predict([params.get('headline')])[0])
            data['all_proba'] = dict(zip(top_subjects, list(subject_model.predict_proba([params.get('headline')])[0])))
            data['proba'] = data['all_proba'][data['subject']]            
            data['success'] = True

        except:
            data = {'response': None, 'success': False}
    else:
        data = {'response': None, 'success': False}
            
    return flask.jsonify(data)
