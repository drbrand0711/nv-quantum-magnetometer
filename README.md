#### 1\. UGRP\_Presentation

This is a shortcut to the slides used for presentation. These slides mostly contain the same content as the report, apart from a few extra images.

#### 2\. extreme\_mode.lms

.lms files have the eigenmode solvers (FDE,EME,..).
This file is the one used to find the effective index vs gap values for Stage 1 of the Extrem Mode Converter.
The fundamental TE is supposed to be found out manually in each run (of some gap size). The structure group has a script to generate the lossy part of the slab.

#### 3\. gap,neff\_data.txt

The real and imag values of neff obtained by running the above file are entered here.

#### 4\. plot\_neff\_g.py

This python code plots the data of the above file. The sample images are realnvsg.png and imagnvsg.png

#### 5\. gap\_profile.py

This python code computes the gap profile given a and b parameters. The output is plotted as in gap\_profile.png and stored for further use in gap\_profile.csv

#### 6\. Extreme\_Mode\_Converter.fsp

.fsp files have the FDTD solver
This file is used to simulate Stage 1 of the Extreme Mode Converter. The gap data is obtained from a file on disk. Check the script file of the structure group and modify the file accordingly.

#### 7\. apodized\_grating.fsp

This file is used to simulate Stage 2 of the Extreme Mode Converter. The Gaussian beam input source can be experimented with. The parameters of the grating are taken from the paper. The structure group script file has more details

#### 8\. ultra-efficient\_grating.fsp

This file is used to try and replicate the design with the parameters straight from the paper.

#### 9\. ultra\_efficient\_grating\_mode\_solver.lms

This file is used to test the different materials for 532 nm with Diamond on top , to see the field profile, effective index values.

#### 10\. diamond\_grating.fsp

This is the most important file. It contains the design made for 532 nm described in the paper. The structure group script sets up the structure once the parameters are entered. The root node script sets up the monitors and domain, once the structure is set.
The analysis group script should be run after a simulation to get the grating strength value. It takes values from the monitors on top and bottom and evaluates grating strength.

