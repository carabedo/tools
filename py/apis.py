def get_tree(dicc,padding=0,parent=''):
    keys_not_list_not_dict=[ (x[0],type(x[1]).__name__) for x in dicc.items() if (type(x[1]).__name__ != 'list') & (type(x[1]).__name__ != 'dict') ]
    keys_list=[ (x[0],type(x[1]).__name__) for x in dicc.items() if type(x[1]).__name__ == 'list']
    keys_dict=[ (x[0],type(x[1]).__name__) for x in dicc.items() if type(x[1]).__name__ == 'dict']

    for tupla_key_type in keys_not_list_not_dict:
        key=tupla_key_type[0]
        kind=tupla_key_type[1]
        print(' '*padding,key,': ',kind)
    # dicts
    for tupla_key_type in keys_dict:
        key=tupla_key_type[0]
        kind=tupla_key_type[1]
        child_dict=dicc[key]
        print(' '*padding,key,': ',kind,'with',len(child_dict.keys()),'keys')
        padding_next=padding+5
        get_tree(child_dict,padding_next)
    # listas
    for tupla_key_type in keys_list:
        key=tupla_key_type[0]
        kind=tupla_key_type[1]
        lista=dicc[key]
        if (len(lista)>1 and check_list_dicts(lista)) : 
            try:
              print(' '*padding,key,': ',kind,'of',len(lista),'dicts with',len(lista[0].keys()),'keys each')
              padding_next=padding+5
              get_tree(lista[0],padding_next)
            except Exception as e:
              print('Error 1',e)

        else:
            if len(lista) >0:
              print(' '*padding,key,': '+ ' list of : ',len(lista), type(lista[0]))
            else:
              print(' '*padding,key,': '+ ' emtpy list')
        

                    
def check_list_dicts(lista):
    lista_dicts=[]
    for x in lista:
        if isinstance(x, dict):
            lista_dicts.append(1)
    if len(lista) == len (lista_dicts):
        return True
    else:
        return False
