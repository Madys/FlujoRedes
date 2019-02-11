import datetime as dt

#User defined functions
def generate_img_filename(base_name, ext_name):
	current_datetime = dt.datetime.now()
	key = str(current_datetime.year) + \
		str(current_datetime.month) + \
		str(current_datetime.day) + \
		str(current_datetime.hour) + \
		str(current_datetime.minute) + \
		str(current_datetime.second)
	return base_name + key + '.' + ext_name