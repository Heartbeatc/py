from conf import setting


def shop():
    print('shopping')
    print(setting.DB_PATH)



def run():
    while True:
        print(
            '''
            1 购物
            2 付款
            3 还款
            4 转账
            '''
        )
        choice=input('>>: ').strip()
        if not  choice:continue
        if choice == '1':
            shop()

run()