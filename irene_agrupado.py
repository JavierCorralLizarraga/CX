

#se actualiza el nombre del archivo de MA y el IC requerido
# excel_filename = '' # descomenta si quieres utilizar un nombre personalizado
poblacion_total = 100000 # poblacion distinto a la muestra que se le esta pasando para calcular el error
IndiceDeConfianza = 80 # declaramos el indice de confianza
#column_letter = 'I'
#column_letter_group = 'EW'
column_letter = 'AG'  # declaramos la letra de la columna de irenes que queremos
column_letter_group = 'J' # declaramos la letra de la columna por la cual queremos agrupar


file_path = excel_filename
df = pd.read_excel(file_path)
#df = pd.read_excel("BD MA ACUM Ene23-Sep23_59668 (cerrado) Vol.xlsx")
column_index = column_index_from_string(column_letter) - 1
column_data = df.iloc[:, column_index]
print("la siguiente es la informacion que se tomara") # deberian ser solo numeros (probablemente enteros) # pero si no lo es solo toma los valores numericos
column_data=column_data.drop(column_data.index[1043:1045])
column_data
#len(column_data)


file_path = excel_filename
df = pd.read_excel(file_path)
column_index = column_index_from_string(column_letter_group) - 1
column_data_group = df.iloc[:, column_index]
print("la siguiente es la informacion por la cual se agrupara") # deberian ser solo numeros (probablemente enteros) # pero si no lo es solo toma los valores numericos
column_data_group

column_data_group.unique()

two_series = pd.concat([column_data_group, column_data], axis=1, keys= ['col1', 'col2'])
#print(two_series['col1'].unique())
#two_series
# filtramos todos los numeros decimales o enteros
#two_series = two_series[column_data.astype('str').apply(lambda x : x.replace('.','',1).isdigit())]
two_series.col2 = two_series.col2#.astype('float')
#column_data = column_data[column_data.astype('str').apply(lambda x : x.replace('.','',1).isdigit())].astype('float')
#column_data
two_series['col1'].unique()

two_series = two_series[2:]
two_series

two_series = two_series.groupby('col1').col2.apply(calc_irene)

two_series.index = [i[0] for i in two_series.index]
#two_series.to_excel("out.xlsx")


irene = two_series.apply(lambda x : crea_errores(x, IndiceDeConfianza, poblacion_total), axis=1)
irene = irene.rename(columns={0: "error"})
irene['irene_mas_error'] = irene['irene'] + irene['error']
irene['irene_menos_error'] = irene['irene'] - irene['error']



# @title Texto de título predeterminado
irene.to_excel("out_groupedby_"+column_letter_group+".xlsx")
irene
