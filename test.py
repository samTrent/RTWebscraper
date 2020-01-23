import pickle 

sample_dicts = [{"headers": ["aa", "bb", "cc"]}, 
                {"headers": ["dd", "ee", "ff"]},
                {"headers": ["gg", "hh", "ii"]}]

input_filename = "output_data.pickle"
output_filename = "output_data.pickle"

class Label_Helper:
  def load_Data(self, input_filename):
    input_file = open(input_filename, "rb")
    tables_dict = pickle.load(input_file)
    input_file.close()
    print(tables_dict)
    return tables_dict

  def save_Data(self, output_filename):
    output_file = open(output_filename, "wb")
    pickle.dump(self.tables_dict, output_file)
    output_file.close()

  def __init__(self, tables_dict, input_filename):
    if tables_dict == None:
      tables_dict = self.load_Data(input_filename)
    self.tables_dict = tables_dict

  def label_tables(self):
    index = 0
    retried = False
    error = False
    print(len(self.tables_dict))
    while index < len(self.tables_dict) and not error:
      print(self.tables_dict[index]["headers"])
      validity_value = input()
      # 1 == True
      if validity_value == "1":
        self.tables_dict[index]["label"] = "True"
        retried = False
      # 2 == False
      elif validity_value == "2":
        self.tables_dict[index]["label"] = "False"
        retried = False
      # 3 == Undo
      elif validity_value == "3" and not retried:
        index -= 1
        retried = True
      # 4 == Skip
      elif validity_value == "4" or retried:
        retried = False
      else:
        error = True
      index += 1

#create the object
data_labeler = Label_Helper(sample_dicts, input_filename)

#check if data_labeler has data
if data_labeler.load_Data(input_filename):
    #Set the object to the new object found 
    data_labeler = data_labeler.load_Data(input_filename)
