#!/bin/bash

# Uncomment to debug
#set -x

# Colour definitions
KNRM="\x1B[0m"
KRED="\x1B[31m"
KGRN="\x1B[32m"
KYEL="\x1B[33m"
KBLU="\x1B[34m"
KMAG="\x1B[35m"
KCYN="\x1B[36m"
KWHT="\x1B[37m"
KRESET="\033[0m"


 # Number of iterations
n_iter=$1

# Cleaning and creating log files
echo -e "${KCYN}Cleaning last test/log_1.tmp  test/log_2.tmp test/log_3.tmp files ...\n"
echo -e "${KGRN} \t rm test/log_1.tmp test/log_2.tmp test/log_3.tmp ...\n"
rm  test/log_1.tmp test/log_2.tmp test/log_3.tmp 

echo -e "${KCYN}Cleaning last test/clk_fun_ubmk.log test/stats.log files ...\n"
echo -e "${KGRN} \t rm test/clk_fun_ubmk.log test/stats.log ...\n"
rm  test/clk_fun_ubmk.log test/stats.log

echo -e "${KCYN}Creating tmp file test/log_1.tmp  test/log_2.tmp test/log_3.tmp files ...\n"
echo -e "${KGRN} \t touch  test/log_1.tmp test/log_2.tmp test/log_3.tmp ...\n"
touch  test/log_1.tmp test/log_2.tmp test/log_3.tmp  


# Creating binaries ...
echo -e "${KCYN}Creating binaries:\n  "
echo -e "${KGRN} \t  make cleanall && make && make clk_fun_ubmk_knl.cubin \n"
make cleanall && make && make clk_fun_ubmk_knl.cubin 


#########################################
# Test:Clock function control flow graph #
#########################################
echo -e "${KCYN} Test: Clock function control flow graph ${KRESET}"


# Each line can be commented or uncommented or changed 
# to modify the behaviour of the program

# name and location of the executable file
CUBIN="cubin/clk_fun_ubmk_knl.cubin "
if [ ! -f ${CUBIN} ]; then
   echo -e "${KRED}The cubin file doesn't exist, did you run make clk_fun_ubmk_knl.cubin?${KRESET}"
   exit 0
fi


# Output File nameArguments
OUTPUT=${OUTPUT}"cubin/clk_fun_ubmk_knl_cfg"
 
# CUDA binary tools
NVDISASM=${NVDISASM}"nvdisasm"

# Arguments
ARGS_1=${ARG_1}" -cfg ${CUBIN}"
ARGS_2=${ARG_2}" dot -o ${OUTPUT}.png -Tpng"


 echo -e "${KCYN}Command to be executed:\n   "
 echo -e "${KGRN} \t ${NVDISASM} ${ARGS_1} | ${ARGS_2} \n"
${NVDISASM} ${ARGS_1} | ${ARGS_2}



#########################################
# Test: clock function latency microbenchmark #
#########################################
echo -e "${KCYN} Test: Clock function latency microbenchmark ${KRESET}"


# Each line can be commented or uncommented or changed 
# to modify the behaviour of the program

# name and location of the executable file
EXECUTABLE="bin/clk_fun_ubmk "
if [ ! -f ${EXECUTABLE} ]; then
   echo -e "${KRED}The execution file doesn't exist, did you already compile it?${KRESET}"
   exit 0
fi


# Log File name, arguments
LOG_FILE=${LOG_FILE}"clk_fun_ubmk.log"
TMP_LOG_FILE=${TMP_LOG_FILE}"tmp_clk_fun_ubmk.log"
BLOCK_SIZE=32

# Executing the binaries n_iter times ...
echo -e "${KCYN}Command to be executed ${n_iter} time(s)\n  "
echo -e "${KGRN} \t ./bin/clk_fun_ubmk ${BLOCK_SIZE} \n"

# Number of warps  from 1 to 32 
for ((i=1; i<=32; i++))
#for ((i=1; i<=1; i++))
    do
        echo -e "${KMAG}--> Number of warps: "$i".\n"
        for ((j=1; j<=${n_iter}; j++))
            do
                echo -e "${KBLU} \t --> Iteration number: "$j".\n"
                ./bin/clk_fun_ubmk $((BLOCK_SIZE*i)) >> test/${LOG_FILE}
                cat test/${LOG_FILE} >> test/${TMP_LOG_FILE}
                awk 'NR == 23 {print }' test/${TMP_LOG_FILE} >>  test/log_1.tmp
                rm test/${TMP_LOG_FILE}
        done

        # Filtering information in the file (I just need the numbers :-P)
        awk  '{print $1}'  test/log_1.tmp >> test/log_2.tmp && rm test/log_1.tmp
        
        # Latency average for ${n_iter} iterations and $i warp(s) ..."
        awk '{for(i=1; i<=NF; i++)  sum=sum + $i;} END {print sum/NR; }' test/log_2.tmp >> test/log_3.tmp && rm test/log_2.tmp

done

# Statistic measurements
echo -e "${KGRN}Statictis measurements: histogram, mode, media, variance, standard deviation."
echo -e "${KCYN}Command to be executed:\n "
echo -e "${KGRN} \t python stats.py\n"
python test/stats.py >> test/stats.log


# Exit message
echo -e "${KYEL} Done 8-) !"

