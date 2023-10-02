import pandas as pd

def horario(name):
    df = pd.read_excel('CONSOLIDADO.xlsx', sheet_name='CONSOLIDADO')
    df = df.drop([0])

    df.columns = ['Source', 'FICHA', 'FORMACIÓN', 'TITULAR', 'TRIMESTRE ACADÉMICO', 'COMPETENCIA', 'NOMBRE DE LA COMPETENCIA', 'RAP 1', 'RAP 2', 'RAP 3', 'RAP 4', 'RAP 5', 'RAP 6', 'INSTRUCTOR', 'NC', 'HORAS SEMANAL', 'NN2', '6-7L', '7-8L', '8-9L', '9-10L', '10-11L', '11-12L', '12-13L', '13-14L', '14-15L', '15-16L', '16-17L', '17-18L', '18-19L', '19-20L', '20-21L', '21-22L', '6-7M', '7-8M', '8-9M', '9-10M', '10-11M', '11-12M', '12-13M', '13-14M', '14-15M', '15-16M', '16-17M', '17-18M', '18-19M', '19-20M', '20-21M', '21-22M', '6-7MI',
                  '7-8MI', '8-9MI', '9-10MI', '10-11MI', '11-12MI', '12-13MI', '13-14MI', '14-15MI', '15-16MI', '16-17MI', '17-18MI', '18-19MI', '19-20MI', '20-21MI', '21-22MI', '6-7J', '7-8J', '8-9J', '9-10J', '10-11J', '11-12J', '12-13J', '13-14J', '14-15J', '15-16J', '16-17J', '17-18J', '18-19J', '19-20J', '20-21J', '21-22J', '6-7V', '7-8V', '8-9V', '9-10V', '10-11V', '11-12V', '12-13V', '13-14V', '14-15V', '15-16V', '16-17V', '17-18V', '18-19V', '19-20V', '20-21V', '21-22V', '6-8S', '8-9S', '9-10S', '10-11S', '11-12S', '12-13S', '13-14S']
    titularInstructor = {}
    if name in df['TITULAR'].values:
        titularInstructor = {
            "ficha": df[df['TITULAR'] == name]['FICHA'].iloc[0],
            "formacion": df[df['TITULAR'] == name]['FORMACIÓN'].iloc[0],
            "trimestre": df[df['TITULAR'] == name]['TRIMESTRE ACADÉMICO'].iloc[0],
        }

    """ Filtrar por nombre del instructor  y guardar el resultado en un nuevo dataframe """
    df = df[df['INSTRUCTOR'] == name]

    df['NC'] = df['NC'].str.split('-').str[1]
    instructor = {
        "nombre": df['INSTRUCTOR'].iloc[0],
        "trimestre": df['TRIMESTRE ACADÉMICO'],
        "competencia": df['NOMBRE DE LA COMPETENCIA'],
        "rap1": df['RAP 1'],
        "rap2": df['RAP 2'],
        "rap3": df['RAP 3'],
        "rap4": df['RAP 4'],
        "rap5": df['RAP 5'],
        "rap6": df['RAP 6'],
        "nc": df['NC'],
        "ficha": df['FICHA'],
        "formacion": df['FORMACIÓN'],
        "titular": df['TITULAR'],
        "horario": {
            "lunes": {
                "6-7": df[df['6-7L'].notnull()][['6-7L', 'NC', 'FICHA']].to_dict('records'),
                "7-8": df[df['7-8L'].notnull()][['7-8L', 'NC', 'FICHA']].to_dict('records'),
                "8-9": df[df['8-9L'].notnull()][['8-9L', 'NC', 'FICHA']].to_dict('records'),
                "9-10": df[df['9-10L'].notnull()][['9-10L', 'NC', 'FICHA']].to_dict('records'),
                "10-11": df[df['10-11L'].notnull()][['10-11L', 'NC', 'FICHA']].to_dict('records'),
                "11-12": df[df['11-12L'].notnull()][['11-12L', 'NC', 'FICHA']].to_dict('records'),
                "12-13": df[df['12-13L'].notnull()][['12-13L', 'NC', 'FICHA']].to_dict('records'),
                "13-14": df[df['13-14L'].notnull()][['13-14L', 'NC', 'FICHA']].to_dict('records'),
                "14-15": df[df['14-15L'].notnull()][['14-15L', 'NC', 'FICHA']].to_dict('records'),
                "15-16": df[df['15-16L'].notnull()][['15-16L', 'NC', 'FICHA']].to_dict('records'),
                "16-17": df[df['16-17L'].notnull()][['16-17L', 'NC', 'FICHA']].to_dict('records'),
                "17-18": df[df['17-18L'].notnull()][['17-18L', 'NC', 'FICHA']].to_dict('records'),
                "18-19": df[df['18-19L'].notnull()][['18-19L', 'NC', 'FICHA']].to_dict('records'),
                "19-20": df[df['19-20L'].notnull()][['19-20L', 'NC', 'FICHA']].to_dict('records'),
                "20-21": df[df['20-21L'].notnull()][['20-21L', 'NC', 'FICHA']].to_dict('records'),
                "21-22": df[df['21-22L'].notnull()][['21-22L', 'NC', 'FICHA']].to_dict('records'),
            },
            "martes": {
                "6-7": df[df['6-7M'].notnull()][['6-7M', 'NC', 'FICHA']].to_dict('records'),
                "7-8": df[df['7-8M'].notnull()][['7-8M', 'NC', 'FICHA']].to_dict('records'),
                "8-9": df[df['8-9M'].notnull()][['8-9M', 'NC', 'FICHA']].to_dict('records'),
                "9-10": df[df['9-10M'].notnull()][['9-10M', 'NC', 'FICHA']].to_dict('records'),
                "10-11": df[df['10-11M'].notnull()][['10-11M', 'NC', 'FICHA']].to_dict('records'),
                "11-12": df[df['11-12M'].notnull()][['11-12M', 'NC', 'FICHA']].to_dict('records'),
                "12-13": df[df['12-13M'].notnull()][['12-13M', 'NC', 'FICHA']].to_dict('records'),
                "13-14": df[df['13-14M'].notnull()][['13-14M', 'NC', 'FICHA']].to_dict('records'),
                "14-15": df[df['14-15M'].notnull()][['14-15M', 'NC', 'FICHA']].to_dict('records'),
                "15-16": df[df['15-16M'].notnull()][['15-16M', 'NC', 'FICHA']].to_dict('records'),
                "16-17": df[df['16-17M'].notnull()][['16-17M', 'NC', 'FICHA']].to_dict('records'),
                "17-18": df[df['17-18M'].notnull()][['17-18M', 'NC', 'FICHA']].to_dict('records'),
                "18-19": df[df['18-19M'].notnull()][['18-19M', 'NC', 'FICHA']].to_dict('records'),
                "19-20": df[df['19-20M'].notnull()][['19-20M', 'NC', 'FICHA']].to_dict('records'),
                "20-21": df[df['20-21M'].notnull()][['20-21M', 'NC', 'FICHA']].to_dict('records'),
                "21-22": df[df['21-22M'].notnull()][['21-22M', 'NC', 'FICHA']].to_dict('records')
            },
            "miercoles": {
                "6-7": df[df['6-7MI'].notnull()][['6-7MI', 'NC', 'FICHA']].to_dict('records'),
                "7-8": df[df['7-8MI'].notnull()][['7-8MI', 'NC', 'FICHA']].to_dict('records'),
                "8-9": df[df['8-9MI'].notnull()][['8-9MI', 'NC', 'FICHA']].to_dict('records'),
                "9-10": df[df['9-10MI'].notnull()][['9-10MI', 'NC', 'FICHA']].to_dict('records'),
                "10-11": df[df['10-11MI'].notnull()][['10-11MI', 'NC', 'FICHA']].to_dict('records'),
                "11-12": df[df['11-12MI'].notnull()][['11-12MI', 'NC', 'FICHA']].to_dict('records'),
                "12-13": df[df['12-13MI'].notnull()][['12-13MI', 'NC', 'FICHA']].to_dict('records'),
                "13-14": df[df['13-14MI'].notnull()][['13-14MI', 'NC', 'FICHA']].to_dict('records'),
                "14-15": df[df['14-15MI'].notnull()][['14-15MI', 'NC', 'FICHA']].to_dict('records'),
                "15-16": df[df['15-16MI'].notnull()][['15-16MI', 'NC', 'FICHA']].to_dict('records'),
                "16-17": df[df['16-17MI'].notnull()][['16-17MI', 'NC', 'FICHA']].to_dict('records'),
                "17-18": df[df['17-18MI'].notnull()][['17-18MI', 'NC', 'FICHA']].to_dict('records'),
                "18-19": df[df['18-19MI'].notnull()][['18-19MI', 'NC', 'FICHA']].to_dict('records'),
                "19-20": df[df['19-20MI'].notnull()][['19-20MI', 'NC', 'FICHA']].to_dict('records'),
                "20-21": df[df['20-21MI'].notnull()][['20-21MI', 'NC', 'FICHA']].to_dict('records'),
                "21-22": df[df['21-22MI'].notnull()][['21-22MI', 'NC', 'FICHA']].to_dict('records')
            },
            "jueves": {
                "6-7": df[df['6-7J'].notnull()][['6-7J', 'NC', 'FICHA']].to_dict('records'),
                "7-8": df[df['7-8J'].notnull()][['7-8J', 'NC', 'FICHA']].to_dict('records'),
                "8-9": df[df['8-9J'].notnull()][['8-9J', 'NC', 'FICHA']].to_dict('records'),
                "9-10": df[df['9-10J'].notnull()][['9-10J', 'NC', 'FICHA']].to_dict('records'),
                "10-11": df[df['10-11J'].notnull()][['10-11J', 'NC', 'FICHA']].to_dict('records'),
                "11-12": df[df['11-12J'].notnull()][['11-12J', 'NC', 'FICHA']].to_dict('records'),
                "12-13": df[df['12-13J'].notnull()][['12-13J', 'NC', 'FICHA']].to_dict('records'),
                "13-14": df[df['13-14J'].notnull()][['13-14J', 'NC', 'FICHA']].to_dict('records'),
                "14-15": df[df['14-15J'].notnull()][['14-15J', 'NC', 'FICHA']].to_dict('records'),
                "15-16": df[df['15-16J'].notnull()][['15-16J', 'NC', 'FICHA']].to_dict('records'),
                "16-17": df[df['16-17J'].notnull()][['16-17J', 'NC', 'FICHA']].to_dict('records'),
                "17-18": df[df['17-18J'].notnull()][['17-18J', 'NC', 'FICHA']].to_dict('records'),
                "18-19": df[df['18-19J'].notnull()][['18-19J', 'NC', 'FICHA']].to_dict('records'),
                "19-20": df[df['19-20J'].notnull()][['19-20J', 'NC', 'FICHA']].to_dict('records'),
                "20-21": df[df['20-21J'].notnull()][['20-21J', 'NC', 'FICHA']].to_dict('records'),
                "21-22": df[df['21-22J'].notnull()][['21-22J', 'NC', 'FICHA']].to_dict('records')                
            },
            "viernes": {
                "6-7": df[df['6-7V'].notnull()][['6-7V', 'NC', 'FICHA']].to_dict('records'),
                "7-8": df[df['7-8V'].notnull()][['7-8V', 'NC', 'FICHA']].to_dict('records'),
                "8-9": df[df['8-9V'].notnull()][['8-9V', 'NC', 'FICHA']].to_dict('records'),
                "9-10": df[df['9-10V'].notnull()][['9-10V', 'NC', 'FICHA']].to_dict('records'),
                "10-11": df[df['10-11V'].notnull()][['10-11V', 'NC', 'FICHA']].to_dict('records'),
                "11-12": df[df['11-12V'].notnull()][['11-12V', 'NC', 'FICHA']].to_dict('records'),
                "12-13": df[df['12-13V'].notnull()][['12-13V', 'NC', 'FICHA']].to_dict('records'),
                "13-14": df[df['13-14V'].notnull()][['13-14V', 'NC', 'FICHA']].to_dict('records'),
                "14-15": df[df['14-15V'].notnull()][['14-15V', 'NC', 'FICHA']].to_dict('records'),
                "15-16": df[df['15-16V'].notnull()][['15-16V', 'NC', 'FICHA']].to_dict('records'),
                "16-17": df[df['16-17V'].notnull()][['16-17V', 'NC', 'FICHA']].to_dict('records'),
                "17-18": df[df['17-18V'].notnull()][['17-18V', 'NC', 'FICHA']].to_dict('records'),
                "18-19": df[df['18-19V'].notnull()][['18-19V', 'NC', 'FICHA']].to_dict('records'),
                "19-20": df[df['19-20V'].notnull()][['19-20V', 'NC', 'FICHA']].to_dict('records'),
                "20-21": df[df['20-21V'].notnull()][['20-21V', 'NC', 'FICHA']].to_dict('records'),
                "21-22": df[df['21-22V'].notnull()][['21-22V', 'NC', 'FICHA']].to_dict('records')
            },
            "sabado": {
                "6-8": df[df['6-8S'].notnull()][['6-8S', 'NC', 'FICHA']].to_dict('records'),
                "8-9": df[df['8-9S'].notnull()][['8-9S', 'NC', 'FICHA']].to_dict('records'),
                "9-10": df[df['9-10S'].notnull()][['9-10S', 'NC', 'FICHA']].to_dict('records'),
                "10-11": df[df['10-11S'].notnull()][['10-11S', 'NC', 'FICHA']].to_dict('records'),
                "11-12": df[df['11-12S'].notnull()][['11-12S', 'NC', 'FICHA']].to_dict('records'),
                "12-13": df[df['12-13S'].notnull()][['12-13S', 'NC', 'FICHA']].to_dict('records'),
                "13-14": df[df['13-14S'].notnull()][['13-14S', 'NC', 'FICHA']].to_dict('records')
            },
            "titularTrimestre": titularInstructor
        }
    }    
    return instructor


def instructores():
    df = pd.read_excel('CONSOLIDADO.xlsx', sheet_name='CONSOLIDADO')
    df = df.drop([0])

    df.columns = ['Source', 'FICHA', 'FORMACIÓN', 'TITULAR', 'TRIMESTRE ACADÉMICO', 'COMPETENCIA', 'NOMBRE DE LA COMPETENCIA', 'RAP 1', 'RAP 2', 'RAP 3', 'RAP 4', 'RAP 5', 'RAP 6', 'INSTRUCTOR', 'NC', 'HORAS SEMANAL', 'NN2', '6-7L', '7-8L', '8-9L', '9-10L', '10-11L', '11-12L', '12-13L', '13-14L', '14-15L', '15-16L', '16-17L', '17-18L', '18-19L', '19-20L', '20-21L', '21-22L', '6-7M', '7-8M', '8-9M', '9-10M', '10-11M', '11-12M', '12-13M', '13-14M', '14-15M', '15-16M', '16-17M', '17-18M', '18-19M', '19-20M', '20-21M', '21-22M', '6-7MI',
                  '7-8MI', '8-9MI', '9-10MI', '10-11MI', '11-12MI', '12-13MI', '13-14MI', '14-15MI', '15-16MI', '16-17MI', '17-18MI', '18-19MI', '19-20MI', '20-21MI', '21-22MI', '6-7J', '7-8J', '8-9J', '9-10J', '10-11J', '11-12J', '12-13J', '13-14J', '14-15J', '15-16J', '16-17J', '17-18J', '18-19J', '19-20J', '20-21J', '21-22J', '6-7V', '7-8V', '8-9V', '9-10V', '10-11V', '11-12V', '12-13V', '13-14V', '14-15V', '15-16V', '16-17V', '17-18V', '18-19V', '19-20V', '20-21V', '21-22V', '6-8S', '8-9S', '9-10S', '10-11S', '11-12S', '12-13S', '13-14S']

    
    
    """ dejar solo la columna instructor con valores unicos"""
    df = df['INSTRUCTOR']
    
    df = df.values.tolist()    
    df = list(set(df))
    """quitar valores nan """
    df = [x for x in df if str(x) != 'nan']
    """ ordenar lista """
    df.sort()   
    
    return df


def competenciasInstructor(name):
    df = pd.read_excel('CONSOLIDADO.xlsx', sheet_name='CONSOLIDADO')
    df_comp = pd.read_excel('Competencias ADSO.xlsx')

    df_comp = df_comp.dropna(axis=1, how='all')

    df = df.drop([0])

    df.columns = ['Source', 'FICHA', 'FORMACIÓN', 'TITULAR', 'TRIMESTRE ACADÉMICO', 'COMPETENCIA', 'NOMBRE DE LA COMPETENCIA', 'RAP 1', 'RAP 2', 'RAP 3', 'RAP 4', 'RAP 5', 'RAP 6', 'INSTRUCTOR', 'NC', 'HORAS SEMANAL', 'NN2', '6-7L', '7-8L', '8-9L', '9-10L', '10-11L', '11-12L', '12-13L', '13-14L', '14-15L', '15-16L', '16-17L', '17-18L', '18-19L', '19-20L', '20-21L', '21-22L', '6-7M', '7-8M', '8-9M', '9-10M', '10-11M', '11-12M', '12-13M', '13-14M', '14-15M', '15-16M', '16-17M', '17-18M', '18-19M', '19-20M', '20-21M', '21-22M', '6-7MI',
                  '7-8MI', '8-9MI', '9-10MI', '10-11MI', '11-12MI', '12-13MI', '13-14MI', '14-15MI', '15-16MI', '16-17MI', '17-18MI', '18-19MI', '19-20MI', '20-21MI', '21-22MI', '6-7J', '7-8J', '8-9J', '9-10J', '10-11J', '11-12J', '12-13J', '13-14J', '14-15J', '15-16J', '16-17J', '17-18J', '18-19J', '19-20J', '20-21J', '21-22J', '6-7V', '7-8V', '8-9V', '9-10V', '10-11V', '11-12V', '12-13V', '13-14V', '14-15V', '15-16V', '16-17V', '17-18V', '18-19V', '19-20V', '20-21V', '21-22V', '6-8S', '8-9S', '9-10S', '10-11S', '11-12S', '12-13S', '13-14S']

    df = df[df['INSTRUCTOR'] == name]

    competencias_instructor = {
        'norma': [],
        'competencia': [],
        'frase': [],
        'n_rap': [],
        'resultados_ap': [],
    }

    for c in df['NC'].str.split('-').str[1].str.strip().tolist():
        for p in df_comp['FRASE O PALABRA CLAVE']:
            if c == p and p not in competencias_instructor['frase']:
                competencias_instructor['norma'].append(df_comp[df_comp['FRASE O PALABRA CLAVE'] == c]['NORMA SECTORIAL DE COMPETENCIA LABORAL (En Sofía Plus)'].iloc[0])
                competencias_instructor['competencia'].append(df_comp[df_comp['FRASE O PALABRA CLAVE'] == c]['COMPETENCIA'].iloc[0])
                competencias_instructor['frase'].append(df_comp[df_comp['FRASE O PALABRA CLAVE'] == c]['FRASE O PALABRA CLAVE'].iloc[0])
                competencias_instructor['n_rap'].append(df_comp[df_comp['FRASE O PALABRA CLAVE'] == c]['N° RAP'].iloc[0])
                competencias_instructor['resultados_ap'].append(df_comp[df_comp['FRASE O PALABRA CLAVE'] == c]['RESULTADOS DE APRENDIZAJE A EVALUAR'].iloc[0])

    return competencias_instructor

def horario_fichas(ficha):
    df = pd.read_excel('CONSOLIDADO.xlsx', sheet_name='CONSOLIDADO')
    df = df.drop([0])

    df.columns = ['Source', 'FICHA', 'FORMACIÓN', 'TITULAR', 'TRIMESTRE ACADÉMICO', 'COMPETENCIA', 'NOMBRE DE LA COMPETENCIA', 'RAP 1', 'RAP 2', 'RAP 3', 'RAP 4', 'RAP 5', 'RAP 6', 'INSTRUCTOR', 'NC', 'HORAS SEMANAL', 'NN2', '6-7L', '7-8L', '8-9L', '9-10L', '10-11L', '11-12L', '12-13L', '13-14L', '14-15L', '15-16L', '16-17L', '17-18L', '18-19L', '19-20L', '20-21L', '21-22L', '6-7M', '7-8M', '8-9M', '9-10M', '10-11M', '11-12M', '12-13M', '13-14M', '14-15M', '15-16M', '16-17M', '17-18M', '18-19M', '19-20M', '20-21M', '21-22M', '6-7MI',
                  '7-8MI', '8-9MI', '9-10MI', '10-11MI', '11-12MI', '12-13MI', '13-14MI', '14-15MI', '15-16MI', '16-17MI', '17-18MI', '18-19MI', '19-20MI', '20-21MI', '21-22MI', '6-7J', '7-8J', '8-9J', '9-10J', '10-11J', '11-12J', '12-13J', '13-14J', '14-15J', '15-16J', '16-17J', '17-18J', '18-19J', '19-20J', '20-21J', '21-22J', '6-7V', '7-8V', '8-9V', '9-10V', '10-11V', '11-12V', '12-13V', '13-14V', '14-15V', '15-16V', '16-17V', '17-18V', '18-19V', '19-20V', '20-21V', '21-22V', '6-8S', '8-9S', '9-10S', '10-11S', '11-12S', '12-13S', '13-14S']
    titularInstructor = {}
    if ficha in df['FICHA'].values:
        titularInstructor = {
            "ficha": df[df['TITULAR'] == ficha]['FICHA'],
            "formacion": df[df['TITULAR'] == ficha]['FORMACIÓN'],
            "trimestre": df[df['TITULAR'] == ficha]['TRIMESTRE ACADÉMICO'],
        }

    """ Filtrar por el numero de ficha antes del espacio y guardar el resultado en un nuevo dataframe """
    df = df[df['FICHA'].str.split(' ').str[0] == ficha]    

    df['NC'] = df['NC'].str.split('-').str[1]
    h_ficha = {
        "nombre": df['INSTRUCTOR'],
        "trimestre": df['TRIMESTRE ACADÉMICO'],
        "competencia": df['NOMBRE DE LA COMPETENCIA'],
        "rap1": df['RAP 1'],
        "rap2": df['RAP 2'],
        "rap3": df['RAP 3'],
        "rap4": df['RAP 4'],
        "rap5": df['RAP 5'],
        "rap6": df['RAP 6'],
        "nc": df['NC'],
        "ficha": df['FICHA'],
        "formacion": df['FORMACIÓN'],
        "titular": df['TITULAR'],
        "horario": {
            "lunes": {
                "6-7": df[df['6-7L'].notnull()][['6-7L', 'NC', 'INSTRUCTOR']].to_dict('records'),
                "7-8": df[df['7-8L'].notnull()][['7-8L', 'NC', 'INSTRUCTOR']].to_dict('records'),
                "8-9": df[df['8-9L'].notnull()][['8-9L', 'NC', 'INSTRUCTOR']].to_dict('records'),
                "9-10": df[df['9-10L'].notnull()][['9-10L', 'NC', 'INSTRUCTOR']].to_dict('records'),
                "10-11": df[df['10-11L'].notnull()][['10-11L', 'NC', 'INSTRUCTOR']].to_dict('records'),
                "11-12": df[df['11-12L'].notnull()][['11-12L', 'NC', 'INSTRUCTOR']].to_dict('records'),
                "12-13": df[df['12-13L'].notnull()][['12-13L', 'NC', 'INSTRUCTOR']].to_dict('records'),
                "13-14": df[df['13-14L'].notnull()][['13-14L', 'NC', 'INSTRUCTOR']].to_dict('records'),
                "14-15": df[df['14-15L'].notnull()][['14-15L', 'NC', 'INSTRUCTOR']].to_dict('records'),
                "15-16": df[df['15-16L'].notnull()][['15-16L', 'NC', 'INSTRUCTOR']].to_dict('records'),
                "16-17": df[df['16-17L'].notnull()][['16-17L', 'NC', 'INSTRUCTOR']].to_dict('records'),
                "17-18": df[df['17-18L'].notnull()][['17-18L', 'NC', 'INSTRUCTOR']].to_dict('records'),
                "18-19": df[df['18-19L'].notnull()][['18-19L', 'NC', 'INSTRUCTOR']].to_dict('records'),
                "19-20": df[df['19-20L'].notnull()][['19-20L', 'NC', 'INSTRUCTOR']].to_dict('records'),
                "20-21": df[df['20-21L'].notnull()][['20-21L', 'NC', 'INSTRUCTOR']].to_dict('records'),
                "21-22": df[df['21-22L'].notnull()][['21-22L', 'NC', 'INSTRUCTOR']].to_dict('records'),
            },
            "martes": {
                "6-7": df[df['6-7M'].notnull()][['6-7M', 'NC', 'INSTRUCTOR']].to_dict('records'),
                "7-8": df[df['7-8M'].notnull()][['7-8M', 'NC', 'INSTRUCTOR']].to_dict('records'),
                "8-9": df[df['8-9M'].notnull()][['8-9M', 'NC', 'INSTRUCTOR']].to_dict('records'),
                "9-10": df[df['9-10M'].notnull()][['9-10M', 'NC', 'INSTRUCTOR']].to_dict('records'),
                "10-11": df[df['10-11M'].notnull()][['10-11M', 'NC', 'INSTRUCTOR']].to_dict('records'),
                "11-12": df[df['11-12M'].notnull()][['11-12M', 'NC', 'INSTRUCTOR']].to_dict('records'),
                "12-13": df[df['12-13M'].notnull()][['12-13M', 'NC', 'INSTRUCTOR']].to_dict('records'),
                "13-14": df[df['13-14M'].notnull()][['13-14M', 'NC', 'INSTRUCTOR']].to_dict('records'),
                "14-15": df[df['14-15M'].notnull()][['14-15M', 'NC', 'INSTRUCTOR']].to_dict('records'),
                "15-16": df[df['15-16M'].notnull()][['15-16M', 'NC', 'INSTRUCTOR']].to_dict('records'),
                "16-17": df[df['16-17M'].notnull()][['16-17M', 'NC', 'INSTRUCTOR']].to_dict('records'),
                "17-18": df[df['17-18M'].notnull()][['17-18M', 'NC', 'INSTRUCTOR']].to_dict('records'),
                "18-19": df[df['18-19M'].notnull()][['18-19M', 'NC', 'INSTRUCTOR']].to_dict('records'),
                "19-20": df[df['19-20M'].notnull()][['19-20M', 'NC', 'INSTRUCTOR']].to_dict('records'),
                "20-21": df[df['20-21M'].notnull()][['20-21M', 'NC', 'INSTRUCTOR']].to_dict('records'),
                "21-22": df[df['21-22M'].notnull()][['21-22M', 'NC', 'INSTRUCTOR']].to_dict('records')
            },
            "miercoles": {
                "6-7": df[df['6-7MI'].notnull()][['6-7MI', 'NC', 'INSTRUCTOR']].to_dict('records'),
                "7-8": df[df['7-8MI'].notnull()][['7-8MI', 'NC', 'INSTRUCTOR']].to_dict('records'),
                "8-9": df[df['8-9MI'].notnull()][['8-9MI', 'NC', 'INSTRUCTOR']].to_dict('records'),
                "9-10": df[df['9-10MI'].notnull()][['9-10MI', 'NC', 'INSTRUCTOR']].to_dict('records'),
                "10-11": df[df['10-11MI'].notnull()][['10-11MI', 'NC', 'INSTRUCTOR']].to_dict('records'),
                "11-12": df[df['11-12MI'].notnull()][['11-12MI', 'NC', 'INSTRUCTOR']].to_dict('records'),
                "12-13": df[df['12-13MI'].notnull()][['12-13MI', 'NC', 'INSTRUCTOR']].to_dict('records'),
                "13-14": df[df['13-14MI'].notnull()][['13-14MI', 'NC', 'INSTRUCTOR']].to_dict('records'),
                "14-15": df[df['14-15MI'].notnull()][['14-15MI', 'NC', 'INSTRUCTOR']].to_dict('records'),
                "15-16": df[df['15-16MI'].notnull()][['15-16MI', 'NC', 'INSTRUCTOR']].to_dict('records'),
                "16-17": df[df['16-17MI'].notnull()][['16-17MI', 'NC', 'INSTRUCTOR']].to_dict('records'),
                "17-18": df[df['17-18MI'].notnull()][['17-18MI', 'NC', 'INSTRUCTOR']].to_dict('records'),
                "18-19": df[df['18-19MI'].notnull()][['18-19MI', 'NC', 'INSTRUCTOR']].to_dict('records'),
                "19-20": df[df['19-20MI'].notnull()][['19-20MI', 'NC', 'INSTRUCTOR']].to_dict('records'),
                "20-21": df[df['20-21MI'].notnull()][['20-21MI', 'NC', 'INSTRUCTOR']].to_dict('records'),
                "21-22": df[df['21-22MI'].notnull()][['21-22MI', 'NC', 'INSTRUCTOR']].to_dict('records')
            },
            "jueves": {
                "6-7": df[df['6-7J'].notnull()][['6-7J', 'NC', 'INSTRUCTOR']].to_dict('records'),
                "7-8": df[df['7-8J'].notnull()][['7-8J', 'NC', 'INSTRUCTOR']].to_dict('records'),
                "8-9": df[df['8-9J'].notnull()][['8-9J', 'NC', 'INSTRUCTOR']].to_dict('records'),
                "9-10": df[df['9-10J'].notnull()][['9-10J', 'NC', 'INSTRUCTOR']].to_dict('records'),
                "10-11": df[df['10-11J'].notnull()][['10-11J', 'NC', 'INSTRUCTOR']].to_dict('records'),
                "11-12": df[df['11-12J'].notnull()][['11-12J', 'NC', 'INSTRUCTOR']].to_dict('records'),
                "12-13": df[df['12-13J'].notnull()][['12-13J', 'NC', 'INSTRUCTOR']].to_dict('records'),
                "13-14": df[df['13-14J'].notnull()][['13-14J', 'NC', 'INSTRUCTOR']].to_dict('records'),
                "14-15": df[df['14-15J'].notnull()][['14-15J', 'NC', 'INSTRUCTOR']].to_dict('records'),
                "15-16": df[df['15-16J'].notnull()][['15-16J', 'NC', 'INSTRUCTOR']].to_dict('records'),
                "16-17": df[df['16-17J'].notnull()][['16-17J', 'NC', 'INSTRUCTOR']].to_dict('records'),
                "17-18": df[df['17-18J'].notnull()][['17-18J', 'NC', 'INSTRUCTOR']].to_dict('records'),
                "18-19": df[df['18-19J'].notnull()][['18-19J', 'NC', 'INSTRUCTOR']].to_dict('records'),
                "19-20": df[df['19-20J'].notnull()][['19-20J', 'NC', 'INSTRUCTOR']].to_dict('records'),
                "20-21": df[df['20-21J'].notnull()][['20-21J', 'NC', 'INSTRUCTOR']].to_dict('records'),
                "21-22": df[df['21-22J'].notnull()][['21-22J', 'NC', 'INSTRUCTOR']].to_dict('records')                
            },
            "viernes": {
                "6-7": df[df['6-7V'].notnull()][['6-7V', 'NC', 'INSTRUCTOR']].to_dict('records'),
                "7-8": df[df['7-8V'].notnull()][['7-8V', 'NC', 'INSTRUCTOR']].to_dict('records'),
                "8-9": df[df['8-9V'].notnull()][['8-9V', 'NC', 'INSTRUCTOR']].to_dict('records'),
                "9-10": df[df['9-10V'].notnull()][['9-10V', 'NC', 'INSTRUCTOR']].to_dict('records'),
                "10-11": df[df['10-11V'].notnull()][['10-11V', 'NC', 'INSTRUCTOR']].to_dict('records'),
                "11-12": df[df['11-12V'].notnull()][['11-12V', 'NC', 'INSTRUCTOR']].to_dict('records'),
                "12-13": df[df['12-13V'].notnull()][['12-13V', 'NC', 'INSTRUCTOR']].to_dict('records'),
                "13-14": df[df['13-14V'].notnull()][['13-14V', 'NC', 'INSTRUCTOR']].to_dict('records'),
                "14-15": df[df['14-15V'].notnull()][['14-15V', 'NC', 'INSTRUCTOR']].to_dict('records'),
                "15-16": df[df['15-16V'].notnull()][['15-16V', 'NC', 'INSTRUCTOR']].to_dict('records'),
                "16-17": df[df['16-17V'].notnull()][['16-17V', 'NC', 'INSTRUCTOR']].to_dict('records'),
                "17-18": df[df['17-18V'].notnull()][['17-18V', 'NC', 'INSTRUCTOR']].to_dict('records'),
                "18-19": df[df['18-19V'].notnull()][['18-19V', 'NC', 'INSTRUCTOR']].to_dict('records'),
                "19-20": df[df['19-20V'].notnull()][['19-20V', 'NC', 'INSTRUCTOR']].to_dict('records'),
                "20-21": df[df['20-21V'].notnull()][['20-21V', 'NC', 'INSTRUCTOR']].to_dict('records'),
                "21-22": df[df['21-22V'].notnull()][['21-22V', 'NC', 'INSTRUCTOR']].to_dict('records')
            },
            "sabado": {
                "6-8": df[df['6-8S'].notnull()][['6-8S', 'NC', 'INSTRUCTOR']].to_dict('records'),
                "8-9": df[df['8-9S'].notnull()][['8-9S', 'NC', 'INSTRUCTOR']].to_dict('records'),
                "9-10": df[df['9-10S'].notnull()][['9-10S', 'NC', 'INSTRUCTOR']].to_dict('records'),
                "10-11": df[df['10-11S'].notnull()][['10-11S', 'NC', 'INSTRUCTOR']].to_dict('records'),
                "11-12": df[df['11-12S'].notnull()][['11-12S', 'NC', 'INSTRUCTOR']].to_dict('records'),
                "12-13": df[df['12-13S'].notnull()][['12-13S', 'NC', 'INSTRUCTOR']].to_dict('records'),
                "13-14": df[df['13-14S'].notnull()][['13-14S', 'NC', 'INSTRUCTOR']].to_dict('records')
            },
            "titularTrimestre": titularInstructor
        }
    }    
    return h_ficha


def fichas():
    df = pd.read_excel('CONSOLIDADO.xlsx', sheet_name='CONSOLIDADO')
    df = df.drop([0])

    df.columns = ['Source', 'FICHA', 'FORMACIÓN', 'TITULAR', 'TRIMESTRE ACADÉMICO', 'COMPETENCIA', 'NOMBRE DE LA COMPETENCIA', 'RAP 1', 'RAP 2', 'RAP 3', 'RAP 4', 'RAP 5', 'RAP 6', 'INSTRUCTOR', 'NC', 'HORAS SEMANAL', 'NN2', '6-7L', '7-8L', '8-9L', '9-10L', '10-11L', '11-12L', '12-13L', '13-14L', '14-15L', '15-16L', '16-17L', '17-18L', '18-19L', '19-20L', '20-21L', '21-22L', '6-7M', '7-8M', '8-9M', '9-10M', '10-11M', '11-12M', '12-13M', '13-14M', '14-15M', '15-16M', '16-17M', '17-18M', '18-19M', '19-20M', '20-21M', '21-22M', '6-7MI',
                  '7-8MI', '8-9MI', '9-10MI', '10-11MI', '11-12MI', '12-13MI', '13-14MI', '14-15MI', '15-16MI', '16-17MI', '17-18MI', '18-19MI', '19-20MI', '20-21MI', '21-22MI', '6-7J', '7-8J', '8-9J', '9-10J', '10-11J', '11-12J', '12-13J', '13-14J', '14-15J', '15-16J', '16-17J', '17-18J', '18-19J', '19-20J', '20-21J', '21-22J', '6-7V', '7-8V', '8-9V', '9-10V', '10-11V', '11-12V', '12-13V', '13-14V', '14-15V', '15-16V', '16-17V', '17-18V', '18-19V', '19-20V', '20-21V', '21-22V', '6-8S', '8-9S', '9-10S', '10-11S', '11-12S', '12-13S', '13-14S']
   
    
    """ dejar solo la columna Ficha con valores unicos antes del espacio"""
    df = df['FICHA'].str.split(' ').str[0]    
       
    df = df.values.tolist()    
    df = list(set(df))
    """quitar valores nan """
    df = [x for x in df if str(x) != 'nan']
    """ ordenar lista """
    df.sort()   
    
    return df

