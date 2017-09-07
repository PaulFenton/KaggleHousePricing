def remap(data):
  numcategories = data.select_dtypes(include=['object']).columns.size
  numcontinuous = data.select_dtypes(include=['float64', 'int64']).columns.size
  print("Starting re-mapping with " + str(numcategories) + " categorical variables, and " + str(numcontinuous) + " continuous variables.")

  data = numerical_to_categorical(data)
  data = categorical_to_numerical(data)
  data = reduce_categorical(data)

  numcategories = data.select_dtypes(include=['object']).columns.size
  numcontinuous = data.select_dtypes(include=['float64', 'int64']).columns.size
  print("Finishd re-mapping with " + str(numcategories) + " categorical variables, and " + str(numcontinuous) + " continuous variables.")

  return data

def numerical_to_categorical(data):
  # convert numerical data that is really categorical
  data = data.replace({"MSSubClass": {20: "SC20", 30: "SC30", 40: "SC40", 45: "SC45",
                                        50: "SC50", 60: "SC60", 70: "SC70", 75: "SC75",
                                        80: "SC80", 85: "SC85", 90: "SC90", 120: "SC120",
                                        150: "SC150", 160: "SC160", 180: "SC180", 190: "SC190"},
                         "MoSold": {1: "Jan", 2: "Feb", 3: "Mar", 4: "Apr", 5: "May", 6: "Jun",
                                    7: "Jul", 8: "Aug", 9: "Sep", 10: "Oct", 11: "Nov", 12: "Dec"}
                         })
  return data

def categorical_to_numerical(data):
  # replace ordinal categories with numeric values

  data = data.replace({"Alley": {"None": 0, "Grvl": 1, "Pave": 2},
                       "CentralAir": {"N": 0, "Y": 1},
                         "BsmtCond": {"None": 0, "Po": 1, "Fa": 2, "TA": 3, "Gd": 4, "Ex": 5},
                         "BsmtExposure": {"No": 0, "None": 0, "Mn": 1, "Av": 2, "Gd": 3},
                         "BsmtFinType1": {"None": 0, "Unf": 1, "LwQ": 2, "Rec": 3, "BLQ": 4,
                                          "ALQ": 5, "GLQ": 6},
                         "BsmtFinType2": {"None": 0, "Unf": 1, "LwQ": 2, "Rec": 3, "BLQ": 4,
                                          "ALQ": 5, "GLQ": 6},
                         "BsmtQual": {"None": 0, "Po": 1, "Fa": 2, "TA": 3, "Gd": 4, "Ex": 5},
                         "Electrical": {"SBrkr": 2, "FuseA": 1, "FuseF": 1, "FuseP": 0, "Mix": 1},
                         "ExterCond": {"Po": 1, "Fa": 2, "TA": 3, "Gd": 4, "Ex": 5},
                         "ExterQual": {"Po": 1, "Fa": 2, "TA": 3, "Gd": 4, "Ex": 5},
                         "FireplaceQu": {"None": 0, "Po": 1, "Fa": 2, "TA": 3, "Gd": 4, "Ex": 5},
                         "Functional": {"Sal": 1, "Sev": 2, "Maj2": 3, "Maj1": 4, "Mod": 5,
                                        "Min2": 6, "Min1": 7, "Typ": 8},
                         "GarageCond": {"None": 0, "Po": 1, "Fa": 2, "TA": 3, "Gd": 4, "Ex": 5},
                         "GarageQual": {"None": 0, "Po": 1, "Fa": 2, "TA": 3, "Gd": 4, "Ex": 5},
                         "GarageFinish": {"None": 0, "Unf": 1, "RFn": 2, "Fin": 3},
                         "HeatingQC": {"Po": 1, "Fa": 2, "TA": 3, "Gd": 4, "Ex": 5},
                         "KitchenQual": {"Po": 1, "Fa": 2, "TA": 3, "Gd": 4, "Ex": 5},
                         "LandSlope": {"Sev": 1, "Mod": 2, "Gtl": 3},
                         "LotShape": {"IR3": 1, "IR2": 2, "IR1": 3, "Reg": 4},
                         "PavedDrive": {"N": 0, "P": 1, "Y": 2},
                         "PoolQC": {"None": 0, "Fa": 1, "TA": 2, "Gd": 3, "Ex": 4},
                         "Street": {"Grvl": 1, "Pave": 2},
                         "Utilities": {"ELO": 1, "NoSeWa": 2, "NoSewr": 3, "AllPub": 4}}
                        )
  return data

def reduce_categorical(data):
  data = data.replace({
                   "BldgType": {"2fmCon": "Duplex"},
                   "Condition1": {"Artery": "BadAdjacency", "RRAn": "BadAdjacency", "RRAe": "BadAdjacency",
                                  "Feedr": "Norm", "RRNn": "Norm", "RRNe": "Norm",
                                  "PosA": "GoodAdjacency", "PosN": "GoodAdjacency"},
                  "Condition2": {"Artery": "BadAdjacency", "RRAn": "BadAdjacency", "RRAe": "BadAdjacency",
                                   "Feedr": "Norm", "RRNn": "Norm", "RRNe": "Norm",
                                   "PosA": "GoodAdjacency", "PosN": "GoodAdjacency"},
                  "Exterior1st": { "CBlock": "Other", "BrkComm": "Other", "Stone": "Other", "AsphShn": "Other",
                                "ImStucc": "Other", "Brk Cmn": "Other", "AsbShng": "Other", "Stucco": "Other"},
                  "Exterior2nd": {"CBlock": "Other", "BrkComm": "Other", "Stone": "Other", "AsphShn": "Other",
                                "ImStucc": "Other", "Brk Cmn": "Other", "AsbShng": "Other", "Stucco": "Other"},
                  "MoSold": {"Jan": "Q1", "Feb": "Q1", "Mar": "Q1",
                             "Apr": "Q2", "May": "Q2", "Jun": "Q2",
                             "Jul": "Q3", "Aug": "Q3", "Sep": "Q3",
                             "Oct": "Q4", "Nov": "Q4", "Dec": "Q4"},
                  "MSSubClass": {"SC30": "SmallOld", "SC40": "SmallOld", "SC45": "SmallOld",
                                 "SC70": "2StoryOld", "SC75": "2StoryOld", "SC80": "2StoryOld", "SC85": "2StoryOld",
                                 "SC150": "SC160"},
                  "MSZoning": {"RH": "RM"},
                  "LandContour": {"Low": "Lvl"},
                  "LotConfig": {"Inside": "Avg", "FR2": "Avg", "Corner" : "Avg",
                                "CulDSac": "Desirable", "FR3": "Desirable"},
                  "HouseStyle": {"SLvl": "1Story", "SFoyer": "1Story", "1.5Unf": "1Story", "2.5Unf": "1Story",
                                 "2.5Fin": "2Story"},
                  "RoofStyle": {"Gambrel": "Gable", "Shed": "Gable",
                                "Mansard": "Hip", "Flat": "Hip"},
                  "MasVnrType": {"BrkCmn": "None"},
                  "Foundation": {"Wood": "CBlock", #filling in with cheap and common
                                 "Slab": "BrkTil", "Stone": "BrkTil"},
                  "Heating": {"GasA": "Normal", "GasW": "Normal", "OthW": "Normal",
                              "Grav": "Cheap", "Wall": "Cheap", "Floor": "Cheap"},
                  "GarageType": {"CarPort": "Attchd", "Basement": "Attchd", "2Types": "Attchd"},
                  "SaleType": {"ConLD": "Oth", "ConLI": "Oth", "CWD": "Oth", "ConLw": "Oth", "Con":"Oth"},
                  "SaleCondition": {"Partial": "Normal", "AdjLand": "Normal", "Alloca": "Normal", "Family": "Normal"}
  })
  return data
