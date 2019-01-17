from django.shortcuts import render
from core.models import user
from pandas import read_csv
import json
from pandas import DataFrame
from sklearn.model_selection import KFold
from sklearn.model_selection import cross_val_score
from sklearn.metrics import accuracy_score
from sklearn.svm import SVC
import random

# Create your views here.
def result(request):
    age = request.POST['age']
    gender = request.POST['gender']     #male 0 female 1
    weight = request.POST['weight']
    height = request.POST['height']
    sugar = request.POST['sugar']
    insulin = request.POST['insulin']
    skin = request.POST['skin']
    if_preg = request.POST['pregancy']
    pregtime = request.POST['pregancytime']
    pressure = request.POST['pressure']
    func = request.POST['func']

    age = int(age)
    weight = int(weight)
    height = int(height)
    sugar = int(sugar)
    pressure = int(pressure)
    pregtime = int(pregtime)
    insulin = int(insulin)

    try:
        skin = int(skin)
    except ValueError :
        skin=0

    try:
        func = float(func)
    except ValueError :
        func=0

    height = height/100
    bmi = weight/(height*height)

    users = user()
    users.func = func
    users.insulin = insulin
    users.age = age
    if gender == '1':
        users.gender = True
    else:
        users.gender = False
    users.blood_sugar = sugar
    users.bmi = bmi
    users.blood_pressure = pressure
    if if_preg == '1':
        users.ifpreg = True
    else:
        users.ifpreg = False
    users.pregancy = pregtime
    users.skin_thickness = skin
    users.No = random.randint(100000,999999)




    filename = 'rsc/pima_data.csv'
    names = ['preg', 'plas', 'pres', 'skin', 'test', 'mass', 'pedi', 'age', 'class']
    data = read_csv(filename, names=names)
    # 获取数据，设置初始参数
    array = data.values
    X = array[:, 0:8]
    Y = array[:, 8]
    num_flod = 10
    seed = 7
    kfold = KFold(n_splits=num_flod, random_state=seed)
    svm = SVC()
    # 训练模型
    svm.fit(X=X, y=Y)
    # 通过训练模型预测得到预测值
    predictions = svm.predict(X)
    # 输出训练精度
    print('训练精度：')
    print(accuracy_score(Y, predictions))
    # 预测第一条数据
    x = DataFrame([[pregtime, sugar, pressure, skin, insulin, bmi, func, age]])
    prediction = svm.predict(x)
    print('第一条数据预测结果输出：')
    print(svm.predict(x))
    # 评估模型优良
    result = cross_val_score(svm, X, Y, cv=kfold)
    print('标准评估模型结果：')
    print(result.mean())
    temp = list(svm.predict(x))
    res1 = 'True'
    res2 = 'False'
    temp1 = temp[0]
    if temp1 == 1:
        users.result = True
        temp1 = res1
    else:
        users.result = False
        temp1 = res2

    users.save()
    print(pregtime, sugar, pressure, skin, insulin, bmi, func, age)

    return render(request, 'result.html', {'训练精度':accuracy_score(Y, predictions), 'result':json.dumps(temp1), '评估':result.mean(), 'bmi':round(bmi,2)})
    # json.dumps(temp1)
def index(request):
    return render(request, 'index.html')

def showInput(request):
    return render(request, 'input.html')
