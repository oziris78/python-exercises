


import PySimpleGUI as sg


########################################################

layout = [
	[
		sg.Input(key='-INPUT-'),
		sg.Spin(['km to mile', 'kg to pound', 'sec to min'], key='-UNITS-'),
		sg.Button('Convert', key='-CONVERT-')
	],
	[
		sg.Text('', key='-OUTPUT-')
	]
]

window = sg.Window("Converter App", layout)


########################################################


def main():
	while True:
		event, values = window.read()

		if event == sg.WIN_CLOSED:
			break

		try:
			if event == '-CONVERT-':
				input_value = values['-INPUT-']
				if values['-UNITS-'] == 'km to mile':
					output = round(float(input_value) * 0.6214,2)
					output_string = f'{input_value} km are {output} miles.'
				if values['-UNITS-'] == 'kg to pound':
					output = round(float(input_value) * 2.20462,2)
					output_string = f'{input_value} kg are {output} pounds.'
				if values['-UNITS-'] == 'sec to min':
					output = round(float(input_value) / 60,2)
					output_string = f'{input_value} seconds are {output} minutes.'

				window['-OUTPUT-'].update(output_string)
		except Exception as e:
			window['-OUTPUT-'].update("Please enter a number")

	window.close()


if __name__ == '__main__':
	main()
	