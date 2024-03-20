def NumericOptionArray(FirstOption, LastOption, Increment):
    result = []
    OptionValue = FirstOption
    
    if FirstOption < LastOption and Increment > 0:
        while OptionValue <= LastOption:
            result.append([str(OptionValue), str(OptionValue)])
            OptionValue += Increment
    else:
        while OptionValue >= LastOption:
            result.append([str(OptionValue), str(OptionValue)])
            OptionValue += Increment
        
    return result
