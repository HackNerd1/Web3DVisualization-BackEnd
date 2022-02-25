from ..base import base
from flask import request, jsonify
from flask_login import login_required
from app.models import Group
from flask import jsonify
from app import db
from app.utils.index import parseList
'''分页查询'''


@base.route('/assets/group', methods=['GET'])
@login_required
def get_group():
    res = Group.query.filter_by(ISDELETED=0)
    page = request.args.get('page') or 1
    size = request.args.get('size') or 20
    # request.args.get('page', 1) 获取url中的参数 默认为1
    groups = res.paginate(page=int(page), per_page=int(size), error_out=False)
    # print(request.args.get('page'))

    return jsonify({
        'code': 200,
        'msg': 'sucess',
        'data': {
            'groups': parseList(groups.items),
            'page': groups.page,
            'total': res.count()
        }
    })


'''新增分组'''


@base.route('/assets/group', methods=['POST'])
@login_required
def add_group():
    group = Group()

    group.NAME = request.form.get('name')
    group.ICON = request.form.get('icon')

    db.session.add(group)
    db.session.commit()
    return jsonify({'code': 200, 'msg': 'success'})


'''修改分组'''


@base.route('/assets/group/:<int:id>', methods=['PUT'])
@login_required
def edit_group(id):
    group = Group.query.get(id)
    group.NAME = request.form.get('name')
    group.ICON = request.form.get('icon')
    db.session.commit()
    return jsonify({'code': 200, 'msg': 'success'})


'''删除'''


@base.route('/assets/group/:<int:id>', methods=['DELETE'])
@login_required
def del_group(id):
    group = Group.query.get(id)

    group.ISDELETED = 1

    db.session.commit()
    return jsonify({'code': 200, 'msg': 'success'})


# '''
#   测试代码
# '''

# @base.route('/assets/403', methods=['GET'])
# def test_403():
#     return jsonify({'code': 403, 'msg': 'falid'})

# @base.route('/assets/500', methods=['GET'])
# def test_500():
#     return jsonify({'code': 500, 'msg': 'falid'})

# @base.route('/assets/401', methods=['GET'])
# def test_401():
#     return jsonify({'code': 401, 'msg': 'falid'})
