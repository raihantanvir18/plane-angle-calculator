from django.shortcuts import render,HttpResponse
from .forms import EquationForm
from .models import Equation
import numpy as np
import math
import re
def home(request):
    return render(request, 'home.html')
def about(request):
    return render(request,'home.html')

def contact(request):
    return render(request,'home.html')



def equation_generator(request):
    return render(request,'equation_generator.html')

def proof_of_coordinate(request):
    return render(request,'proof_of_coordinate.html')



def extract_coefficients(equation):

    pattern = r'([-+]?\d*\.\d+|[-+]?\d*)\s*([xyz]?)'


    matches = re.findall(pattern, equation)

    coefficients = [0.0, 0.0, 0.0,]

    for coefficient, variable in matches:
        if coefficient:
            if coefficient == '-':
                coeff_value = -1.0  
            elif coefficient == '+':
                coeff_value = 1.0   
            else:
                coeff_value = float(coefficient)
        else:
            coeff_value = 1.0  

        if variable == 'x':
            coefficients[0] += coeff_value
        elif variable == 'y':
            coefficients[1] += coeff_value
        elif variable == 'z':
            coefficients[2] += coeff_value

    return coefficients
def calculate_angle(equation1, equation2):
    coefficients11 = []
    coefficients12 = []  


    equation_parts = equation1.split('=')
   

    if len(equation_parts) == 2:
     left_equation = equation_parts[0].strip() 
     right_equation = equation_parts[1].strip() 
   
     print(left_equation)
     print(right_equation)
     
    else:
     print("Invalid equation format. There should be exactly one '=' sign.")
   
    
    coefficients11=extract_coefficients(left_equation)
    coefficients12=extract_coefficients(right_equation)
    coefficients2 = extract_coefficients(equation2)
   
    a=coefficients11[0]
    b=coefficients11[1]
    c=coefficients11[2]
  
    a1=coefficients12[0]
    b1=coefficients12[1]
    c1=coefficients12[2]

    a3=coefficients2[0]
    b3=coefficients2[1]
    c3=coefficients2[2]

   
    eq1 = np.array([a,b,c])
    eq2 = np.array([a1,b1,c1])
    eq3 = np.array([a3,b3,c3])

    x = np.cross(eq1, eq2)
    y1 = np.dot(x, eq3)
    y2 = np.sum(y1)

    x_magnitude = math.sqrt(np.sum(x ** 2))
    eq3_magnitude = math.sqrt(np.sum(eq3 ** 2))
    x1 = x_magnitude * eq3_magnitude

    angle_degrees = math.degrees(math.asin(abs(y2) / x1))
    return angle_degrees
    


def calculator(request):
    if request.method == 'POST':
        form = EquationForm(request.POST)
        if form.is_valid():
            equation1 = form.cleaned_data['equation1']
            equation2 = form.cleaned_data['equation2']
            result = calculate_angle(equation1, equation2)

            # Save the result to the database
            equation = Equation(equation1=equation1, equation2=equation2, result=result)
            equation.save()

            return render(request, 'result.html', {'result': result})
    else:
        form = EquationForm()

    return render(request, 'calculator.html', {'form': form})


def calculate_angle_from_equations(equation1, equation2):

    coefficients1 = extract_coefficients(equation1)
    coefficients2 = extract_coefficients(equation2)
    a1=coefficients1[0]
    b1=coefficients1[1]
    c1=coefficients1[2]

    a2=coefficients2[0]
    b2=coefficients2[1]
    c2=coefficients2[2]

    D = a1 * a2 + b1 * b2 + c1 * c2
    N1 = math.sqrt(a1 * a1 + b1 * b1 + c1 * c1)
    N2 = math.sqrt(a2 * a2 + b2 * b2 + c2 * c2)
    angle_degrees = math.degrees(math.acos(D / (N1 * N2)))

    return angle_degrees

def calculator11(request):
    if request.method == 'POST':
        form = EquationForm(request.POST)
        if form.is_valid():
            equation1 = form.cleaned_data['equation1']
            equation2 = form.cleaned_data['equation2']
            
            # Calculate the angle using the new function
            result = calculate_angle_from_equations(equation1, equation2)
            
            print("Calculated Angle:", result)

            return render(request, 'result.html', {'result': result})
    else:
        form = EquationForm()

    return render(request, 'calculator11.html', {'form': form})


   