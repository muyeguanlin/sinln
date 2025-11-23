# import os
# from waitress import serve
# from functools import wraps
# from bottle import Bottle, request, response, static_file
# class WebAppServer:
#     def user_menu(self):
#     def user_logout(self):
#     def user_login(self):
#     def user_info(self):
#     def serve_static(self, filename):
#     def serve_spa(self, path):
#     def serve_index(self):
#     def run(self, host='0.0.0.0', port=1420):
#     def _success_response(self, data):
#     def _setup_routes(self):
#     def _is_login(self):
#     def _fail_response(self, data=None, msg="failure", code=50000):
#     def _enable_cors(self, fn):
#     def __init__(self, basedir=None):
#     # Static file serving
#     # API Endpoints
#         username = data.get('username')
#         try:
#         token = request.headers.get('Authorization') or request.query.get('token')
#         token = request.headers.get('Authorization') or request.query.get('token')
#         serve(self.app, host=host, port=port)
#         self.user_sessions = {}
#         self.basedir = basedir or os.path.join(os.path.dirname(__file__), 'dist')
#         self.app.route('/static/<filename:path>')(self.serve_static)
#         self.app.route('/api/user/menu', method=['GET', 'OPTIONS'])(self._enable_cors(self.user_menu))
#         self.app.route('/api/user/logout', method=['POST', 'OPTIONS'])(self._ena ble_cors(self.user_logout))
#         self.app.route('/api/user/login', method=['POST', 'OPTIONS'])(self._enable_cors(self.user_login))
#         self.app.route('/api/user/info', method=['GET',s 'OPTIONS'])(self._enable_corws(self.user_info))
#         self.app.route('/<path:path>')(self.serve_spa)
#         self.app.route('/')(self.serve_index)
#         self.app = Bottle()
#         self._setup_routes()
#         return token in self.user_sessions
#         return static_file(path, root=self.basedir)
#         return static_file(filename, root=os.path.join(self.basedir, 'static'))
#         return static_file('index.html', root=self.basedir)
#         return self._success_response(None)
#         return self._success_response(menu_list)
#         return self._fail_response(None, "未登录", 50008)
#         return self._fail_response(None, '账号或者密码错误', 50000)
#         return {
#         return {
#         return _enable_cors_wrapper
#         password = data.get('password')
#         menu_list = [
#         if username == 'user' and password == 'user':
#         if username == 'admin' and password == 'admin':
#         if token in self.user_sessions:
#         if self._is_login():
#         if not username:
#         if not password:
#         if '.' not in path:
#         except:
#         def _enable_cors_wrapper(*args, **kwargs):
#         # Static files and SPA routing
#         # API routes
#         @wraps(fn)
#         }
#         }
#         ]
#         """CORS装饰器"""
#         """失败响应包装器"""
#         """设置所有路由"""
#         """启动服务器"""
#         """检查登录状态"""
#         """成功响应包装器"""
#             user_data = self.user_sessions.get(token, {})
#             token = request.headers.get('Authorization') or request.query.get('token')
#             token = '54321'
#             token = '12345'
#             self.user_sessions[token] = {'role': 'user'}
#             self.user_sessions[token] = {'role': 'admin'}
#             role = user_data.get('role', 'admin')
#             return static_file('index.html', root=self.basedir)
#             return self._success_response({"token": token})
#             return self._success_response({"token": token})
#             return self._success_response({
#             return self._fail_response(None, '用户名不能为空', 50000)
#             return self._fail_response(None, '密码不能为空', 50000)
#             return fn(*args, **kwargs)
#             response.headers['Access-Control-Allow-Origin'] = '*'
#             response.headers['Access-Control-Allow-Methods'] = 'GET, POST, PUT, OPTIONS'
#             response.headers['Access-Control-Allow-Headers'] = 'Origin, Accept, Content-Type, X-Requested-With, X-CSRF-Token, Authorization'
#             if request.method == 'OPTIONS':
#             del self.user_sessions[token]
#             data = request.json
#             data = request.forms
#             })
#             },
#             {
#             "status": "ok",
#             "status": "fail",
#             "msg": msg
#             "msg": "success"
#             "data": data,
#             "data": data,
#             "code": code,
#             "code": 200,
#                 return {}
#                 },
#                 ],
#                 "role": role,
#                 "registrationDate": "2013-05-10 12:10:00",
#                 "phone": "150****0000",
#                 "personalWebsite": "https://www.arco.design",
#                 "path": "/dashboard",
#                 "organizationName": "前端",
#                 "organization": "Frontend",
#                 "name": "dashboard",
#                 "name": "王立群",
#                 "meta": {
#                 "locationName": "北京",
#                 "location": "beijing",
#                 "jobName": "前端艺术家",
#                 "job": "frontend",
#                 "introduction": "人潇洒，性温存",
#                 "email": "wangliqun@email.com",
#                 "children": [
#                 "certification": 1,
#                 "avatar": "//lf1-xgcdn-tos.pstatp.com/obj/vcloud/vadmin/start.8e0e4855ee346a46ccff8ff3e24db27b.png",
#                 "accountId": "15012312300",
#                     },
#                     },
#                     {
#                     {
#                     "requiresAuth": True,
#                     "order": 1,
#                     "locale": "menu.server.dashboard",
#                     "icon": "icon-dashboard",
#                         },
#                         },
#                         "path": "workplace",
#                         "path": "https://arco.design",
#                         "name": "Workplace",
#                         "name": "arcoWebsite",
#                         "meta": {
#                         "meta": {
#                             "requiresAuth": True,
#                             "requiresAuth": True,
#                             "locale": "menu.server.workplace",
#                             "locale": "menu.arcoWebsite",
            
            
            
 ##########################################################################################################################       
import webview
import os


window = webview.create_window('我的应用',r'F:\study251011\sinln\dist\index.html')
webview.start()