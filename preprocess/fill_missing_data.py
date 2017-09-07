def fill(data):
  nullcount = data.drop(['SalePrice'], axis=1).isnull().sum().sum()
  print("Data has " + str(nullcount) + " missing values. Attempting to fill them in...")
  cleanData = data
  # fill in missing categorical data for each column
  # list from combi[missing_features].isnull().sum()
  # Alley: replacing 2721 missing values with "None"
  cleanData["Alley"] = data["Alley"].fillna("None")
  # BsmtCond: replace 82 null values with "None"
  cleanData["BsmtCond"] = data["BsmtCond"].fillna("None")
  # BsmtExposure: rplace 82 null values with "None"
  cleanData["BsmtExposure"] = data["BsmtExposure"].fillna("None")
  # BsmtFinSF1: replace single null with 0.. there is no basement for this house
  cleanData["BsmtFinSF1"] = data["BsmtFinSF1"].fillna(0)
  # BsmtFinSF2: replace single null with 0.. there is no basement for this house
  cleanData["BsmtFinSF2"] = data["BsmtFinSF2"].fillna(0)
  # BsmtFinType1: replace 79 missing with "None", no basement
  cleanData["BsmtFinType1"] = data["BsmtFinType1"].fillna("None")
  # BsmtFinType2: replace 80 missing with "None", no basement
  cleanData["BsmtFinType2"] = data["BsmtFinType2"].fillna("None")
  # BsmtFullBath: replace 2 values with 0, no basement means no full basement baths
  cleanData["BsmtFullBath"] = data["BsmtFullBath"].fillna(0)
  # BsmtHalfBath: replace 2 NA's with 0, no basement means no bathrooms
  cleanData["BsmtHalfBath"] = data["BsmtHalfBath"].fillna(0)
  # BsmtQual
  cleanData["BsmtQual"] = data["BsmtQual"].fillna("None")
  # BsmtUnfSF
  cleanData["BsmtUnfSF"] = data["BsmtUnfSF"].fillna(0)
  # Electrical replaced single missing value with the mode "SBrkr"
  cleanData["Electrical"] = data["Electrical"].fillna("SBrkr")
  # Exterior1st replace single missing value with "BrkFace" because other houses in "edwards" neighborhood with Flat roofstyle have BrkFace
  cleanData["Exterior1st"] = data["Exterior1st"].fillna("BrkFace")
  # Exterior2nd follow same rule as exterior1st
  cleanData["Exterior2nd"] = data["Exterior2nd"].fillna("BrkFace")
  # Fence: replacing 2348 missing values with "None"
  cleanData["Fence"] = data["Fence"].fillna("None")
  # FireplaceQu: replacing 1420 missing values with "None"
  cleanData["FireplaceQu"] = data["FireplaceQu"].fillna("None")
  # Functional: Assume typical functionality for 2 missing cases
  cleanData["Functional"] = data["Functional"].fillna("Typ")
  # GarageArea: assume the single missing value was area = 0
  cleanData["GarageArea"] = data["GarageArea"].fillna(0)
  # GarageCars: assume the missing value is cars = 0
  cleanData["GarageCars"] = data["GarageCars"].fillna(0)
  # GarageCond: assuming missing 159 garage condition is because there is no garage
  cleanData["GarageCond"] = data["GarageCond"].fillna("None")
  # GarageFinish: assume 159 missing garage
  cleanData["GarageFinish"] = data["GarageFinish"].fillna("None")
  # GarageQual: assumine missing garag 159 e quality means no garage
  cleanData["GarageQual"] = data["GarageQual"].fillna("None")
  # GarageType: assume missing 157 garage type means no garage: TODO: Why are there only 157 and not 159 missing?
  cleanData["GarageType"] = data["GarageType"].fillna("None")
  # GarageYrBlt: fill missing 159 garage year built's with the median.. TODO: find a better way to exclude this info if there is no garage
  cleanData["GarageYrBlt"] = data["GarageYrBlt"].fillna(data["YearBuilt"])
  # KitchenQual: Assume the 1 missing vlue gets the mode "TA"
  cleanData["KitchenQual"] = data["KitchenQual"].fillna("TA")
  # LotFrontage fill 486 values with the mean TODO: IMPROVE HOW TO DO THIS!!!
  cleanData["LotFrontage"] = data["LotFrontage"].fillna(data["LotFrontage"].mean())
  # MSZoning: fill the 4 missing values with the median "RL"
  cleanData["MSZoning"] = data["MSZoning"].fillna("RL")
  # MasVnrArea: for now, fill in the 23 values with 0 TODO: get more sophisticated here?
  cleanData["MasVnrArea"] = data["MasVnrArea"].fillna(0)
  # MasVnrType: for now, fill in the 24 values with the most common value "None" TODO: get more sophisticated here?
  cleanData["MasVnrType"] = data["MasVnrType"].fillna("None")
  # MiscFeature: assume for 2814 NA's that this means No feature or "None"
  cleanData["MiscFeature"] = data["MiscFeature"].fillna("None")
  # PoolQC: fill in the 2909 NA values with "None" for no pool
  cleanData["PoolQC"] = data["PoolQC"].fillna("None")
  # SaleType fill in the 1 NA value with "WD", the mode
  cleanData["SaleType"] = data["SaleType"].fillna("WD")
  # TotalBsmtSF: fill the one missing value in with 0, there is no basement
  cleanData["TotalBsmtSF"] = data["TotalBsmtSF"].fillna(0)
  # Utilities: fill in the 2 cases of missing Utilities with the mode, "AllPub"
  cleanData["Utilities"] = data["Utilities"].fillna("AllPub")

  nullcount = cleanData.drop(['SalePrice'], axis=1).isnull().sum().sum()
  print("After filling in missing values, there are " + str(nullcount) + " missing values remaining.")
  if nullcount > 0:
    print("The null values are:")
    nullseries = cleanData.drop(['SalePrice'], axis=1).isnull().sum()
    print(str(nullseries[nullseries > 0]))
  return cleanData
