import openpyxl
from openpyxl.chart import PieChart, Reference

class Bar:
    def Charts(self,Filename):


            wb = openpyxl.load_workbook(Filename)
            sheet = wb.active

            values = Reference(sheet,min_col=2, min_row=3, max_row=14)

            cats = Reference(sheet, min_col=14, min_row=2, max_row=14)

            # Create object of BarChart class
            chart = PieChart()
            chart.add_data(cats, titles_from_data=True)
            chart.set_categories(values)

            # set the title of the chart
            chart.title = "TOTAL BLANK DEPARTMENTS"

            # set the title of the x-axis


            # set the title of the y-axis


            # the top-left corner of the chart
            # is anchored to cell F2 .
            sheet.add_chart(chart,"D16")

            # save the file
            wb.save("My_PIE-CHART2.xlsx")
            print("New Bar-Char xl created in a present directory named as 'My_PIE-CHART2.xlsx'" )
'''except:
            print("File is not exist in current directory or file formate is not in .xlsx")'''
Filename='exel1.xlsx'
object=Bar()
object.Charts(Filename)