from django import template

register = template.Library()


@register.simple_tag
def access_list(some_list: list, index: int):
    """
    リストの要素のうち、インデックスで指定した要素を返す
    :param some_list: 要素を取得したいリスト
    :param index: 取得したいリストのインデックス
    :return: 指定したインデックスに格納されているリストの要素
    """
    try:
        result = some_list[int(index)]
        return result
    except:
        return ""

@register.simple_tag
def calcurate_case1(credits_list:list, user_credit):
    try:
        result = 0
        getCredit = 0
        allCredit = 0
        clist = list(credits_list.values())
        for i in clist:
            if(i['CreditCondition'] == 1):
                if(user_credit[i['Number']-1] == 1):
                    getCredit += i['CreditScore']
                allCredit += i['CreditScore']
        result = 4 - getCredit
        #print("区分1で足りない単位="+result)
        if(result <= 0):
            result = 0
        return result
    except:
        return ""

@register.simple_tag
def calcurate_case2(credits_list:list, user_credit):
    try:
        result = 0
        getCredit = 0
        allCredit = 0
        clist = list(credits_list.values())
        for i in clist:
            if(i['CreditCondition'] == 2):
                if(user_credit[i['Number']-1] == 1):
                    getCredit += i['CreditScore']
                allCredit += i['CreditScore']
        result = allCredit - getCredit
        #print("区分2で足りない単位="+result)
        if(result <= 0):
            result = 0        
        return result
    except:
        return ""

@register.simple_tag
def calcurate_case3(credits_list:list, user_credit):
    try:
        result = 0
        getCredit = 0
        allCredit = 0
        clist = list(credits_list.values())
        for i in clist:
            if(i['CreditCondition'] == 3):
                if(user_credit[i['Number']-1] == 1):
                    getCredit += i['CreditScore']
                allCredit += i['CreditScore']
        result = 2 - getCredit
        #print("区分3で足りない単位="+result)
        if(result <= 0):
            result = 0    
        return result
    except:
        return ""

@register.simple_tag
def calcurate_case4(credits_list:list, user_credit):
    try:
        result = 0
        getCredit = 0
        allCredit = 0
        clist = list(credits_list.values())
        for i in clist:
            if(i['CreditCondition'] == 4):
                if(user_credit[i['Number']-1] == 1):
                    getCredit += i['CreditScore']
                allCredit += i['CreditScore']
        result = 2 - getCredit
        #print("区分4で足りない単位="+result)
        if(result <= 0):
            result = 0    
        return result
    except:
        return ""

@register.simple_tag
def calcurate_case5(credits_list:list, user_credit):
    try:
        result = 0
        getCredit = 0
        allCredit = 0
        clist = list(credits_list.values())
        for i in clist:
            if(i['CreditCondition'] == 5):
                if(user_credit[i['Number']-1] == 1):
                    getCredit += i['CreditScore']
                allCredit += i['CreditScore']
        result = 8 - getCredit
        #print("区分5で足りない単位="+result)
        if(result <= 0):
            result = 0
        return result
    except:
        return ""

@register.simple_tag
def calcurate_case6(credits_list:list, user_credit):
    try:
        result = 0
        getCredit = 0
        allCredit = 0
        clist = list(credits_list.values())
        for i in clist:
            if(i['CreditCondition'] == 6):
                if(user_credit[i['Number']-1] == 1):
                    getCredit += i['CreditScore']
                allCredit += i['CreditScore']
        result = 0 - getCredit
        #print("区分6で足りない単位="+result)
        if(result <= 0):
            result = 0    
        return result
    except:
        return ""

@register.simple_tag
def calcurate_case7(credits_list:list, user_credit):
    try:
        result = 0
        getCredit = 0
        allCredit = 0
        clist = list(credits_list.values())
        for i in clist:
            if(i['CreditCondition'] == 7):
                if(user_credit[i['Number']-1] == 1):
                    getCredit += i['CreditScore']
                allCredit += i['CreditScore']
        result = 14 - getCredit
        #print("区分7で足りない単位="+result)
        if(result <= 0):
            result = 0    
        return result
    except:
        return ""

@register.simple_tag
def calcurate_case8(credits_list:list, user_credit):
    try:
        result = 0
        getCredit = 0
        allCredit = 0
        clist = list(credits_list.values())
        for i in clist:
            if(i['CreditCondition'] == 8):
                if(user_credit[i['Number']-1] == 1):
                    getCredit += i['CreditScore']
                allCredit += i['CreditScore']
        result = 44 - getCredit
        #print("区分8で足りない単位="+result)
        if(result <= 0):
            result = 0    
        return result
    except:
        return ""

@register.simple_tag
def calcurate_case9(credits_list:list, user_credit):
    try:
        result = 0
        getCredit = 0
        allCredit = 0
        clist = list(credits_list.values())
        for i in clist:
            if(i['CreditCondition'] == 9):
                if(user_credit[i['Number']-1] == 1):
                    getCredit += i['CreditScore']
                allCredit += i['CreditScore']
        result = 0 - getCredit
        #print("区分9で足りない単位="+result)
        if(result <= 0):
            result = 0    
        return result
    except:
        return ""

# 区分1～5までの合計
# @register.simple_tag
# def calcurate_case15(credits_list:list, user_credit):
#     try:
#         result = 0
#         getCredit = 0
#         allCredit = 0
#         clist = list(credits_list.values())
#         for i in clist:
#             if(i['CreditCondition'] <= 5):
#                 if(user_credit[i['Number']-1] == 1):
#                     getCredit += i['CreditScore']
#                 allCredit += i['CreditScore']
#         result = 10 - getCredit
#         #print("区分9で足りない単位="+result)
#         return result
#     except:
#         return ""