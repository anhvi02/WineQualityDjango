from django.shortcuts import render
import joblib 
# Create your views here.

def home(request):
    return render(request,'predict/home.html')

def result(request):
    reg = joblib.load("model/final_model.sav") 
    lis = []

    cols = ['fixed acidity', 'volatile acidity', 'citric acid', 'residual sugar',
       'chlorides', 'free sulfur dioxide', 'total sulfur dioxide', 'density',
       'pH', 'sulphates', 'alcohol']

    for col in cols:
        lis.append(float(request.GET[col]))

    answer = reg.predict([lis])
    if answer == 0:
        answer = 'Bad Quality'
    else:
        answer = 'Good Quality'
    inputs = zip(cols, lis)
    return render(request, 'predict/result.html',{'answer': answer,'inputs':inputs})
