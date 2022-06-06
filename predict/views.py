from django.shortcuts import render
import joblib 
# Create your views here.

def home(request):
    return render(request,'predict/home.html')

def result(request):
    reg = joblib.load("model/final_model.sav") 
    predict_val = []

    features = ['fixed acidity', 'volatile acidity', 'citric acid', 'residual sugar',
       'chlorides', 'free sulfur dioxide', 'total sulfur dioxide', 'density',
       'pH', 'sulphates', 'alcohol']

    for fea in features:
        predict_val.append(float(request.GET[fea]))

    answer = reg.predict([predict_val])
    if answer == 0:
        answer = 'BAD QUALITY'
    else:
        answer = 'GOOD QUALITY'

    context = {
        'answer' : answer
    }
    for fea, val in zip(features, predict_val):
        context[fea.replace(' ','_')] = val
    # render_cols = []
    # for col in cols:
    #     render_cols.append(col.capitalize())
    # inputs = zip(render_cols, predict_val)
    print(context)


    return render(request, 'predict/result.html',context=context)
