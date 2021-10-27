class patient:
  def __init__(self, id_num, first_name, last_name, height_cm, weight_kg, age, rest_heart_rate):
    self.first_name = first_name
    self.last_name = last_name
    self.id_num = id_num
    self.height_cm = height_cm
    self.weight_kg = weight_kg
    self.age = age
    self.rest_heart_rate = rest_heart_rate

    def full_name(self):
        return f"{self.first_name} {self.last_name}"

patient_1 = patient("ARC345/98B", "John", "Smith", 190, 80, 49, 48)

print(patient_1.first_name, " ", patient_1.last_name)
print("weight: ", patient_1.weight_kg, " kg")
print(patient_1(full_name))
