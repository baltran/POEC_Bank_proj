import json
import requests
from flask import request, jsonify

from webapp.api import bp
from webapp.api.errors import bad_request


def convert(value, source_currency, dest_currency):
    r = requests.get('https://api.exchangerate-api.com/v4/latest/{}'.format(
        source_currency))
    if r.status_code != 200:
        return 'Erreur: le service de conversion a échoué.'
    response = json.loads(r.content.decode('utf-8-sig'))
    print(response)
    value = value * float(response['rates'][dest_currency])
    return value


@bp.route('/convert', methods=['POST'])
def convert_currency():
    """Renvoie la conversion d'une devise
        test httpie:
        http POST http://localhost:5000/api/convert
    """
    data = request.get_json() or {}
    if 'value' not in data or ('value' in data and not data['value']):
        return bad_request('Veuillez ajouter une valeur')
    if 'source_currency' not in data or ('source_currency' in data and not data['source_currency']):
        return bad_request('Veuillez ajouter une devise source')
    if 'dest_currency' not in data or ('dest_currency' in data and not data['dest_currency']):
        return bad_request('Veuillez ajouter une devise de conversion')
    try:
        value = float(data['value'])
    except (ValueError, TypeError):
        return bad_request('Veuillez mettre un nombre')
    else:
        return jsonify({'value': convert(value,
                                         data['source_currency'],
                                         data['dest_currency'])})
