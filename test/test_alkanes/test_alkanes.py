# Copyright (C) 2017  Jan Wollschläger <jmw.tau@gmail.com>
# This file is part of Tau.
#
# Tau is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

from matplotlib import pyplot as plt
import unittest
import math
from tau import tau



class TestAlkanes(unittest.TestCase):


    def test_pa_ccs_alkanes(self):
        alkanes = ["methane", "ethane", "propane", "butane", "pentane"]
        reference_ccs = [27.499, 35.806, 42.457, 50.114, 57.079]
        ccs = []
        for alkane in alkanes:
            ccs.append(tau.pa_ccs(xyzfile="{}.xyz".format(alkane),radii='mobcal', fast=True))
        print(ccs)
        print(reference_ccs)
        plt.plot(ccs, reference_ccs, 'bo')
        plt.savefig("alkanes.png")
        plt.show()


if __name__ == '__main__':
    unittest.main()
