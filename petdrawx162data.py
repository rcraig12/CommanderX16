#!/usr/bin/python3

# Copyright (c) 2019, Robert Craig
# All rights reserved.

# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions are met:

# 1. Redistributions of source code must retain the above copyright notice, this
#    list of conditions and the following disclaimer.

# 2. Redistributions in binary form must reproduce the above copyright notice,
#    this list of conditions and the following disclaimer in the documentation
#    and/or other materials provided with the distribution.

# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS"
# AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE
# IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE
# DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE LIABLE
# FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL
# DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR
# SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER
# CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY,
# OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE
# OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.


# Converts a petdrawx16 save file to a assembler byte array

import numpy as np
import math
import sys
import argparse

# parse arguments
parser = argparse.ArgumentParser(formatter_class=argparse.RawTextHelpFormatter,
    description="Converts a PETDRAWX16 save file to Commander X16 byte data.\n\n"
    "optional arguments have defaults of 'data' and 32 if not used.\n\n"
    )

parser.add_argument("input", help="the PETDRAW16 input file name")
parser.add_argument("output", help="the output file name")
parser.add_argument("-l" , "--label", default="data", help="the label for the data", type=str)
parser.add_argument("-w" , "--width", default=32, help="Width of data output", type=int)

args = parser.parse_args()

outputWidth = args.width
lblname = args.label

# load file
p = np.fromfile(args.input, dtype='uint8')

# convert to data
with open(args.output, "w") as file:
    file.write("%s:\n" % lblname)
    i = 0
    counter = 0
    for x in p:
        if i == 0 and counter > 1:
            file.write("    !byte ")    
        if counter > 1:
            file.write("$%02x" % x)
            if i < (outputWidth - 1) and (counter + 1) < p.size:
                file.write(",")
            i = i + 1
            if i == outputWidth:
                file.write("\n")
                i = 0
        counter = counter + 1
