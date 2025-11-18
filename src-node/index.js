// index.js
import fastify from 'fastify';
import cors from '@fastify/cors';
import mysql from 'mysql2/promise';

const app = fastify({logger:true});


// 注册 CORS 插件，并配置为允许所有来源

app.register(cors, {
  origin: ' *', // 允许所有来源，生产环境应该限制为具体的域名
  // origin: ' http://localhost:1420', // 允许所有来源，生产环境应该限制为具体的域名
  methods: ['GET', 'POST', 'PUT', 'DELETE'] // 允许的HTTP方法
});

// // 原生 Node.js 手动处理 CORS
// app.addHook('onRequest', (request, reply, done) => {
//   // 设置允许的源，这里可以根据请求动态判断
//   const origin = request.headers.origin;
//   const allowedOrigins = ['http://localhost:3000', 'http://127.0.0.1:3000', 'https://example.com'];
//   if (allowedOrigins.includes(origin)) {
//     reply.header('Access-Control-Allow-Origin', origin);
//   } else {
//     // 或者回复固定的允许源，使用 '*' 则不能携带凭证
//     reply.header('Access-Control-Allow-Origin', '*'); 
//   }

//   // 设置允许的 HTTP 方法
//   reply.header('Access-Control-Allow-Methods', 'GET, POST, PUT, DELETE, OPTIONS');
//   // 设置允许的头部
//   reply.header('Access-Control-Allow-Headers', 'Content-Type, Authorization, X-Requested-With');
//   // 设置是否允许发送凭证（如 cookies），如果 Allow-Origin 为 '*'，则此项必须为 false
//   // reply.header('Access-Control-Allow-Credentials', 'true'); 
//   // 设置预检请求（Preflight）的结果缓存时间
//   reply.header('Access-Control-Max-Age', '86400'); // 24小时

//   // 处理 OPTIONS 预检请求
//   if (request.method === 'OPTIONS') {
//     reply.send(); // 直接响应，不继续执行后续路由
//   } else {
//     done(); // 继续执行后续生命周期
//   }
// });



app.addHook('preHandler', async (request, reply) => {
  // 你的逻辑在这里，例如日志记录、验证等
  console.log(`收到请求: ${request.method} ${request.url}`);
  // 不需要调用 next()，Fastify 会自动继续
});




const pool = mysql.createPool({
  host: 'localhost',
  user: 'root',
  password: 'zst654321',
  database: 'mysql',
  connectionLimit: 10
});
app.decorate('mysql', pool);

// 现在使用 app 而不是 fastify 来定义路由
app.post('/', async (req, res) => {

  const [rows] = await app.mysql.execute(
    // 'SELECT * FROM user WHERE id = ?',
    'SELECT * FROM baidu_images',
    // [req.params.id]
  );
  // return JSON.stringify(rows);
  return rows;

  // return { message: 'Hello from Fast00ify!' };
  // res.send('根目录!')
});
// 现在使用 app 而不是 fastify 来定义路由
app.post('/add', async (req, res) => {
  // return { message: 'Hello from Fast00ify!' };
  res.send('post------------------------')
 
});

app.post('/see', async (req, res) => {
  const message = req.body; 
  console.log(`收到用户的消息:  ${JSON.stringify(message, null, 2)}`);

  // 处理登录逻辑，然后发送响应
  // 例如，假设登录成功
  res.send({ 
    status: 'success', 
    message: '登录成功',
    data: message 
  });
});




    // app.listen({ host: '0.0.0.0', port: 3000 });
    
    app.listen({ port: 3000 });
 