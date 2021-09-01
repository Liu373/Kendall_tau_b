
import pandas as pd
import math
import statistics
import scipy.stats as stats



Class Kendall_tau_b:
  
  def __init__(self, x, y, name):
    
    self.x    = x
    self.y    = ye
    self.name = name
    self.z    = 1.95996398454005
    
    
  def Q(self, i, j):
    
    q = 0
    ij = (j[1] - i[1]) * (j[0] - i[0])
    
    if ij > 0:
      q_ij = 1
      
    if ij < 0:
      q_ij = -1
      
    if ij == 0:
      q_ij = 0
      
    q = q + q_ij
    
    return q
  
  
  
  
  
  def Ci(self, x, y, i):
    
    ci = 0
    
    for k in range(0, len(x)):
      if k != i:
        ci = ci + self.Q([x[i], y[i]], [x[k], y[k]])
        
    return ci
  
  
  
  
  
  def main(self):
    
    global tau_hat, p_values, tau_L, tau_U
    
    c_i = []
    n = len(self.x)
    
    for i in range(0, n):
      a = self.Ci(self.x, self.y, i)
      c_i.append(a)
      
      
    tau_hat, p_values = stats.kendalltau(self.x, self.y)
    
    sigma_hat_2 = 2 * (n-2) * statistics.variance(c_i) / n / (n-1)
    sigma_hat_2 = sigma_hat_2 + 1 - (tau_hat)**2
    sigma_hat_2 = sigma_hat_2 * 2 / n / (n-1)
    
    tau_L = tau_hat - self.z * math.sqrt(sigma_hat_2)
    tau_U = tau_hat + self.z * math.sqrt(sigma_hat_2)
    
    
    print("\n")
    print("-" * 50)
    print("\n")
    print("{0}'s Statistics".format(self.name))
    print("\n")
    print("Rank Correlation:     {0}".format(round(tau_hat, 5)))
    print("\n")
    print("P Value:              {0}".format(round(p_value, 5)))
    print("\n")
    print("Confidence Interval:  {0} and {1}".format(round(tau_L, 5), round(tau_U, 5)))
    print("\n")
    print("-" * 50)
    
    
    
  
  
  


if __name__ == '__main__':
  
  Rc = pd.read_excel(r"C:\xxxxx\xxxx\xxxxx.xlsx")
  
  x1_Name = "xxxAssmt"
  x2_Name = "Finxxx"
  x3_Name = "Induxxx"
  x4_Name = "Manaxxx"
  
  
  x1 = list(Rc[x1_Name])
  x2 = list(Rc[x2_Name])
  x3 = list(Rc[x3_Name])
  x4 = list(Rc[x4_Name])
  y1 = list(Rc["xx_Ratxx_Num"])
  
  
  Kendall = Kendall_tau_b(x1, y1, x1_Name)
  Kendall.main()
  
  Kendall = Kendall_tau_b(x2, y2, x2_Name)
  Kendall.main()
  
  xx
  xx
  xx
  xx
  xx
  xx

    
          
          
          
          
          
          
          
    
    



























