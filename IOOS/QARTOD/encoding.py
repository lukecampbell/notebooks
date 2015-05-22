#!/usr/bin/env python
from netCDF4 import Dataset
import numpy as np

class EncodingExample:
    def __init__(self):
        self.nc = None


    def __enter__(self):
        self.nc = Dataset('/tmp/example.nc', 'w')
        return self

    def __exit__(self, type, value, traceback):
        try:
            self.nc.close()
        except:
            pass

    def make_file(self):
        self.nc.createDimension('time')
        t_var = self.nc.createVariable('temperature', np.float32, ('time',), fill_value=-9999.)
        t_var.standard_name = 'seawater_temperature'
        t_var.units = 'deg_C'
        t_var.long_name = 'Surface Temperature'
        qc_var = self.nc.createVariable('temperature_qc', np.uint8, ('time',), fill_value=np.uint8(9))
        qc_var.standard_name = 'seawater_temperature status_flag'
        qc_var.long_name = 'Surface Temperature Quality Flag'
        qc_var.flag_values = np.array([1, 2, 3, 4, 9], dtype=np.uint8)
        qc_var.flag_meanings = "quality_good not_evaluated suspect fail missing_data"

        qc_var = self.nc.createVariable('temperature_tests_qc', np.uint64, ('time',))
        qc_var.standard_name = 'seawater_temperature status_flag'
        qc_var.long_name = 'Seawater Temperature Test Flag'
        qc_var.flag_decode_instructions = 'http://www.ioos.noaa.gov/qartod/welcome.html'



def main():
    with EncodingExample() as encoding:
        encoding.make_file()

if __name__ == '__main__':
    main()
