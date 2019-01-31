menu = {
    '北京': {
        '海淀': {
            '五道口': {
                'soho': {},
                '网易': {},
                'google': {}
            },
            '中关村': {
                '爱奇艺': {},
                '汽车之家': {},
                'youku': {},
            },
            '上地': {
                '百度': {},
            },
        },
        '昌平': {
            '沙河': {
                '老男孩': {},
                '北航': {},
            },
            '天通苑': {},
            '回龙观': {},
        },
        '朝阳': {},
        '东城': {},
    },
    '上海': {
        '闵行': {
            "人民广场": {
                '炸鸡店': {}
            }
        },
        '闸北': {
            '火车站': {
                '携程': {}
            }
        },
        '浦东': {},
    },
    '山东': {},
}

current_layer = menu
history = []
while True:
    for i in current_layer:
        print(i)
    choice = input('>:').strip()
    if not choice:
        continue
    if choice == 'q':
        exit('程序已退出')
    elif choice in current_layer:
        if len(current_layer[choice]) > 0:
            history.append(current_layer)
            current_layer = current_layer[choice]
        else:
            print('当前已是最底层！')
    elif choice == 'b':
        if len(history) > 0:
            current_layer = history[-1]
            history.pop()
        else:
            print('当前已是最顶层！')
    else:
        print('输入有误，请重新输入')
