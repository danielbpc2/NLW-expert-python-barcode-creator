from flask import Blueprint, request, jsonify

tags_routes_bp = Blueprint('tags_routes', __name__)

@tags_routes_bp.route('/create_tag', methods=['POST'])
def create_tag():
    # product_code = body.get('product_code')
    print(request.json)
    # tag = Code128(product_code, writer=ImageWriter())
    # path_from_tag = f'{tag}'
    # tag.save(path_from_tag)

    return jsonify({"status": "ok"}),200
