load 7xy7_HID_gromacs.pdb 

remove resn popc
remove resn CL-
select bm. not solvent around 10.0 and solvent
remove not sele

save selected_water.pdb

quit
