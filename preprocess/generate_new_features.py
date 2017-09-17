def generate(data):

    # ultra simple category reductions for unimportant variables
    #data['AllBsmtFinSF'] = data['BsmtFinSF1'] + data['BsmtFinSF2']

    #data['TotalBathrooms'] = data['FullBath'] + 0.5*data['HalfBath'] + data['BsmtFullBath'] + 0.5*data['BsmtHalfBath']

    #data['TotalDeckArea'] = data['WoodDeckSF'] + data['OpenPorchSF'] + data['EnclosedPorch'] + data['3SsnPorch'] + data['ScreenPorch'] + data['PoolArea']

    return data
