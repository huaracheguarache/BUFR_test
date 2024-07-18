import eccodes

file = open('temp_2024040100.bufr', 'rb')

while True:
    bufr = eccodes.codes_bufr_new_from_file(file)
    if bufr is None:
        break

    eccodes.codes_set(bufr, 'unpack', 1)
    station = eccodes.codes_get(bufr, 'stationNumber')

    try:
        time_delta = eccodes.codes_get_array(bufr, 'timePeriod')

    except eccodes.KeyValueNotFoundError:
        print(f'Station: {station}')
        print('Missing timePeriod!')
        print(40 * '-')

    else:
        air_temp = eccodes.codes_get_array(bufr, 'airTemperature')
        time_length = len(time_delta)
        air_temp_length = len(air_temp)

        if time_length != air_temp_length:
            print('Length mismatch!')
            print(f'Station: {station}')
            print(f'Time length: {time_length}')
            print(f'Air temperature length: {air_temp_length}')
            print(f'Difference: {time_length - air_temp_length:+d}')
            print(40 * '-')

    eccodes.codes_release(bufr)

file.close()
