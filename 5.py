def make_car(marka,model,**kwargs):
    print('Модель:',model,'\n','Марка:',marka)

make_car('subaru', 'outback', color='blue', tow_package=True)