const mockData=[
  {
    "_id": "600d4075e218daaf4ec77e52",
    "menuType": "1",
    "menuName": "系统管理",
    "path": "/components",
    "icon": "el-icon-setting",
    "children": [
      {
        "_id": "600d525e602f452aaeeffcd9",
        "menuType": "1",
        "menuName": "用户管理",
        "path": "/user",
        "children": [
          {
            "_id": "6030ca8f93f0e159c8390f0c",
            "menuType": "1",
            "menuName": "新增",
            "path": "/system/add",
            "menuCode": "user-create"
          },
          {
            "_id": "603226d9257d15a8c54cf9f8",
            "menuType": "1",
            "menuName": "批量删除",
            "menuCode": "user-delete"
          },
          {
            "_id": "603253e0a821c6bb59084541",
            "menuType": "1",
            "menuName": "查看",
            "path": "/system/see",
            "menuCode": "user-query"
            
          }
        ]
      },
      {
        "_id": "601bc4f8a794e23c2e42efa9",
        "menuType": "1",
        "menuName": "菜单管理",
        "path": "/menu2",
        "children": [
          {
            "_id": "60325400a821c6bb59084543",
            "menuType": "1",
            "menuName": "查看",
            "path": "/components/chakan",
            "menuCode": "menu-query"
            
          },
          {
            "_id": "6032540fa821c6bb59084544",
            "menuType": "1",
            "menuName": "创建",
            "path": "/components/add",
            "menuCode": "menu-create"
          },
          {
            "_id": "6032540fa821c6bb59084545",
            "menuType": "1",
            "menuName": "啥玩意儿",
            "path": "/components/see",
            "menuCode": "menu-呵呵"
          }
        ]
      }
    ]
  },
  {
    "_id": "601b9eb25929c81a1f988bb0",
    "menuType": "1",
    "menuName": "审批管理",
    "path": "/audit",
    "icon": "el-icon-s-promotion",
    "children": [
      {
        "_id": "601bc763a794e23c2e42efaa",
        "menuType": "1",
        "menuName": "休假申请",
        "path": "/leave",
        "children": [
          {
            "_id": "603254a8a821c6bb59084549",
            "menuType": "1",
            "menuName": "查看",
            "path": "/components/chakan",
            "menuCode": "leave-query"
          },
          
          {
            "_id": "603254baa821c6bb5908454a",
            "menuType": "1",
            "menuName": "申请休假",
            "path": "/components/shenqinxiujia",
            "menuCode": "leave-create"
          }
        ]
      }
    ]
  }
]



export default mockData;
