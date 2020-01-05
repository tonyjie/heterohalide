#!/bin/bash
# source with-sdaccel
# platform=xilinx_u200_qdma_201910_1
# kernel_name=default_function
# ~blaok/git/soda-internal/src/sodac unsharp_separate.soda --xocl-kernel unsharp_separate_kernel.cpp --recursion-limit 3000 --temporal-cse no

# xocc -t hw -f ${platform} --kernel ${kernel_name}_kernel --xp prop:kernel.${kernel_name}_kernel.kernel_flags="-std=c++0x" -c ${app}_kernel.cpp -o ${app}.hw.xo -s

# ~blaok/git/soda/src/sodac --xocl-platform ~blaok/git/soda/zynq7000 --xocl-hw-xo xofile.xo unsharp_separate.soda --recursion-limit 3000 --temporal-cse no

# # ~blaok/git/soda/src/sodac --xocl-platform /opt/xilinx/platforms/xilinx_u250_xdma_201830_2 --xocl-hw-xo xofile_separate.xo unsharp_separate.soda --recursion-limit 3000 --temporal-cse no
# ~blaok/git/soda/src/report-xo-util <xofile.xo >report_separate_zynq_unroll_8.rpt

# U250 board
# ~blaok/git/soda-internal/src/sodac --xocl-platform /opt/xilinx/platforms/xilinx_u250_xdma_201830_2 --xocl-hw-xo xofile.xo unsharp_separate.soda --recursion-limit 3000 --temporal-cse no
# echo xofile generated
# ~blaok/git/soda-internal/src/report-xo-util <xofile.xo >report_separate_size_2440_unroll_32.rpt
# echo report generated

# F1 board
~blaok/git/soda-internal/src/sodac --xocl-platform /opt/tools/xilinx/aws_platform/xilinx_aws-vu9p-f1-04261818_dynamic_5_0 --xocl-hw-xo xofile.xo unsharp_separate.soda --recursion-limit 3000 --temporal-cse no
echo xofile generated
~blaok/git/soda-internal/src/report-xo-util <xofile.xo >f1_separate_size_2440_unroll_32.rpt
echo report generated