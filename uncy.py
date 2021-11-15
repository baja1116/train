train_mass = 22680
train_acceleration = 10
train_distance = 100
bomb_mass = 1

def f_to_c(f_temp):
  return (f_temp - 32) * 5/9

f100_in_celsius = f_to_c(100)

def c_to_f(c_temp):
  return (c_temp * 9/5) +32

c0_in_american = c_to_f(0)
print(c0_in_american)

def get_force(mass, acceleration):
  return mass * acceleration 

train_force = get_force(train_mass, train_acceleration)
print("The GE train supplies" + str(train_force) + " Newtons of Force.")

def get_energy(mass, c=3*10**8): 
  return mass * c**2

bomb_energy = get_energy(bomb_mass)
print("a 1kg bomb supplies" + str(bomb_energy) +  " joules. ")

def get_work(mass, acceleration, distance):
  force = get_force(mass, acceleration)
  return force * distance 

train_work = get_work(train_mass, train_acceleration, train_distance)

print(" the GE train does" + str(train_work) + " joules of work over " + str(train_distance) + " meters. ")
