
#print(type(73.19))
counties = ["Arapahoe","Denver","Jefferson"]
counties.insert(1,"El Paso")
counties.remove("Arapahoe")
counties[2]="Denver"
counties[1]="Jefferson"
counties.append("Arapahoe")
counties_tuple=("Arapahoe","Denver","Jefferson")
counties_dict={}
counties_dict["Arapahoe"]=422829
counties_dict["Denver"] = 463353
counties_dict["Jefferson"] = 432438
print(counties_dict.get('Arapahoe'))
print(counties_dict)
print(counties_dict.keys())
#print(counties_dict.values())
voting_data=[]
voting_data.append({"county":"Arapahoe", "registered_voters": 422829})
voting_data.append({"county":"Denver", "registered_voters": 463353})
voting_data.append({"county":"Jefferson", "registered_voters": 432438})
voting_data.insert(1,{"county":"El Paso", "registered_voters":461149})
voting_data.remove({"county":"Arapahoe", "registered_voters": 422829})
voting_data[1]={"county":"Jefferson", "registered_voters": 432438}
voting_data[2]={"county":"Denver", "registered_voters": 463353}
voting_data.append({"county":"Arapahoe", "registered_voters": 422829})
print(voting_data)