# -*- coding: utf-8 -*-
"""
Created on Wed Mar  1 13:58:27 2023

@author: Acer
"""

import numpy as np
import pickle
import streamlit as st

# loading the saved model
loaded_model = pickle.load(open('C:/Users/Acer/Desktop/ML deployment/trained_wine_model.sav', 'rb'))

# creating a function for prediction

def red_wine_prediction(input_data):
    
   # changing the input data to a numpy array
   input_data_as_numpy_array = np.asarray(input_data)

   # reshape the data as we are predicting the label for only one instance
   input_data_reshaped = input_data_as_numpy_array.reshape(1,-1)

   prediction = loaded_model.predict(input_data_reshaped)
   print(prediction)

   if (prediction[0]==1):
     return 'Good Quality Wine'
   else:
     return 'Bad Quality Wine'
      
      
def main():
      
      # giving a title
      st.title('Check Red Wine Quality')
      
      
      #getting input from user
      
    

      
      fixedacidity = st.text_input('Fixed Acidity Level')
      volatileacidity = st.text_input('Volatile Acidity Level')
      citricacid = st.text_input('Citric Acid Level')
      residualsugar = st.text_input ('Residual Sugar Value')
      chlorides = st.text_input('Chlorides level')
      freesulfurdioxide = st.text_input('Free Sulfur Dioxide Level')
      totalsulfurdioxide = st.text_input('Total Sulfur Dioxide Level')
      density = st.text_input('Density value of Wine')
      pH = st.text_input('pH value of Wine')
      sulphates = st.text_input('Sulphate in Wine')
      alcohol = st.text_input('Amount of Alcohol present in  Wine')
      
      
     
      
      #code for prediction
      quality = ''
      
      
      # creating a button for prediction
      
      if st.button('Red Wine Quality Check'):
          quality = red_wine_prediction([fixedacidity,volatileacidity,citricacid,residualsugar,chlorides,freesulfurdioxide,totalsulfurdioxide,density,pH,sulphates,alcohol])
      
        
      st.success(quality)
      
      
      
if __name__== '__main__':
    main()
    