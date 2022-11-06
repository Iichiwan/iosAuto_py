# iosAuto
 fgo ios自动化python脚本

# 简介
这是一个基于wda的fgo自动化刷本脚本，在iphone12mini设备上试运行

前端操作视频：https://www.bilibili.com/video/BV1zV4y137vf/

真机运行视频：https://www.bilibili.com/video/BV1bg411r7r8/

前端地址：http://116.62.220.225/#/dash1

# 系统概述

![image](https://cdn.nlark.com/yuque/0/2022/png/12503614/1667119194323-925eb38e-a2c8-474f-b3cb-b983c5cf21e3.png)

## python
依赖facebook-wda实现自动化能力，通过http请求从服务端获取脚本json

JsonToAuto.py：实现json到执行脚本元素的转化

common.py：实现具体的脚本原子能力

checkui.py：依赖airtest实现ui校验，用于自动化流程中的节点确认

## javascript
使用[飞冰](https://ice.work/) （一个基于 React 的研发解决方案）搭建

与服务端联通，展示库中已存储脚本，同时提供新增、修改、删除能力

## java
使用SpringBoot搭建

提供数据库查询、修改接口，也可在这里实现脚本的定制、修改

## mysql

存储脚本json

脚本json格式
```
{
    "start":[
        "eatApple",
        "choose"
    ],
    "turn1":[
        {
            "action":"skill",
            "skill":7,
            "aim":1
        },
        {
            "action":"skill",
            "skill":8,
            "aim":0
        },
        {
            "action":"skill",
            "skill":9,
            "aim":1
        },
        {
            "action":"suitChange",
            "a":3,
            "b":4
        },
        {
            "action":"skill",
            "skill":1,
            "aim":0
        },
        {
            "action":"skill",
            "skill":2,
            "aim":0
        },
        {
            "action":"skill",
            "skill":3,
            "aim":3
        },
        {
            "action":"skill",
            "skill":4,
            "aim":0
        },
        {
            "action":"skill",
            "skill":6,
            "aim":0
        },
        {
            "action":"cardToNextTurn",
            "one":-1,
            "two":1,
            "three":2
        }
    ],
    "turn2":[
        {
            "action":"skill",
            "skill":5,
            "aim":0
        },
        {
            "action":"skill",
            "skill":7,
            "aim":0
        },
        {
            "action":"cardToNextTurn",
            "one":-2,
            "two":1,
            "three":2
        }
    ],
    "turn3":[
        {
            "action":"skill",
            "skill":8,
            "aim":1
        },
        {
            "action":"skill",
            "skill":9,
            "aim":1
        },
        {
            "action":"suitSkill",
            "skill":1,
            "aim":1
        },
        {
            "action":"card",
            "one":-1,
            "two":1,
            "three":2,
            "wait":10
        }
    ],
    "end":[

    ]
}
```


# 后续优化
