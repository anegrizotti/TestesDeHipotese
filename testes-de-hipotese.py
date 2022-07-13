#Th para variâncias de populações normais
import statistics
import numpy as np
import math
import scipy.stats as st

def th_chi_bilateral(h0, graus, var, alpha): 
  chicalc=graus*var/h0
  print("qui_quad_calc",chicalc)
  X1=st.chi2.ppf((alpha/100)/2,graus)
  X2=st.chi2.ppf(1-(alpha/100)/2,graus)
  print("O valor do qui1 é:",X1, "O valor de qui2 é:", X2)

  if chicalc>X1 and chicalc<X2:
    print("Não rejeitar a hipótese inicial porque tcalc pertence à RNR") 
  else:
    print("Rejeitar a hipótese inicial porque tcalc pertence à RC") 

def th_chi_esquerda(h0, graus, var, alpha): #<
  chicalc=graus*var/h0
  print("qui_quad_calc",chicalc)
  X=st.chi2.ppf(alpha/100,graus)
  print("O valor do qui_quadrado é:",X)

  if chicalc > X:
    print("Não rejeitar a hipótese inicial porque tcalc pertence à RNR")
  else:
    print("Rejeitar a hipótese inicial porque tcalc pertence à RC")

def th_chi_direita(h0, graus, var, alpha): 
  chicalc=graus*var/h0
  print("qui_quad_calc",chicalc)
  X=st.chi2.ppf(1-alpha/100,graus)
  print("O valor do qui_quadrado é:",X)

  if chicalc <X:
    print("Não rejeitar a hipótese inicial pois tcalc pertence à RNR")
  else:
    print("Rejeitar a hipótese inicial pois tcalc pertence à RC")


#TH para a média de populações normais com variâncias conhecidas
def th_media_var_conhecida_esquerda(media, u, var, n, alpha):
   zcalc = (media - u) / math.sqrt(var / n)
   print("z_calc", zcalc)
   zAlpha = st.norm.ppf(alpha / 100)
   print("O valor do z_alpha é:", zAlpha)

   if zcalc > zAlpha:
       print(
           "Não rejeitar a hipótese inicial porque tcalc pertence à RNR")  
   else:
       print(
           "Rejeitar a hipótese inicial porque tcalc pertence à RC") 
       
def th_media_var_conhecida_direita(media, u, var, n, alpha):
   zcalc = (media - u) / math.sqrt(var / n)
   print("z_calc", zcalc)
   zAlpha = st.norm.ppf(1 - (alpha / 100))
   print("O valor do z_alpha é:", zAlpha)

   if zcalc < zAlpha:
       print(
           "Não rejeitar a hipótese inicial porque tcalc pertence à RNR") 
   else:
       print(
           "Rejeitar a hipótese inicial porque tcalc pertence à RC")  
       
def th_media_var_conhecida_bilateral(media, u, var, n, alpha):
   zcalc = (media - u) / math.sqrt(var / n)
   print("z_calc", zcalc)
   zAlpha = st.norm.ppf((alpha / 100) / 2)
   print("O valor do z_alpha negativo é:", zAlpha)
   zalphaneg = st.norm.ppf(1 - (alpha / 100) / 2)
   print("O valor do z_alpha positivo é:", zalphaneg)

   if zalphaneg < zcalc < zAlpha:
       print(
           "Não rejeitar a hipótese inicial porque tcalc pertence à RNR") 
   else:
       print(
           "Rejeitar a hipótese inicial porque tcalc pertence à RC") 
  

#TH para a média de populações normais com variâncias desconhecidas
import statistics
import numpy as np
import math
import scipy.stats as st

def th_media_var_desconhecida_esquerda(media, u, var, n, alpha):
   tcalc = (media - u) / math.sqrt(var / n)
   fi = n - 1
   print("t_calc", tcalc)
   tAlpha = st.t.ppf((alpha / 100), fi)
   print("O valor do t_alpha é:", tAlpha)
   if tcalc > tAlpha:
       print(
           "Não rejeitar a hipótese inicial porque tcalc pertence à RNR")  
   else:
       print(
           "Rejeitar a hipótese inicial porque tcalc pertence à RC") 


def th_media_var_desconhecida_direita(media, u, var, n, alpha):
   tcalc = (media - u) / math.sqrt(var / n)
   fi = n - 1
   print("t_calc", tcalc)
   tAlpha = st.t.ppf(1 - (alpha / 100), fi)
   print("O valor do t_alpha é:", tAlpha)

   if tcalc < tAlpha:
       print(
           "Não rejeitar a hipótese inicial porque tcalc pertence à RNR") 
   else:
       print(
           "Rejeitar a hipótese inicial porque tcalc pertence à RC")  

def th_media_var_desconhecida_bilateral(media, u, var, n, alpha): 
   fi = n - 1 
   tcalc = (media - u) / math.sqrt(var / n)
   print("t_calc", tcalc)
   tAlpha = st.t.ppf(1 - (alpha/100)/2,fi)
   print("O valor do t_alpha positivo é:", tAlpha)
   tAlphaNeg = st.t.ppf((alpha/100)/2,fi)
   print("O valor do t_alpha negativo é:", tAlphaNeg)

   if tAlphaNeg < tcalc < tcalc:
       print(
           "Não rejeitar a hipótese inicial porque tcalc pertence à RNR")  
   else:
       print(
           "Rejeitar a hipótese inicial porque tcalc pertence à RC")  


#TH para proporções de populações normais
def th_proporcoes_pop_normais_bilateral(p0, p, q0, n, alpha): 
   zcalc = (p0 - p) / math.sqrt((p0 * q0) / n)
   print("z_calc", zcalc)
   zAlpha = st.norm.ppf(1 - (alpha/100)/2)
   print("O valor do z_alpha positivo é:", zAlpha)
   zAlphaNeg = st.norm.ppf((alpha/100)/2)
   print("O valor do z_alpha negativo é:", zAlphaNeg)

   if zAlphaNeg < zcalc < zcalc:
       print(
           "Não rejeitar a hipótese inicial porque tcalc pertence à RNR")  
   else:
       print(
           "Rejeitar a hipótese inicial porque tcalc pertence à RC")  

def th_proporcoes_pop_normais_direita(p0, p, q0, n, alpha): 
   zcalc = (p0 - p) / math.sqrt((p0 * q0) / n)
   print("z_calc", zcalc)
   zAlpha = st.norm.ppf(1 - (alpha / 100))
   print("O valor do z_alpha é:", zAlpha)

   if zcalc < zAlpha:
       print(
           "Não rejeitar a hipótese inicial porque tcalc pertence à RNR")  
   else:
       print(
           "Rejeitar a hipótese inicial porque tcalc pertence à RC")  

def th_proporcoes_pop_normais_esquerda(p0, p, q0, n, alpha): 
   zcalc = (p0 - p) / math.sqrt((p0 * q0) / n)
   print("z_calc", zcalc)
   zAlpha = st.norm.ppf(alpha / 100)
   print("O valor do z_alpha é:", zAlpha)

   if zcalc > zAlpha:
       print(
           "Não rejeitar a hipótese inicial porque tcalc pertence à RNR")  
   else:
       print(
           "Rejeitar a hipótese inicial porque tcalc pertence à RC")  


#TH para diferença entre médias de populações normais
import numpy as np
import statistics
import math

def calcula_Di(n):
  Xi = np.array([ [31.9, 35.4, 28, 39.1, 30.5, 31.9, 33, 29.6, 35.7, 30.2, 38.8, 35.9, 37.1, 36.2, 32.6, 36.9, 24.2, 28.5, 28.7, 41.1, 33.8, 32.1, 28.7, 35.4, 36.6, 34.3, 35.5, 34.2, 33.8, 25.3, 27.7, 21.9, 30, 36.8, 26.9] ], dtype= 'double')
  Yi = np.array([ [44.7, 54.6, 41.1, 46.7, 43.0, 46.6, 42.9, 48.7, 50.0, 47.9, 47.2, 58.0, 51.0, 41.1, 49.6, 51.3, 39.0, 45.6, 49.8, 54.4, 47.1, 45.5, 52.8, 49.4, 47.2, 54.8, 40.2, 45.4, 48.6, 50.0, 51.5, 55.0, 44.7, 42.2, 52.0] ], dtype= 'double')
  Di = Xi - Yi
  print("Di:", Di) 
  di2 = Di**2
  print("Di^2:", di2)
  somatorioDi2 = di2.sum()
  print("Somatorio Di^2:", somatorioDi2)
  somatorio = Di.sum()
  print("Somatorio:", somatorio)
  media = np.mean(Di)
  print("Média", media)
  s = math.sqrt((1/(n-1))*((somatorioDi2)-(somatorio**2)/n))
  print("Desvio Padrão", s)

def th_diferenca_media_pop_normal_direita(d, u, var, n, alpha): 
   tcalc = (d - u) / math.sqrt(var / n)
   fi = n - 1
   print("t_calc", tcalc)
   tAlpha = st.t.ppf(1 - (alpha / 100), fi)
   print("O valor do t_alpha é:", tAlpha)

   if tcalc < tAlpha:
       print(
           "Não rejeitar a hipótese inicial porque tcalc pertence à RNR")  
   else:
       print(
           "Rejeitar a hipótese inicial porque tcalc pertence à RC")  
       
def th_diferenca_media_pop_normal_esquerda(d, u, var, n, alpha):
   tcalc = (d - u) / math.sqrt(var / n)
   fi = n - 1
   print("t_calc", tcalc)
   tAlpha = st.t.ppf((alpha / 100), fi)
   print("O valor do t_alpha é:", tAlpha)

   if tcalc > tAlpha:
       print(
           "Não rejeitar a hipótese inicial porque tcalc pertence à RNR")  
   else:
       print(
           "Rejeitar a hipótese inicial porque tcalc pertence à RC")  

