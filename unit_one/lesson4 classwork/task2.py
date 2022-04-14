"""
<select>
	<option>Электроник</option>
	<option>Сыроежкин</option>
	<option>Чижиков</option>
	<option>Кукушкина</option>
</select>
"""

str = '<select>\n'
for i in ['Электроник','Сыроежкин', 'Чижиков', 'Кукушкина']:
  str   += '\t<option>' + i + '</option>\n'
print( str + '</select>')

