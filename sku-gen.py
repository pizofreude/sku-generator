import pandas as pd
import os


__location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__))) # Identifying path

colors = pd.read_csv(os.path.join(__location__, 'CHARTS/colors.csv')) # Importing Chart of Colors
models = pd.read_csv(os.path.join(__location__, 'CHARTS/categories-subcategories.csv')) # Importing Chart of Models



def colorist(file): #Function to switch Colors to Color Codes
    
    fake_id_parts = pd.DataFrame(file, columns = ['U_COLOR'])
    l = len(fake_id_parts)
    i = 0
    
    for color_list in fake_id_parts['U_COLOR']:
        
        coded_colors = []
        #print(color_list)
        #print(type(color_list))
        for color in str(color_list).split(','):
               
             if i < l:
                #print(color) 
                st = str.strip(color)
                #print(color)
                c = colors.loc[colors['Name'] == st]
                if len(c) > 0:
                    a = str(c.iloc[0,0])
                
                    coded_colors.append(a)
                else:
                    coded_colors.append('')
                
        coded_colors = str(coded_colors)
        coded_colors = coded_colors.replace('\'','')
        coded_colors = coded_colors.replace('[','')
        coded_colors = coded_colors.replace(']','')
        print(coded_colors)
        
        #print(z)
        file.at[i, 'COLOR'] = coded_colors
        print('=====================')
        print('ItemCode ' + str(file.at[i, 'ItemCode']) + ' |COLOR CODE: ' + coded_colors)
        #print(z)
        i +=  1
    
       

    
    file.to_csv((os.path.join(__location__,'Results/COLORIST_result.csv'))) #save results

    print('============================================================')
    print(str(i) + ' ITEMS COLORS CODED' )
    print('COLORIST FUNCTION DONE CODING COLORS!')
    print('RESULT SAVED AS COLORIST_result.csv')
    print('============================================================')

def sku_gen(column, file, sep): #main function for Sku generatiobn
    
    data_column = pd.DataFrame(file, columns= [column], dtype = str) #taking one column from file to use as main reference for Sku Generation
    index = 0
    
    print('============================================================')
    print(str(len(data_column)) + ' ITEMS HAS BEEN RECIVED. ' + column + ' GENERATION IS STARTING')
    print('============================================================')
    
    
    for column_name, item in data_column.iteritems(): #iteration through data columns (2 columns: index and variables)
        
        i = - 1 #index for new items
        add_counter = 0 #counter for cases when SKU can be rewritten in the same row instead of copying
        
        for variables in item.tolist(): #iteration through variables column

            
            
                
                variable_as_str = str(variables)
                variables_list = variable_as_str.split(',') #split variables
               
                    
                
                if len(variables_list) > 1 and ( file.at[index, 'ItemCode'] != 'USED'): # Check if the variable is a list of variables 
                    
                    for var in variables_list : #if yes make a copy of the row and add variable in the column instead of the list of variables

                        #if '.' in var:
                            #var = var.split('.')[0]
                        print(var)
                        file.loc[i] = file.iloc[index]
                        file.at[i, 'ItemCode'] = str.strip(str(file.at[i, 'ItemCode']))+sep+str.strip(var)
                        file.at[i, column] = str.strip(var)
                        
                        print(file.at[i, 'ItemCode'])
                        print(column + ' GENERATED')
                        print('===============================================')
                        i -= 1
                        
                    file.at[index, 'ItemCode'] = 'USED'
                    
                elif (variables_list[0] != 'nan') and ( file.at[index, 'ItemCode'] != 'USED'): #Check is there a variable
                    if '.' in variable_as_str:
                        variable_as_str = variable_as_str.split('.')[0]
                    file.at[index, 'ItemCode'] = str.strip(str(file.at[index, 'ItemCode']))+sep+str.strip(variable_as_str) 
                    add_counter = add_counter + 1 #if yes add value from column to ItemCode
                    print('--------------------')
                    print(file.at[index, 'ItemCode'])
                    print(column+' ADDED')
                    
                index += 1
                
        amount = int(str(i)[1:]) - 1
        am = str(amount)
        print('-----------------------------------------------------------------------------------')
        print(column+' GENERATED: ' + am + ' SKUs')
        print(column+' ADDED: ' + str(add_counter) + ' SKUs')
        print('-----------------------------------------------------------------------------------')
    
    file.to_csv((os.path.join(__location__,'Results/'+column+'_result.csv')))
   
    
file_str = 'sku_gen_template.csv'

#description_edit(immport_file)



immport_file = pd.read_csv(os.path.join(__location__, file_str))


#immport_file = pd.read_csv(os.path.join(__location__, 'MODELIST_result.csv'))
colorist(immport_file)


immport_file = pd.read_csv(os.path.join(__location__, file_str))
sku_gen('SupplierCatalogNo', immport_file , '')
immport_file = pd.read_csv(os.path.join(__location__, 'Results/SupplierCatalogNo_result.csv'))
sku_gen('U_SIZE', immport_file, '-' )
immport_file = pd.read_csv(os.path.join(__location__, 'Results/U_SIZE_result.csv'))
sku_gen('U_VARIABLE', immport_file, '-' )
immport_file = pd.read_csv(os.path.join(__location__, 'Results/U_VARIABLE_result.csv'))
sku_gen('OC', immport_file, '-' )
immport_file = pd.read_csv(os.path.join(__location__, 'Results/OC_result.csv'))
sku_gen('U_LOGO', immport_file,'-' )
immport_file = pd.read_csv(os.path.join(__location__, 'Results/U_LOGO_result.csv'))


immport_file = immport_file[immport_file['ItemCode'] != 'USED'] #delete parent items
immport_file.to_csv('Results/final'+'_result.csv') #save results
print('===================================')
print('GENERATION IS DONE')
print('===================================')

immport_file = pd.read_csv(os.path.join(__location__, 'Results/final_result.csv'))

for col in immport_file:
            #print(col)
            if 'Unnamed' in str(col):
                #print('c')
                
                immport_file.drop(col,inplace=True, axis=1)




immport_file.to_csv(file_str[:-4] + '_result.csv')

