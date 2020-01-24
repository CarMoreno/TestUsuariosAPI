import openpyxl
import csv
class Elecciones():
    documento = openpyxl.load_workbook('Elecciones.xlsx')
    hoja = documento.get_sheet_by_name('Hoja1')  # Un doc de excel tiene varias hojas..

    def agrupar(self, criterio, paramSearch):
        count = 0
        for fila in self.hoja.rows:
            for columna in fila:
                if paramSearch in str(columna.value):
                    count += 1

        with open('{}.csv'.format(criterio), 'w') as csvfile:
            filewriter = csv.writer(csvfile, delimiter=',')
            filewriter.writerow([criterio, 'Count'])
            filewriter.writerow([paramSearch, count])


elecciones = Elecciones()
elecciones.agrupar('Candidato', 'Juan Perez')
elecciones.agrupar('Partido', 'liberal')
elecciones.agrupar('Puesto', '2')
elecciones.agrupar('Municipio', 'Cali')
elecciones.agrupar('Departamento', 'Antioquia')

